from typing import List, Any
import logging
from jinja2 import Template, TemplateError, StrictUndefined
from at_common_functions.utils.storage import get_storage
from at_common_models.system.prompt import PromptModel
from at_common_functions.utils.openai import get_openai
from babel.numbers import format_currency, format_decimal, format_percent

logger = logging.getLogger(__name__)

async def get_prompt(prompt_name: str) -> PromptModel:
    """Retrieve prompt template from storage."""
    storage = get_storage()
    prompts: List[PromptModel] = await storage.query(
        model_class=PromptModel,
        filters=[PromptModel.name == prompt_name]
    )

    if len(prompts) == 0:
        raise ValueError(f"No prompt found for name: {prompt_name}")
    if len(prompts) > 1:
        raise ValueError(f"Multiple prompts found for name: {prompt_name}, got {len(prompts)}")
    
    return prompts[0]

def setup_jinja_environment():
    """Configure and return Jinja2 environment with custom filters."""
    env = Template.environment_class()
    env.filters['format_currency'] = format_currency
    env.filters['format_number'] = format_decimal
    env.filters['format_decimal'] = format_decimal
    env.filters['format_percent'] = format_percent
    env.undefined = StrictUndefined
    return env

def render_prompts(prompt: PromptModel, env, **kwargs) -> tuple[str, str]:
    """Render system and user prompts using the template."""
    try:
        sys_template = env.from_string(prompt.sys_tpl)
        usr_template = env.from_string(prompt.usr_tpl)
        
        return (
            sys_template.render(**kwargs),
            usr_template.render(**kwargs)
        )
    except TemplateError as e:
        logger.error(f"Failed to render template for prompt {prompt.name}: {str(e)}")
        raise

async def inference(*, model: str, prompt_name: str, **kwargs: Any) -> str:
    """
    Generate an inference using OpenAI's chat model with templated prompts.
    
    Args:
        model: OpenAI model identifier
        prompt_name: Name of the prompt template to use
        **kwargs: Additional keyword arguments to pass to the prompt template
    
    Returns:
        str: The model's response
    """
    if not model:
        raise ValueError("Model parameter cannot be empty")

    prompt = await get_prompt(prompt_name)
    env = setup_jinja_environment()
    system_prompt, user_prompt = render_prompts(prompt, env, **kwargs)

    openai = get_openai()
    response = await openai.chat(
        system=system_prompt,
        user=user_prompt,
        model=model,
        temperature=prompt.param_temperature,
        max_tokens=prompt.param_max_tokens
    )
    
    return response
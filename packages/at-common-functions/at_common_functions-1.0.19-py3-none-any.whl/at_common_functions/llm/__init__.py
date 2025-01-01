from at_common_functions.llm.impls.inference import inference as _inference
from at_common_workflow import export
from typing import Any

@export
async def inference(*, model: str, prompt_name: str, **kwargs: Any) -> str:
    return await _inference(model=model, prompt_name=prompt_name, **kwargs)
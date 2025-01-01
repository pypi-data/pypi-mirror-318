import pytest
from unittest.mock import MagicMock, patch, AsyncMock
from at_common_functions.news import list_stocks
from at_common_models.news.stock import NewsStockModel
from at_common_models.news.article import NewsArticleModel
from datetime import datetime, timedelta
import pytest_asyncio

TEST_SYMBOL = "AAPL"

@pytest_asyncio.fixture
async def mock_storage():
    storage = MagicMock()
    
    # Use current time for test data
    current_time = datetime.now()
    two_days_ago = current_time - timedelta(days=2)
    five_days_ago = current_time - timedelta(days=5)
    
    # Sample test data with relative dates
    stock_news = [
        NewsStockModel(
            news_id="article1",
            symbol=TEST_SYMBOL,
            published_at=two_days_ago  # 2 days ago
        ),
        NewsStockModel(
            news_id="article2",
            symbol=TEST_SYMBOL,
            published_at=five_days_ago  # 5 days ago
        )
    ]
    
    articles = [
        NewsArticleModel(
            id="article1",
            source="Test Source",
            headline="Test Headline 1",
            summary="Test Summary 1",
            url="http://test1.com",
            published_at=two_days_ago  # 2 days ago
        ),
        NewsArticleModel(
            id="article2",
            source="Test Source",
            headline="Test Headline 2",
            summary="Test Summary 2",
            url="http://test2.com",
            published_at=five_days_ago  # 5 days ago
        )
    ]
    
    async def mock_query(model_class, filters, sort=None, limit=None):
        # Add debug prints
        print(f"\nQuery called with:")
        print(f"model_class: {model_class}")
        print(f"filters: {filters}")
        print(f"sort: {sort}")
        print(f"limit: {limit}")
        
        if model_class == NewsStockModel:
            filtered_news = stock_news.copy()
            
            for filter_condition in filters:
                if hasattr(filter_condition.left, 'key'):
                    key = filter_condition.left.key
                    value = filter_condition.right.value if hasattr(filter_condition.right, 'value') else filter_condition.right
                    print(f"Filtering {key} with value {value}")
                    
                    if key == 'symbol':
                        filtered_news = [n for n in filtered_news if n.symbol == value]
                    elif key == 'published_at':
                        filtered_news = [n for n in filtered_news if n.published_at >= value]
            
            if sort:
                filtered_news.sort(key=lambda x: x.published_at, reverse=True)
            
            result = filtered_news[:limit] if limit else filtered_news
            print(f"Returning NewsStockModel results: {[n.news_id for n in result]}")  # Print IDs for clarity
            return result
            
        elif model_class == NewsArticleModel:
            if not filters:
                print("No filters for NewsArticleModel")
                return []
                
            article_ids = filters[0].right.value if hasattr(filters[0].right, 'value') else filters[0].right
            print(f"Looking for articles with IDs: {article_ids}")
            filtered_articles = [a for a in articles if a.id in article_ids]
            print(f"Returning NewsArticleModel results: {[a.id for a in filtered_articles]}")  # Print IDs for clarity
            return filtered_articles
        
        return []

    storage.query = AsyncMock(side_effect=mock_query)
    return storage

@pytest.mark.asyncio
@patch('at_common_functions.news.impls.stock.get_storage')
async def test_list_stocks_success(mock_get_storage, mock_storage):
    mock_get_storage.return_value = mock_storage
    
    # Add debug print for current time
    print(f"\nCurrent time: {datetime.now()}")
    
    result = await list_stocks(symbol=TEST_SYMBOL, limit=2)
    
    # Add debug print for result
    print(f"Test result: {result}")
    
    assert isinstance(result, list)
    assert len(result) == 2
    
    for article in result:
        assert isinstance(article, dict)
        assert "id" in article
        assert "source" in article
        assert "headline" in article
        assert "summary" in article
        assert "url" in article
        assert "published_at" in article

@pytest.mark.asyncio
@patch('at_common_functions.news.impls.stock.get_storage')
async def test_list_stocks_no_results(mock_get_storage, mock_storage):
    mock_get_storage.return_value = mock_storage
    
    result = await list_stocks(symbol="INVALID_SYMBOL", limit=5)
    
    assert isinstance(result, list)
    assert len(result) == 0

@pytest.mark.asyncio
@patch('at_common_functions.news.impls.stock.get_storage')
async def test_list_stocks_with_limit(mock_get_storage, mock_storage):
    mock_get_storage.return_value = mock_storage
    
    result = await list_stocks(symbol=TEST_SYMBOL, limit=1)
    
    assert isinstance(result, list)
    assert len(result) == 1

@pytest.mark.asyncio
@patch('at_common_functions.news.impls.stock.get_storage')
async def test_list_stocks_with_days_back(mock_get_storage, mock_storage):
    mock_get_storage.return_value = mock_storage
    
    result = await list_stocks(
        symbol=TEST_SYMBOL, 
        limit=2,
        days_back=7
    )
    
    assert isinstance(result, list)
    assert len(result) == 2

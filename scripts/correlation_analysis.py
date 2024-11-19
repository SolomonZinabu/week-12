import pandas as pd


def align_datasets(stock_data: pd.DataFrame, sentiment_data: pd.DataFrame) -> pd.DataFrame:
    """
    Align stock and sentiment data by date.
    
    Args:
        stock_data (pd.DataFrame): Stock data with 'Date' and 'Daily_Return' columns.
        sentiment_data (pd.DataFrame): Sentiment data with 'date' and 'average_sentiment' columns.
        
    Returns:
        pd.DataFrame: Combined data with 'Date', 'Daily_Return', and 'average_sentiment'.
    """
    # Ensure both columns are datetime64[ns]
    stock_data['Date'] = pd.to_datetime(stock_data['Date'], errors='coerce')
    sentiment_data['date'] = pd.to_datetime(sentiment_data['date'], errors='coerce')
    
    # Merge the datasets
    combined_data = pd.merge(stock_data, sentiment_data, left_on='Date', right_on='date', how='inner')
    
    # Select relevant columns
    return combined_data[['Date', 'Daily_Return', 'average_sentiment']]


def calculate_pearson_correlation(combined_data: pd.DataFrame) -> float:
    """
    Calculate Pearson correlation between stock returns and sentiment scores.
    
    Args:
        combined_data (pd.DataFrame): Data with 'Daily_Return' and 'average_sentiment' columns.
        
    Returns:
        float: Pearson correlation coefficient.
    """
    return combined_data['Daily_Return'].corr(combined_data['average_sentiment'])

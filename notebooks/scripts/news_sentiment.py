from textblob import TextBlob
import pandas as pd

def analyze_sentiment(headline: str) -> str:
    """
    Analyze the sentiment of a headline using TextBlob.
    
    Args:
        headline (str): News headline.
        
    Returns:
        str: Sentiment category (positive, negative, neutral).
    """
    polarity = TextBlob(headline).sentiment.polarity
    if polarity > 0:
        return 'positive'
    elif polarity < 0:
        return 'negative'
    else:
        return 'neutral'

def calculate_sentiment_scores(news_data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate sentiment scores for news headlines and aggregate by day.
    
    Args:
        news_data (pd.DataFrame): DataFrame with 'date' and 'headline' columns.
        
    Returns:
        pd.DataFrame: Daily average sentiment scores.
    """
    news_data['sentiment'] = news_data['headline'].apply(lambda x: TextBlob(x).sentiment.polarity)
    daily_sentiment = news_data.groupby('date')['sentiment'].mean().reset_index()
    daily_sentiment.rename(columns={'sentiment': 'average_sentiment'}, inplace=True)
    return daily_sentiment

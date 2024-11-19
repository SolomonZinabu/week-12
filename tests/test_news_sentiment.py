import pandas as pd
from scripts.news_sentiment import analyze_sentiment, calculate_sentiment_scores

def test_analyze_sentiment():
    assert analyze_sentiment("This is great!") == 'positive'
    assert analyze_sentiment("This is bad.") == 'negative'
    assert analyze_sentiment("This is okay.") == 'neutral'

def test_calculate_sentiment_scores():
    news_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-01', '2023-01-02'],
        'headline': ['Good news!', 'Bad news!', 'Neutral news.']
    })
    daily_sentiment = calculate_sentiment_scores(news_data)
    assert len(daily_sentiment) == 2
    assert daily_sentiment.iloc[0]['average_sentiment'] > 0
    assert daily_sentiment.iloc[1]['average_sentiment'] == 0

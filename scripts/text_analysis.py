from textblob import TextBlob
from sklearn.feature_extraction.text import CountVectorizer

def perform_sentiment_analysis(headlines: list) -> list:
    """
    Perform sentiment analysis on a list of headlines.
    
    Args:
        headlines (list): List of news headlines.
        
    Returns:
        list: List of sentiment scores (positive, neutral, negative).
    """
    sentiment_scores = []
    for headline in headlines:
        polarity = TextBlob(headline).sentiment.polarity
        if polarity > 0:
            sentiment_scores.append('positive')
        elif polarity < 0:
            sentiment_scores.append('negative')
        else:
            sentiment_scores.append('neutral')
    return sentiment_scores

def extract_keywords(headlines: list, n_keywords: int = 10) -> list:
    """
    Extract common keywords from headlines using CountVectorizer.
    
    Args:
        headlines (list): List of news headlines.
        n_keywords (int): Number of top keywords to extract.
        
    Returns:
        list: List of top keywords.
    """
    vectorizer = CountVectorizer(max_features=n_keywords, stop_words='english')
    keywords = vectorizer.fit_transform(headlines)
    return vectorizer.get_feature_names_out()

import pandas as pd
from scripts.correlation_analysis import align_datasets, calculate_pearson_correlation

def test_align_datasets():
    stock_data = pd.DataFrame({
        'Date': ['2023-01-01', '2023-01-02'],
        'Daily_Return': [1.5, -0.5]
    })
    sentiment_data = pd.DataFrame({
        'date': ['2023-01-01', '2023-01-02'],
        'average_sentiment': [0.8, -0.2]
    })
    aligned_data = align_datasets(stock_data, sentiment_data)
    assert len(aligned_data) == 2
    assert 'Daily_Return' in aligned_data.columns
    assert 'average_sentiment' in aligned_data.columns

def test_calculate_pearson_correlation():
    combined_data = pd.DataFrame({
        'Daily_Return': [1.5, -0.5],
        'average_sentiment': [0.8, -0.2]
    })
    correlation = calculate_pearson_correlation(combined_data)
    assert -1 <= correlation <= 1

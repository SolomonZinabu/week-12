import pandas as pd

def calculate_text_length(df: pd.DataFrame, text_column: str) -> pd.Series:
    """
    Calculate the length of text in a specified column.
    
    Args:
        df (pd.DataFrame): DataFrame containing the text data.
        text_column (str): Column name for text data.
    
    Returns:
        pd.Series: Series containing text lengths.
    """
    return df[text_column].str.len()

def count_by_column(df: pd.DataFrame, column: str) -> pd.Series:
    """
    Count occurrences of unique values in a column.
    
    Args:
        df (pd.DataFrame): DataFrame to analyze.
        column (str): Column name to count by.
    
    Returns:
        pd.Series: Counts of unique values.
    """
    return df[column].value_counts()

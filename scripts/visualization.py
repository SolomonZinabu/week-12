import matplotlib.pyplot as plt
import seaborn as sns
import pandas as pd
def plot_counts(counts: pd.Series, title: str, xlabel: str, ylabel: str):
    """
    Plot bar chart for counts of unique values in a series.
    
    Args:
        counts (pd.Series): Series containing counts of unique values.
        title (str): Chart title.
        xlabel (str): X-axis label.
        ylabel (str): Y-axis label.
    """
    plt.figure(figsize=(10, 6))
    sns.barplot(x=counts.index, y=counts.values)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.xticks(rotation=45)
    plt.show()

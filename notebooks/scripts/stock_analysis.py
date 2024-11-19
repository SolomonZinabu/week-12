import pandas as pd
import talib
import yfinance as yf

def load_stock_data(ticker: str, start_date: str, end_date: str) -> pd.DataFrame:
    """
    Load stock price data using yfinance.
    
    Args:
        ticker (str): Stock ticker (e.g., "AAPL").
        start_date (str): Start date in YYYY-MM-DD format.
        end_date (str): End date in YYYY-MM-DD format.
        
    Returns:
        pd.DataFrame: Stock price data.
    """
    stock = yf.Ticker(ticker)
    data = stock.history(start=start_date, end=end_date)
    data.reset_index(inplace=True)
    return data

def calculate_technical_indicators(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate technical indicators for stock data.
    
    Args:
        data (pd.DataFrame): Stock price data with 'Close' column.
        
    Returns:
        pd.DataFrame: DataFrame with additional indicator columns.
    """
    data['SMA_20'] = talib.SMA(data['Close'], timeperiod=20)
    data['EMA_20'] = talib.EMA(data['Close'], timeperiod=20)
    data['RSI'] = talib.RSI(data['Close'], timeperiod=14)
    macd, macd_signal, macd_hist = talib.MACD(data['Close'], fastperiod=12, slowperiod=26, signalperiod=9)
    data['MACD'] = macd
    data['MACD_Signal'] = macd_signal
    data['MACD_Hist'] = macd_hist
    return data

def calculate_daily_returns(data: pd.DataFrame) -> pd.DataFrame:
    """
    Calculate daily stock returns as percentage change in closing prices.
    
    Args:
        data (pd.DataFrame): Stock price data with 'Close' column.
        
    Returns:
        pd.DataFrame: DataFrame with an additional 'Daily_Return' column.
    """
    data['Daily_Return'] = data['Close'].pct_change() * 100
    return data

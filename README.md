# Part 1: Overview and Setup
# Financial News Sentiment Analysis for Stock Price Prediction

This project aims to analyze financial news headlines, derive sentiment scores, and correlate them with stock price movements. It has been enhanced with advanced features like CI/CD pipelines, testing, and interactive visualizations.

## Features
- **Sentiment Analysis**: Automated sentiment scoring using `TextBlob`.
- **Stock Analysis**: Technical indicators like SMA, EMA, RSI, and MACD.
- **Statistical Insights**: Correlation analysis between sentiment and stock returns.
- **CI/CD Integration**: Automated testing and deployment using GitHub Actions.
- **Interactive Visualizations**: Insights displayed via time series and scatter plots.

---

## Installation and Setup

### Prerequisites
- Python 3.9 or higher
- pip (Python package manager)

### Clone the Repository
```bash
git clone https://github.com/SolomonZinabu/week-12.git
cd week-12

Install Dependencies

Install Dependencies

pip install -r requirements.txt

Run Tests Locally

pytest tests/

Project Structure

project/
├── notebooks/
│   ├── task-1.ipynb          # EDA and Data Preparation
│   ├── task-2.ipynb          # Stock Analysis
│   ├── task-3.ipynb          # Correlation Analysis
├── scripts/
│   ├── news_sentiment.py     # Sentiment Analysis Functions
│   ├── correlation_analysis.py # Dataset Alignment and Correlation
│   ├── stock_analysis.py     # Stock Data Processing
├── tests/
│   ├── test_news_sentiment.py # Unit Tests for Sentiment Analysis
│   ├── test_correlation_analysis.py # Unit Tests for Correlation
│   ├── test_stock_analysis.py # Unit Tests for Stock Analysis
├── .github/
│   └── workflows/
│       └── ci.yml            # CI/CD Pipeline Configuration
├── requirements.txt          # Project Dependencies
├── README.md                 # Project Documentation
├── LICENSE                   # License Information


Notebooks
Explore results and visualizations in:

notebooks/task-1.ipynb: EDA
notebooks/task-2.ipynb: Stock Analysis
notebooks/task-3.ipynb: Correlation Analysis


Key Features
Sentiment Analysis
Sentiment categories: Positive, Negative, Neutral
Aggregated daily sentiment scores for correlation analysis.
Stock Analysis
Calculated indicators:
SMA: 20-day Simple Moving Average
EMA: 20-day Exponential Moving Average
RSI: Relative Strength Index
MACD: Moving Average Convergence Divergence
Generated processed stock data for further analysis.
Correlation Analysis
Computed Pearson correlation coefficient between daily stock returns and sentiment scores.
Visualized insights through scatter plots and time series overlays.


---

### **Part 3: CI/CD and Testing**

```bash
## CI/CD Pipeline

### Features
- **Continuous Integration**: Automated testing on every push/pull request using GitHub Actions.
- **Documentation Deployment**: Auto-generated documentation hosted on GitHub Pages.
- **Slack Notifications**: Build failure notifications sent to Slack.

### Configuration
- CI/CD pipeline located in `.github/workflows/ci.yml`.
- Includes linting, formatting, testing, and deployment steps.

---

## Testing

### Unit Tests
- Tests for individual functions in `scripts/`.
- Example:
```bash
def test_analyze_sentiment():
    assert analyze_sentiment("This is amazing!") == 'positive'


Run Tests

pytest tests/

Coverage
90% test coverage ensured.

Contribution Guidelines

Fork the repository and create a new branch for your changes.
Submit a pull request to the main branch with a clear description.


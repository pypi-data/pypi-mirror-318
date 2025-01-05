import pandas as pd
import yfinance as yf


class PortfolioDataFetcher:
    def __init__(self, assets: list, benchmark_ticker: str = "SPY"):
        """
        Initialize the PortfolioDataFetcher with assets.
        :param assets: A list of asset tickers (e.g., ["AAPL", "GOOGL", "AMZN"]).
        :param benchmark_ticker: Ticker for the benchmark (default is "SPY").
        """
        if not assets:
            raise ValueError("Asset list cannot be empty.")

        self.assets = assets
        self.benchmark_ticker = benchmark_ticker

    def fetch_assets_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch price and dividend data for all assets in the portfolio.
        :param start_date: Start date for the data.
        :param end_date: End date for the data.
        :return: A DataFrame containing price and dividend data for all assets.
        """
        all_assets_data = {}
        for asset in self.assets:
            ticker = yf.Ticker(asset)
            price_data = ticker.history(start=start_date, end=end_date)["Close"]
            price_data.name = asset

            dividend_data = ticker.dividends
            dividend_data.name = f"{asset}_dividends_per_share"

            combined_data = pd.concat([price_data, dividend_data], axis=1)
            all_assets_data[asset] = combined_data

        return pd.concat(all_assets_data.values(), axis=1).fillna(0)

    def fetch_benchmark_data(self, start_date: str, end_date: str) -> pd.Series:
        """
        Fetch the benchmark data (SPY by default, or user-provided benchmark ticker).
        :param start_date: Start date for the benchmark data.
        :param end_date: End date for the benchmark data.
        :return: A pandas Series containing the benchmark data.
        """
        benchmark_ticker = yf.Ticker(self.benchmark_ticker)
        benchmark_data = benchmark_ticker.history(start=start_date, end=end_date)[
            "Close"
        ]
        benchmark_data.name = self.benchmark_ticker
        return benchmark_data

    def fetch_core_data(self, start_date: str, end_date: str) -> pd.DataFrame:
        """
        Fetch both the assets and benchmark data, returning the core data.
        :param start_date: Start date for the data.
        :param end_date: End date for the data.
        :return: A DataFrame combining both assets and benchmark data.
        """
        # Fetch asset data
        assets_data = self.fetch_assets_data(start_date, end_date)

        # Fetch benchmark data
        benchmark_data = self.fetch_benchmark_data(start_date, end_date)

        self.core_data = pd.concat([assets_data, benchmark_data], axis=1)
        return self.core_data

import os
from typing import Any, Dict

import pandas as pd


class PortfolioConfigLoader:
    def __init__(self, portfolio_setup_file_path: str, total_investment: float):
        """
        Initialize the Portfolio Backtester.
        :param portfolio_setup_file_path: Path to the configuration Excel or CSV file.
        :param total_investment: Total amount of money invested in the portfolio.
        """
        if total_investment <= 0:
            raise ValueError("Total investment must be a positive value.")
        self.total_investment: float = total_investment
        self.portfolio_config: pd.DataFrame = self._load_config(
            portfolio_setup_file_path
        )

    def _load_config(self, portfolio_setup_file_path: str) -> pd.DataFrame:
        """
        Load the portfolio configuration from a file (Excel or CSV).
        :param portfolio_setup_file_path: Path to the configuration file.
        :return: A DataFrame containing the portfolio configuration.
        """
        if not os.path.isfile(portfolio_setup_file_path):
            raise FileNotFoundError(f"File not found: {portfolio_setup_file_path}")

        try:
            ext = os.path.splitext(portfolio_setup_file_path)[-1].lower()
            if ext in [".xlsx", ".xls"]:
                portfolio_config = pd.read_excel(portfolio_setup_file_path)
            elif ext == ".csv":
                portfolio_config = pd.read_csv(portfolio_setup_file_path)
            else:
                raise ValueError(f"Unsupported file format: {ext}")
        except Exception as e:
            raise ValueError(f"Failed to load the configuration file: {e}")

        self._validate_portfolio_config(portfolio_config)
        return portfolio_config

    def _validate_portfolio_config(self, portfolio_config: pd.DataFrame) -> None:
        """
        Validate the portfolio configuration to ensure all weights sum to 1.
        :param portfolio_config: DataFrame containing the portfolio configuration.
        """
        if "Assets" not in portfolio_config.columns:
            raise ValueError("Configuration file must contain an 'Assets' column.")

        for column in portfolio_config.columns:
            if column != "Assets" and portfolio_config[column].notna().any():
                total_value: float = portfolio_config[column].sum()
                if not abs(total_value - 1) < 1e-6:
                    raise ValueError(
                        f"The total value for '{column}' does not sum up to 1. "
                        f"Found: {total_value}"
                    )

    def _build_portfolio_dict(self) -> Dict[str, Dict[Any, float]]:
        """
        Build a dictionary of portfolios from the configuration DataFrame.
        :return: A dictionary where keys are portfolio names,
        and values are asset-weight pairs.
        """
        portfolio_dict: Dict[str, Dict[Any, float]] = {
            column: {
                asset: value
                for asset, value in zip(
                    self.portfolio_config["Assets"], self.portfolio_config[column]
                )
                if pd.notna(value)
            }
            for column in self.portfolio_config.columns
            if column != "Assets" and self.portfolio_config[column].notna().any()
        }
        if not portfolio_dict:
            raise ValueError("No valid portfolios found in the configuration file.")
        return portfolio_dict

    def select_portfolio(
        self, target_portfolio: str
    ) -> tuple[dict[Any, float], list[Any]]:
        """
        Select the target portfolio for backtesting.
        :param target_portfolio: Name of the target portfolio.
        :return: List of assets in the selected portfolio.
        """
        portfolio_dict = self._build_portfolio_dict()
        if target_portfolio not in portfolio_dict:
            raise ValueError(
                f"Portfolio '{target_portfolio}' not found in configuration."
            )
        self.portfolio: Dict[Any, float] = portfolio_dict[target_portfolio]
        return self.portfolio, list(self.portfolio.keys())

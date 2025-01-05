import numpy as np
import pandas as pd


class BacktestRunner:
    def __init__(self, core_data, portfolio, total_investment):
        """
        Initialize the backtest runner with the necessary data.

        :param core_data: The core financial data.
        :param portfolio: A dictionary representing the asset allocation.
        :param total_investment: Total amount to invest in the portfolio.
        """
        self.core_data = core_data
        self.portfolio = portfolio
        self.total_investment = total_investment

        # Benchmark data is assumed to be the last column in core_data
        self.benchmark_data = self.core_data.iloc[:, -1]

    def _initialize_allocations(self):
        """
        Initialize the asset allocations based on the total investment.
        """
        allocations = {
            asset: self.total_investment * weight
            for asset, weight in self.portfolio.items()
        }
        asset_shares = {
            asset: allocations[asset] / self.core_data[asset].iloc[0]
            for asset in self.portfolio.keys()
        }
        return allocations, asset_shares

    def _calculate_daily_values(self, asset_shares, date):
        """
        Calculate the daily value and daily dividends for each asset.
        """
        daily_value = {
            asset: shares * self.core_data.loc[date, asset]
            for asset, shares in asset_shares.items()
        }
        daily_dividends = {
            asset: shares * self.core_data.loc[date, f"{asset}_dividends_per_share"]
            for asset, shares in asset_shares.items()
        }
        return daily_value, daily_dividends

    def _reinvest_dividends(self, asset_shares, daily_dividends, date):
        """
        Reinvest dividends if the flag is set to True.
        """
        for asset in self.portfolio.keys():
            if daily_dividends[asset] > 0:
                asset_shares[asset] += (
                    daily_dividends[asset] / self.core_data.loc[date, asset]
                )

    def _rebalance_portfolio(
        self, asset_shares, allocations, date, last_rebalance_date
    ):
        """
        Rebalance the portfolio if the date is a new year.
        """
        if date.year != last_rebalance_date.year:
            total_portfolio_value = sum(
                shares * self.core_data.loc[date, asset]
                for asset, shares in asset_shares.items()
            )
            for asset in self.portfolio.keys():
                allocations[asset] = total_portfolio_value * self.portfolio[asset]
                asset_shares[asset] = (
                    allocations[asset] / self.core_data.loc[date, asset]
                )
            last_rebalance_date = date
        return allocations, asset_shares, last_rebalance_date

    def _update_results(self, results, date, daily_value, daily_dividends):
        """
        Update the results DataFrame with the daily values and dividends.
        """
        for asset in self.portfolio.keys():
            results.loc[date, f"{asset}_value"] = daily_value[asset]
            results.loc[date, f"{asset}_dividends"] = daily_dividends[asset]

    def _calculate_net_profit(self, results):
        """
        Calculate the net profit of the portfolio.
        """
        results["portfolio_value"] = results[
            [f"{asset}_value" for asset in self.portfolio.keys()]
        ].sum(axis=1)
        results["dividend_value"] = results[
            [f"{asset}_dividends" for asset in self.portfolio.keys()]
        ].sum(axis=1)
        results["net_profit"] = (
            results["portfolio_value"]
            + results["dividend_value"]
            - self.total_investment
        )

    def _calculate_benchmark_value(self, results):
        """
        Calculate the benchmark value based on the benchmark data.
        """
        benchmark_initial_value = self.benchmark_data.iloc[0]
        benchmark_investment = self.total_investment / benchmark_initial_value
        benchmark_values = self.benchmark_data * benchmark_investment
        results["benchmark_value"] = benchmark_values

    def _calculate_statistics(self, data, risk_free_rate=0.03):
        """
        Helper function to calculate various performance metrics
        for a given data series.

        :param data: The price data of the portfolio or benchmark.
        :param risk_free_rate: The annual risk-free rate (default: 3%).
        :return: A dictionary of calculated performance metrics.
        """
        annual_risk_free_rate = risk_free_rate
        daily_risk_free_rate = annual_risk_free_rate / 252
        returns = data.pct_change().dropna()

        start_balance = data.iloc[0]
        end_balance = data.iloc[-1]

        # Annualized return (CAGR)
        num_years = (data.index[-1] - data.index[0]).days / 365.25
        annualized_return = ((end_balance / start_balance) ** (1 / num_years) - 1) * 100

        # Standard deviation (Annualized)
        std_dev = returns.std() * np.sqrt(252) * 100

        # Best and Worst Year
        best_year = data.resample("Y").apply(lambda x: x.pct_change().sum()).max() * 100
        worst_year = (
            data.resample("Y").apply(lambda x: x.pct_change().sum()).min() * 100
        )

        # Maximum Drawdown
        max_drawdown = ((data / data.cummax()).min() - 1) * 100

        # Sharpe Ratio
        sharpe_ratio = (annualized_return - annual_risk_free_rate) / std_dev

        # Sortino Ratio (downside risk)
        downside_risk = (
            np.sqrt(np.mean(np.square(np.maximum(daily_risk_free_rate - returns, 0))))
            * np.sqrt(252)
            * 100
        )
        sortino_ratio = (annualized_return - annual_risk_free_rate) / downside_risk

        # Correlation with Benchmark
        benchmark_correlation = data.corr(self.benchmark_data)

        return {
            "Start Balance": f"${start_balance:,.2f}",
            "End Balance": f"${end_balance:,.2f}",
            "Annualized Return (CAGR)": f"{annualized_return:.2f}%",
            "Standard Deviation": f"{std_dev:.2f}%",
            "Best Year": f"{best_year:.2f}%",
            "Worst Year": f"{worst_year:.2f}%",
            "Maximum Drawdown": f"{max_drawdown:.2f}%",
            "Sharpe Ratio": f"{sharpe_ratio:.2f}",
            "Sortino Ratio": f"{sortino_ratio:.2f}",
            "Benchmark Correlation": f"{benchmark_correlation:.2f}",
        }

    def _performance_summary(self, results: pd.DataFrame):
        """
        Generate a performance summary table comparing the portfolio
        with the benchmark.

        :param results: A DataFrame containing the backtest results.
        :return: A DataFrame summarizing the performance of the portfolio and benchmark.
        """
        # Handle missing benchmark data
        if "benchmark_value" not in results.columns:
            raise ValueError(
                "Benchmark data ('benchmark_value') is missing from results."
            )

        # Calculate statistics for the portfolio and benchmark
        portfolio_stats = self._calculate_statistics(results["portfolio_value"])
        benchmark_stats = self._calculate_statistics(results["benchmark_value"])

        # Combine the statistics into a summary DataFrame
        summary_data = {
            "Metric": [
                "Start Balance",
                "End Balance",
                "Annualized Return (CAGR)",
                "Standard Deviation",
                "Best Year",
                "Worst Year",
                "Maximum Drawdown",
                "Sharpe Ratio",
                "Sortino Ratio",
                "Benchmark Correlation",
            ],
            "My Portfolio": [
                portfolio_stats["Start Balance"],
                portfolio_stats["End Balance"],
                portfolio_stats["Annualized Return (CAGR)"],
                portfolio_stats["Standard Deviation"],
                portfolio_stats["Best Year"],
                portfolio_stats["Worst Year"],
                portfolio_stats["Maximum Drawdown"],
                portfolio_stats["Sharpe Ratio"],
                portfolio_stats["Sortino Ratio"],
                portfolio_stats["Benchmark Correlation"],
            ],
            "Benchmark": [
                benchmark_stats["Start Balance"],
                benchmark_stats["End Balance"],
                benchmark_stats["Annualized Return (CAGR)"],
                benchmark_stats["Standard Deviation"],
                benchmark_stats["Best Year"],
                benchmark_stats["Worst Year"],
                benchmark_stats["Maximum Drawdown"],
                benchmark_stats["Sharpe Ratio"],
                benchmark_stats["Sortino Ratio"],
                benchmark_stats["Benchmark Correlation"],
            ],
        }

        summary_df = pd.DataFrame(summary_data)
        summary_df = summary_df.set_index("Metric")

        return summary_df

    def run_backtest(
        self, reinvest_dividends=False, annual_rebalance=False
    ) -> pd.DataFrame:
        """
        Run the backtest for the selected portfolio.

        :param reinvest_dividends: Whether to reinvest dividends.
        :param annual_rebalance: Whether to rebalance annually.
        :return: A DataFrame containing the backtest results.
        """
        if self.core_data is None or self.portfolio is None:
            raise ValueError(
                "Core data or portfolio is not initialized. Call 'fetch_data' first."
            )

        # Initialize allocations and asset shares
        allocations, asset_shares = self._initialize_allocations()

        results = pd.DataFrame(index=self.core_data.index)
        last_rebalance_date = self.core_data.index[0]

        for date in self.core_data.index:
            # Calculate daily values and dividends
            daily_value, daily_dividends = self._calculate_daily_values(
                asset_shares, date
            )

            # Update the results DataFrame
            self._update_results(results, date, daily_value, daily_dividends)

            # Reinvest dividends if necessary
            if reinvest_dividends:
                self._reinvest_dividends(asset_shares, daily_dividends, date)

            # Annual rebalancing
            if annual_rebalance:
                (
                    allocations,
                    asset_shares,
                    last_rebalance_date,
                ) = self._rebalance_portfolio(
                    asset_shares, allocations, date, last_rebalance_date
                )

        # Finalize the portfolio performance
        self._calculate_net_profit(results)

        # Benchmark calculations
        self._calculate_benchmark_value(results)

        # Annual summary
        annual_performance_summary = results.resample("Y").agg(
            {
                "portfolio_value": ["first", "last"],
                "dividend_value": "sum",
                "net_profit": "last",
            }
        )
        annual_performance_summary.columns = [
            "Start Value",
            "End Value",
            "Total Dividends",
            "Accumulated Net Profit",
        ]
        annual_performance_summary["Net Profit (Year)"] = (
            annual_performance_summary["End Value"]
            - annual_performance_summary["Start Value"]
        )
        annual_performance_summary["Return (%)"] = (
            annual_performance_summary["Net Profit (Year)"]
            / annual_performance_summary["Start Value"]
        ) * 100
        annual_performance_summary.index = annual_performance_summary.index.strftime(
            "%Y"
        )

        # Stock details
        asset_performance_details_list = []
        for asset in self.portfolio.keys():
            stock_yearly = (
                results[[f"{asset}_value", f"{asset}_dividends"]]
                .resample("Y")
                .agg({f"{asset}_value": ["first", "last"], f"{asset}_dividends": "sum"})
            )
            stock_yearly.columns = ["Start Value", "End Value", "Total Dividends"]
            stock_yearly["Return (%)"] = (
                (stock_yearly["End Value"] - stock_yearly["Start Value"])
                / stock_yearly["Start Value"]
            ) * 100
            stock_yearly["Asset"] = asset
            asset_performance_details_list.append(stock_yearly)

        asset_performance_details = pd.concat(
            asset_performance_details_list, keys=self.portfolio.keys()
        ).reset_index()
        asset_performance_details["Date"] = asset_performance_details["Date"].dt.year
        asset_performance_details.rename(columns={"Date": "Year"}, inplace=True)
        asset_performance_details = asset_performance_details.drop(columns="level_0")
        performance_summary = self._performance_summary(results)
        raw_results = results.copy()

        return (
            performance_summary,
            annual_performance_summary,
            asset_performance_details,
            raw_results,
        )

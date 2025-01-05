import pandas as pd
import plotly.express as px
import plotly.graph_objects as go


class BacktestVisualizer:
    def __init__(
        self,
        raw_results: pd.DataFrame,
        asset_performance_details: pd.DataFrame,
        output_path: str,
    ):
        """
        Initialize the BacktestVisualizer class
        with raw results and asset performance details.
        :param raw_results: A DataFrame containing the backtest results.
        :param asset_performance_details:
            A DataFrame containing the annual returns of each stock.
        """
        self.raw_results = raw_results
        self.asset_performance_details = asset_performance_details
        self.output_path = output_path

    def plot_results(self):
        """
        Plot portfolio value, benchmark, net profit,
        and annual returns for each asset using Plotly.
        """
        self.plot_portfolio_vs_benchmark()
        self.plot_net_profit()
        self.plot_annual_returns()

    def plot_portfolio_vs_benchmark(self):
        """
        Plot portfolio value against the benchmark over time.
        """
        fig = go.Figure()

        # Portfolio Value and Benchmark Value
        fig.add_trace(
            go.Scatter(
                x=self.raw_results.index,
                y=self.raw_results["portfolio_value"],
                mode="lines",
                name="Portfolio Value",
                line=dict(color="blue", width=2),
            )
        )

        fig.add_trace(
            go.Scatter(
                x=self.raw_results.index,
                y=self.raw_results["benchmark_value"],
                mode="lines",
                name="Benchmark",
                line=dict(color="orange", width=2),
            )
        )

        fig.update_layout(
            title="Portfolio Value and Benchmark Over Time",
            xaxis_title="Date",
            yaxis_title="Value",
            showlegend=True,
        )
        # fig.show()
        fig.write_html(
            f"{self.output_path}/Portfolio Value and Benchmark Over Time.html"
        )

    def plot_net_profit(self):
        """
        Plot net profit over time.
        """
        fig = go.Figure()
        fig.add_trace(
            go.Scatter(
                x=self.raw_results.index,
                y=self.raw_results["net_profit"],
                mode="lines",
                name="Net Profit",
                line=dict(color="red", width=2),
            )
        )

        fig.update_layout(
            title="Net Profit Over Time",
            xaxis_title="Date",
            yaxis_title="Net Profit",
            showlegend=True,
        )
        # fig.show()
        fig.write_html(f"{self.output_path}/Net Profit Over Time.html")

    def plot_annual_returns(self):
        """
        Plot the annual returns for each asset.
        """
        fig = go.Figure()

        for idx, asset in enumerate(self.asset_performance_details["Asset"].unique()):
            stock_results = self.asset_performance_details[
                self.asset_performance_details["Asset"] == asset
            ]

            fig.add_trace(
                go.Bar(
                    x=stock_results["Year"] + 0.1 * idx,
                    y=stock_results["Return (%)"],
                    name=f"{asset}",
                    text=[f"{height:.2f}%" for height in stock_results["Return (%)"]],
                    textposition="outside",
                    width=0.1,
                    marker=dict(color=px.colors.qualitative.Set2[idx % 10]),
                )
            )

        fig.update_layout(
            title="Annual Returns of Each Stock",
            xaxis_title="Year",
            yaxis_title="Return (%)",
            xaxis=dict(tickmode="linear"),
            showlegend=True,
        )
        # fig.show()
        fig.write_html(f"{self.output_path}/Annual Returns of Each Stock.html")

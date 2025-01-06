import argparse
import json
import warnings
from pathlib import Path

import pandas as pd

from retroflux import (
    BacktestRunner,
    BacktestVisualizer,
    PortfolioConfigLoader,
    PortfolioDataFetcher,
)

warnings.filterwarnings("ignore", category=FutureWarning)


def main():
    parser = argparse.ArgumentParser(description="Run portfolio backtest.")
    parser.add_argument(
        "--config_file", type=str, required=True, help="Path to the configuration file"
    )

    args = parser.parse_args()

    print("[INFO] Loading configuration file...")
    with open(args.config_file, "r") as f:
        config = json.load(f)
    print("[INFO] Configuration file loaded successfully.")

    print("[INFO] Initializing portfolio configuration...")
    config_loader = PortfolioConfigLoader(
        portfolio_setup_file_path=config["portfolio_setup_file_path"],
        total_investment=config["total_investment"],
    )
    portfolio, assets = config_loader.select_portfolio(config["target_portfolio"])
    print(
        f"[INFO] Portfolio '{config['target_portfolio']}' "
        "selected with {len(assets)} assets."
    )

    print("[INFO] Fetching core data for assets and benchmark...")
    data_fetcher = PortfolioDataFetcher(
        assets=assets, benchmark_ticker=config["benchmark"]
    )
    core_data = data_fetcher.fetch_core_data(
        start_date=config["start_date"], end_date=config["end_date"]
    )
    print("[INFO] Core data fetched successfully.")

    print("[INFO] Running backtest...")
    backtester = BacktestRunner(
        core_data=core_data,
        portfolio=portfolio,
        total_investment=config["total_investment"],
    )
    (
        performance_summary,
        annual_performance_summary,
        asset_performance_details,
        raw_results,
    ) = backtester.run_backtest(
        reinvest_dividends=config["reinvest_dividends"],
        annual_rebalance=config["annual_rebalance"],
    )
    print("[INFO] Backtest completed successfully.")

    output_path = Path(config["output_path"])
    print(f"[INFO] Saving results to {output_path}/backtest_results.xlsx...")
    with pd.ExcelWriter(output_path / "backtest_results.xlsx") as writer:
        performance_summary.to_excel(writer, sheet_name="Performance Summary")
        annual_performance_summary.to_excel(
            writer, sheet_name="Annual Performance Summary"
        )
        asset_performance_details.to_excel(
            writer, sheet_name="Asset Performance Details", index=False
        )
    print(f"[INFO] Results saved successfully to {output_path}/backtest_results.xlsx.")

    print("[INFO] Generating visualizations...")
    visualizer = BacktestVisualizer(raw_results, asset_performance_details, output_path)
    visualizer.plot_results()
    print(f"[INFO] Visualizations saved to {output_path}.")

    print(
        "[INFO] Backtest process completed. All results and visualizations are ready."
    )


if __name__ == "__main__":
    main()

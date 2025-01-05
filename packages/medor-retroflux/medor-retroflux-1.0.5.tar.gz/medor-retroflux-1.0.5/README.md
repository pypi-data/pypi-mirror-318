**Retroflux** is a sophisticated and flexible tool designed to backtest your investment portfolio with precision and ease. With this tool, you can evaluate how your portfolio would have performed historically, benchmark its performance against market indices like the S&P 500, and uncover actionable insights to refine your investment strategy.

## Key Features

**1. Backtest Historical Performance**

Analyze your portfolio's historical performance over a defined time period and compare it against a benchmark (default: S&P 500).

**2. Customizable Options**

- **Dividend Reinvestment**: Choose to reinvest dividends or withdraw them as cash flow.

- **Portfolio Rebalancing**: Simulate portfolio rebalancing at specific intervals (currently supports annual rebalancing).

**3. Detailed Analytics**

Gain access to comprehensive performance metrics, including:

- Cumulative returns

- Annualized returns

- Volatility

- Sharpe ratio

- Drawdowns

**4. Multi-Asset Support**

Backtest portfolios comprising stocks, ETFs, bonds, and other financial instruments.

**5. Visualization Tools**

Generate intuitive graphs and charts to analyze performance trends and identify opportunities.

## **Installation**

1. Install Retroflux directly from PyPI:

   ```bash
   pip install retroflux
   ```

2. Optionally, you can install Retroflux in a virtual environment (recommended):

   ```bash
   python -m venv your_venv
   source your_venv/bin/activate  # For macOS/Linux
   your_venv\Scripts\activate  # For Windows
   pip install retroflux
   ```

## **Configuration File**

Before running the backtest, you need to provide a JSON configuration file with the necessary parameters. Below is an example configuration file:

```json
{
  "portfolio_setup_file_path": "/your_path/portfolio_setup_file.xlsx",
  "total_investment": 100000,
  "target_portfolio": "Portfolio #1",
  "benchmark": "SPY",
  "start_date": "2020-01-01",
  "end_date": "2024-12-31",
  "reinvest_dividends": true,
  "annual_rebalance": true,
  "output_path": "/your_path/outputs"
}
```

## **Configuration Explanation**

- **portfolio_setup_file_path**: Path to the Excel file containing portfolio setup. This file should include information about the portfolio.
- **total_investment**: The total investment amount, e.g., 100000.
- **target_portfolio**: The name of the target portfolio for backtesting, e.g., "Portfolio #1".
- **benchmark**: The benchmark index ticker (e.g., "SPY" for the S&P 500 ETF).
- **start_date**: The start date for the backtest, in YYYY-MM-DD format.
- **end_date**: The end date for the backtest, in YYYY-MM-DD format.
- **reinvest_dividends**: Whether to reinvest dividends, set to true or false.
- **annual_rebalance**: Whether to perform annual rebalancing of the portfolio, set to true or false.
- **output_path**: Path to save the backtest results. The results will be saved here.

## **Portfolio Setup File Example**

The portfolio setup file should be an Excel file containing asset allocations for different portfolios. Below is an example of how the file should be structured:

| Assets | Portfolio #1 | Portfolio #2 | Portfolio #3 |
|--------|--------------|--------------|--------------|
| AAPL   | 0.3          | 0.4          |              |
| MSFT   | 0.3          |              | 0.5          |
| GOOGL  | 0.2          |              | 0.3          |
| AMZN   | 0.2          | 0.6          |              |
| TSLA   |              |              | 0.2          |

- **Assets**:  This column is required and should list the assets included in your portfolio (e.g., AAPL, MSFT, etc.).
- **Portfolio #1, Portfolio #2, etc.**: These are the names of the portfolios the user creates. You can add multiple portfolios, and the allocations for each asset will be defined by the values under each portfolio column.
- **Value under each portfolio**: This represents the proportion of the total investment allocated to each asset in that particular portfolio. The sum of all allocations in each portfolio should equal 1 (or 100%).

You can reference the portfolios in the configuration file by specifying the portfolio name under `target_portfolio`.

## **Usage**

### **Running the Backtest**

Once Retroflux is installed, you can run the backtest by passing the path to your configuration file:

```bash
run-backtest --config_file "/path/to/your/config.json"
```

This command will initiate the backtest process using the configuration from the specified JSON file.

### **Result Output**

- The backtest results will be saved as an Excel file with the following sheets:
  - **Performance Summary**: Summary of the portfolio's performance.
  - **Annual Performance Summary**: Annual performance summary of the portfolio.
  - **Asset Performance Details**: Detailed performance for each asset.
  
- Interactive Plotly charts will also be generated and saved in the output path specified in your configuration file.

## **Notes**

- Ensure that the paths in the configuration file are correctly set.
- Make sure the necessary dependencies are installed (they are included in the requirements.txt or automatically installed with `pip install retroflux`).
- The output folder must have write permissions to save results and charts.

## **Product Roadmap**

**Upcoming Enhancements:**

- **Cash Flow Simulations**: Add or withdraw funds at regular intervals based on user-defined schedules.

- **Granular Timeframe Analysis**: Extend analytics to include month-over-month and week-over-week performance comparisons.

- **Dynamic Allocation Adjustments**: Test and compare multiple asset allocation strategies.

- **AI-Driven Insights**: Integrate AI models to analyze results and provide actionable recommendations.

- **Automated Report Generation**: Export performance summaries and insights as professionally designed PDFs.

- **Advanced Visualization**: Introduce more detailed charts for drawdown analysis, risk assessment, and monthly breakdowns.

## Contributing

Contributions are welcome! If you have ideas for new features, find a bug, or want to improve the documentation, feel free to open an issue or submit a pull request.

1. Fork the repository.
2. Create your feature branch: git checkout -b feature/YourFeature.
3. Commit your changes: git commit -m 'Add your feature'.
4. Push to the branch: git push origin feature/YourFeature.
5. Open a pull request.

## License

This project is licensed under the GNU Affero General Public License v3 (AGPLv3).

By using this software, you agree to comply with the terms of the AGPLv3, ensuring that any derivative work or modification that interacts with users over a network must also be distributed under the same license. For full details, please refer to the LICENSE file.

If you have any questions or feedback, feel free to open an issue or contact me at miao.vince.bi@medor.ca.

## Acknowledgment

This project is inspired by Portfolio Visualizer (https://www.portfoliovisualizer.com/), a platform owned and operated by SRL Global Ltd.

## Disclaimer

Retroflux is a tool designed for educational and informational purposes only.
- **Investment Risk:** All investments involve risk, including the potential loss of principal.
- **No Investment Advice:** This tool does not constitute financial, investment, or legal advice. Users should conduct their own due diligence and consult with a qualified professional before making investment decisions.
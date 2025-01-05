from setuptools import find_packages, setup

setup(
    name="medor-retroflux",
    version="1.0.2",
    packages=find_packages(),
    install_requires=[
        "pandas",
        "matplotlib",
        "pyyaml",
        "numpy",
        "plotly",
        "yfinance",
        "fpdf",
        "kaleido",
        "openpyxl",
        "nbformat",
    ],
    entry_points={
        "console_scripts": [
            "run-backtest=main:main",
        ],
    },
    author="Vince BI Miao",
    description="A backtesting tool for financial strategies",
    long_description=open("README.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Medor-Inc/Retroflux.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.7",
)

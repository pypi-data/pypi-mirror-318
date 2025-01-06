from setuptools import setup

setup(
    name="medor-retroflux",
    version="1.1.0",
    packages=["retroflux"],
    install_requires=[
        "pandas",
        "matplotlib",
        "pyyaml",
        "numpy",
        "plotly",
        "yfinance",
        "kaleido",
        "openpyxl",
        "nbformat",
    ],
    entry_points={
        "console_scripts": [
            "run-backtest=retroflux.main:main",
        ],
    },
    author="Vince BI Miao",
    author_email="miao.vince.bi@medor.ca",
    description="A backtesting tool for financial strategies",
    long_description=open("README_without_images.md").read(),
    long_description_content_type="text/markdown",
    url="https://github.com/Medor-Inc/Retroflux.git",
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: GNU Affero General Public License v3",
        "Operating System :: OS Independent",
    ],
    python_requires=">=3.8",
)

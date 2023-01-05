# Financial Indexes Correlation
Analyze financial data correlations

## Features

- You can run it fast, and it is easy to use.
- There are no complexities and no database usage in this project. Even dependencies are a few.
- It is easy to modify and customize.
- This project generates practical information for data scientists.
- You can read the code for educational purposes.

## Run

1. Clone the repository.
2. Run `pip3 install -r requirements.txt`.
3. Put your [Nasdaq Data Link](https://data.nasdaq.com/) API key in the `API_KEY` file.
4. Run `python3 main.py`.

This will print the 

## Config

For the configuration, you can:

- Change `config.py` constants.
- Define new indicators in `indicators.py`.

## Config.py Description

- `QUOTES_LIST_WITH_SOURCE`: What are your considered financial indexes?
- `START_TIME` and `END_TIME`: The time interval for the financial indexes candles
- `CSV_DELIMITER`: The delimiter in every generated CSV file
- `API_KEY_FILE_PATH`: Path to the Nasdaq Data Link API key file

## See Also

- [Binance Futures Trading Bot](https://github.com/erfaniaa/binance-futures-trading-bot)
- [Binance Spot Trading Bot](https://github.com/smzerehpoush/binance-spot-trading-bot)
- [Crypto Trading Strategy Backtester](https://github.com/Erfaniaa/crypto-trading-strategy-backtester)
- [Financial Dataset Generator](https://github.com/Erfaniaa/financial-dataset-generator)

## Credits

[Erfan Alimohammadi](https://github.com/Erfaniaa) and [Amir Reza Shahmiri](https://github.com/Amirrezashahmiri)

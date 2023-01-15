# Financial Indexes Correlation
Analyze financial data correlations

## About Correlation

- In statistics, correlation or dependence is any statistical relationship, whether causal or not, between two random variables or bivariate data. Although in the broadest sense, "correlation" may indicate any type of association, in statistics it usually refers to the degree to which a pair of variables are linearly related. Familiar examples of dependent phenomena include the correlation between the height of parents and their offspring, and the correlation between the price of a good and the quantity the consumers are willing to purchase, as it is depicted in the so-called demand curve.

- Correlations are useful because they can indicate a predictive relationship that can be exploited in practice. For example, an electrical utility may produce less power on a mild day based on the correlation between electricity demand and weather. In this example, there is a causal relationship, because extreme weather causes people to use more electricity for heating or cooling. However, in general, the presence of a correlation is not sufficient to infer the presence of a causal relationship (i.e., correlation does not imply causation).

Source: [Wikipedia](https://en.wikipedia.org/wiki/Correlation)

## Features

- You can run it fast, and it is easy to use.
- There are no complexities and no database usage in this project. Even dependencies are a few.
- It is easy to modify and customize.
- This project generates practical information for data scientists.
- You can read the code for educational purposes.

## Sample Correlation Matrix Output

![image](https://user-images.githubusercontent.com/7780269/212567969-1e309001-6683-4ed2-bc0c-4bb2d2f95587.png)


## Run

1. Clone the repository.
2. Run `pip3 install -r requirements.txt`.
3. Put your [Nasdaq Data Link](https://data.nasdaq.com/) API key in the `API_KEY` file.
4. Run `python3 main.py`.

This will print the correlation matrix and save it to a CSV file.

## Config

For the configuration, you can change `config.py` constants.

## Config.py Description

- `QUOTES_LIST_WITH_SOURCE`: What are your considered financial indexes?
- `START_TIME` and `END_TIME`: The time interval for the financial indexes candles
- `CSV_DELIMITER`: The delimiter character in the generated CSV file
- `API_KEY_FILE_PATH`: Path to the Nasdaq Data Link API key file

## See Also

- [Binance Futures Trading Bot](https://github.com/erfaniaa/binance-futures-trading-bot)
- [Binance Spot Trading Bot](https://github.com/smzerehpoush/binance-spot-trading-bot)
- [Crypto Trading Strategy Backtester](https://github.com/Erfaniaa/crypto-trading-strategy-backtester)
- [Financial Dataset Generator](https://github.com/Erfaniaa/financial-dataset-generator)

## Credits

[Erfan Alimohammadi](https://github.com/Erfaniaa) and [Amir Reza Shahmiri](https://github.com/Amirrezashahmiri)

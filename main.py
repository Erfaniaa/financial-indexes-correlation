import config

from requests_html import HTMLSession
import yfinance
import pandas as pd

import datetime


def date_string_to_datetime(date_string):
	return datetime.datetime.strptime(date_string, "%Y-%m-%d")


def get_next_day_string(current_day_string):
	current_day_datetime = date_string_to_datetime(current_day_string)
	next_day_datetime = current_day_datetime + datetime.timedelta(days=1)
	next_day_string = next_day_datetime.strftime("%Y-%m-%d")
	return next_day_string


def date_range(start_datetime, end_datetime):
    for i in range(int((end_datetime - start_datetime).days) + 1):
        yield start_datetime + datetime.timedelta(i)


def get_data_for_quote(quote, start_time, end_time):
	df = yfinance.download(quote, start=get_next_day_string(start_time), end=get_next_day_string(end_time), interval="1d", auto_adjust=True, prepost=True, threads=True)
	df = df.reset_index()
	df = df.dropna()
	df = df.loc[~df.apply(lambda row: (row == 0).any(), axis=1)]
	if df.shape[0] == 0:
		return df
	return df


def get_total_start_and_end_time(moving_average_size):
	start_time = datetime.datetime.utcnow() + datetime.timedelta(days=-moving_average_size)
	end_time = datetime.datetime.utcnow() + datetime.timedelta(days=-1)
	return start_time.strftime("%Y-%m-%d"), end_time.strftime("%Y-%m-%d")


def get_total_crypto_quotes_list(maximum_cryptos_to_consider):
	html_session = HTMLSession()
	yfinance_response = html_session.get(f"https://finance.yahoo.com/crypto?offset=0&count={maximum_cryptos_to_consider}")
	df = pd.read_html(yfinance_response.html.raw_html)               
	df = df[0].copy()
	total_crypto_quotes_list = df.Symbol.tolist()
	return total_crypto_quotes_list


def get_values_series_from_dataframe(df, quote_name):
	return df["Close"].rename(quote_name[:-4])


def get_values_for_quotes_list(quote_names_list, start_time, end_time):
	all_quotes_values_list = []
	for quote_name in quote_names_list:
		print("Quote:", quote_name)
		df = get_data_for_quote(quote_name, start_time, end_time)
		print("Data downloaded.")
		values_series = get_values_series_from_dataframe(df, quote_name)
		print("_" * 80)
		if values_series.shape[0] != 0:
			all_quotes_values_list.append(values_series)
	return all_quotes_values_list


def generate_matrix_from_all_quotes_values(all_quotes_values_list, quotes_list):
	df = pd.DataFrame(all_quotes_values_list)
	df = df.T
	columns_rename_dict = {}
	for i in range(len(quotes_list)):
		columns_rename_dict[i] = quotes_list[i][0].split('/')[-1]
	df = df.rename(columns=columns_rename_dict)
	df = df.corr()
	return df


def concat_datasets(dataset1, dataset2):
	ret = []
	for row in dataset1:
		ret.append(row)
	for row in dataset2:
		ret.append(row)
	return ret


def generate_correlation_matrix(quotes_list, start_time, end_time, output_csv_file_path, output_csv_file_delimiter):
	all_quotes_values_list = get_values_for_quotes_list(quotes_list, start_time, end_time)
	df = generate_matrix_from_all_quotes_values(all_quotes_values_list, quotes_list)
	df.to_csv(output_csv_file_path, sep=output_csv_file_delimiter)


def run(look_back_days, maximum_cryptos_to_consider, output_csv_file_path, output_csv_file_delimiter):
	start_time, end_time = get_total_start_and_end_time(look_back_days)
	crypto_quotes_list = get_total_crypto_quotes_list(maximum_cryptos_to_consider)
	generate_correlation_matrix(crypto_quotes_list, start_time, end_time, output_csv_file_path, output_csv_file_delimiter)


def main():
	run(config.LOOK_BACK_DAYS,
		config.MAXIMUM_CRYPTOS_TO_CONSIDER,
		config.OUTPUT_CSV_FILE_PATH,
		config.OUTPUT_CSV_FILE_DELIMITER)


if __name__ == "__main__":
	main()

import os
import pandas as pd
from load_time_series import download_time_series


data_folder = 'time_series_data'
data_file = os.path.join(data_folder, 'time_series.csv')
url = r'https://data.open-power-system-data.org/time_series/2020-10-06/time_series_60min_singleindex.csv'

def main():
    if not os.path.exists(data_folder):
        os.makedirs(data_folder)
    if not os.path.isfile(data_file):
        print(f"{data_file} is not exist. Downloading data...")
    else:
        print(f'{data_file} is exist. Ready to data analise.')
    df = pd.read_csv(data_file, parse_dates=['utc_timestamp'])
    column_of_interest = [
        'utc_timestamp',
        'DE_load_actual_entsoe_transparency',
        'DE_wind_onshore_generation_actual',
        'DE_solar_generation_actual'
    ]
    df = df[column_of_interest]
    print(df.head())
    print(len(df))


if __name__ == '__main__':
    main()
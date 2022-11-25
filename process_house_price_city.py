from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/house_price')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)


city_lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
city_lut = city_lut[['CityName','CityCode','LTLAName','LTLACode']]

mean_price = pd.read_csv('./house_price/city_mean_all_sales_all_house_types.csv')
median_price = pd.read_csv('./house_price/city_median_all_sales_all_house_types.csv')

mean_price = city_lut.merge(mean_price,left_on='LTLACode', right_on='LTLACode',how='left')
median_price = city_lut.merge(median_price,left_on='LTLACode', right_on='LTLACode',how='left')


city_name_list = []
city_code_list = []
LTLA_name_list = []
LTLA_code_list = []
time_list = []
type_list = []
price_list = []
for _, row in mean_price.iterrows():
    for i in range(len(row.index) - 4):
        city_name_list.append(row['CityName'])
        city_code_list.append(row['CityCode'])
        LTLA_name_list.append(row['LTLAName'])
        LTLA_code_list.append(row['LTLACode'])
        type_list.append('Mean')

        time_list.append(row.index[i+4])
        price_list.append(row[row.index[i+4]])

for _, row in median_price.iterrows():
    for i in range(len(row.index) - 4):
        city_name_list.append(row['CityName'])
        city_code_list.append(row['CityCode'])
        LTLA_name_list.append(row['LTLAName'])
        LTLA_code_list.append(row['LTLACode'])
        type_list.append('Median')

        time_list.append(row.index[i+4])
        price_list.append(row[row.index[i+4]])

house_price = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'LTLAName':LTLA_name_list, 'LTLACode':LTLA_code_list, 'Time':time_list, 'Aggregation':type_list, 'Price':price_list})
house_price = house_price.sort_values(['CityCode','LTLACode'], ascending=True)
house_price.to_csv(OUTPUT_PATH.joinpath('house_price_city.csv'),index=False)

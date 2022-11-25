from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/basic_statistics/population')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

city_lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
city_lut = city_lut[['LTLAName','LTLACode','CityCode','CityName']]
city_lut = city_lut.drop_duplicates()

# 读取postcode - LTLA lookup table
msoa_lut = pd.read_csv('./city_defination_and_LUTs/pcd_oa_lsoa_msoa_ltla_utla_rgn_ctry_ew_may_2021_lu.csv',dtype=str)
msoa_lut = msoa_lut[['msoa21cd','ltla22cd']].drop_duplicates()


city_msoa_lut = city_lut.merge(msoa_lut, left_on='LTLACode', right_on='ltla22cd',how='left')[['CityCode','CityName','LTLACode','msoa21cd']]

pop_data = pd.read_csv('./msoa_pop/msoa_pop.csv')

pop_data = city_msoa_lut.merge(pop_data ,left_on='msoa21cd', right_on='MSOACode',how='left')[['CityName','CityCode','Population']]
pop_data = pop_data.groupby(['CityName','CityCode']).sum().reset_index()


area_data = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')[['CityCode', 'Area']]
pop_data = pop_data.merge(area_data, left_on='CityCode', right_on='CityCode')
pop_data['PopulationDensity'] = pop_data['Population'] / pop_data['Area']
pop_data = pop_data.drop('Area', axis=1)
pop_data = pop_data.sort_values(['CityCode'], ascending=True)


pop_data.to_csv(OUTPUT_PATH.joinpath('population_city.csv'),index=False)

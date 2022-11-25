from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/basic_statistics/area')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

city_lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
city_lut = city_lut[['CityName','CityCode']]
city_lut = city_lut.drop_duplicates()

msoa_lut = pd.read_csv('./city_defination_and_LUTs/Middle_Layer_Super_Output_Area_(2011)_to_Major_Towns_and_Cities_(December_2015)_Lookup_in_England_and_Wales.csv')[['MSOA11CD','MSOA11NM','TCITY15CD']]
msoa_lut = msoa_lut.rename(columns={'MSOA11NM':'MSOAName','MSOA11CD':'MSOACode'})
msoa_in_city = city_lut.merge(msoa_lut, left_on='CityCode', right_on='TCITY15CD', how='left').drop(['TCITY15CD'],axis=1)

msoa_area = pd.read_csv('./city_defination_and_LUTs/Middle_Layer_Super_Output_Areas_(December_2011)_Boundaries_Generalised_Clipped_(BGC)_EW_V3.csv')[['MSOA11CD','Shape__Area']]
area = msoa_in_city.merge(msoa_area, left_on = 'MSOACode', right_on = 'MSOA11CD',how='left')
area = area.rename(columns={'Shape__Area':'Area'})
area = area[['CityName','CityCode','MSOAName','MSOACode','Area']]
area['Area'] /= 1000000
area = area.sort_values(['CityCode','MSOACode'], ascending=True)
area.to_csv(OUTPUT_PATH.joinpath('area_msoa.csv'),index=False)

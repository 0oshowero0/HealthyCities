from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/basic_statistics/area')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

city_lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
city_lut = city_lut[['CityName','CityCode']]
city_lut = city_lut.drop_duplicates()

area = pd.read_csv('./city_defination_and_LUTs/Major_Towns_and_Cities_(December_2015)_Boundaries_V2.csv')[['TCITY15CD','Shape__Area']]
area = city_lut.merge(area, left_on = 'CityCode', right_on = 'TCITY15CD',how='left')
area['Area'] = area['Shape__Area']
area = area[['CityName','CityCode','Area']]
area['Area'] /= 1000000
area = area.sort_values(['CityCode'], ascending=True)

area.to_csv(OUTPUT_PATH.joinpath('area_city.csv'),index=False)

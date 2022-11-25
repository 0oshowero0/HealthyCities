import pandas as pd
import geopandas as gpd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/basic_statistics/centroid')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

boundary = gpd.read_file('./city_defination_and_LUTs/Major_Towns_and_Cities_(December_2015)_Boundaries_V2.geojson', driver='geojson')

city_lut = gpd.read_file('./city_defination_and_LUTs/city_look_up_table.csv')
city_lut = city_lut[['CityCode','CityName']]

boundary = boundary.merge(city_lut,right_on='CityCode',left_on='TCITY15CD',how='right')[['CityCode', 'CityName','geometry']]

boundary['centroid'] = boundary['geometry'].map(lambda x:x.centroid)
boundary = boundary.drop('geometry',axis=1)
boundary = boundary.rename(columns={'centroid':'geometry'})

boundary.to_file(OUTPUT_PATH.joinpath('geographical_centroid_city.geojson'), driver='GeoJSON')

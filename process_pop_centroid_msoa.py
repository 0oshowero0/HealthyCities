import pandas as pd
import geopandas as gpd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/basic_statistics/centroid')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

centroid = gpd.read_file('./city_defination_and_LUTs/Middle_Layer_Super_Output_Areas_(December_2011)_Population_Weighted_Centroids.geojson', driver='geojson')

msoa_lut = gpd.read_file('./city_defination_and_LUTs/msoa_look_up_table.csv')
msoa_lut = msoa_lut[['CityName','CityCode','MSOAName','MSOACode']]

centroid = centroid.merge(msoa_lut,right_on='MSOACode',left_on='msoa11cd',how='right')[['MSOACode', 'MSOAName','CityCode','CityName','geometry']]

centroid.to_file(OUTPUT_PATH.joinpath('population_weighted_centroid_msoa.geojson'), driver='GeoJSON')

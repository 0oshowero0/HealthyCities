import pandas as pd
import geopandas as gpd
from pathlib import Path

OUTPUT_PATH = Path('./output/environmental_determinants/basic_statistics/centroid')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

boundary = gpd.read_file('./city_defination_and_LUTs/Middle_Layer_Super_Output_Areas_(December_2011)_Boundaries_Generalised_Clipped_(BGC)_EW_V3.geojson', driver='geojson')

msoa_lut = gpd.read_file('./city_defination_and_LUTs/msoa_look_up_table.csv')
msoa_lut = msoa_lut[['CityName','CityCode','MSOAName','MSOACode']]

boundary = boundary.merge(msoa_lut,right_on='MSOACode',left_on='MSOA11CD',how='right')[['MSOACode', 'MSOAName','CityCode','CityName','geometry']]

boundary['centroid'] = boundary['geometry'].map(lambda x:x.centroid)
boundary = boundary.drop('geometry',axis=1)
boundary = boundary.rename(columns={'centroid':'geometry'})

boundary.to_file(OUTPUT_PATH.joinpath('geographical_centroid_msoa.geojson'), driver='GeoJSON')

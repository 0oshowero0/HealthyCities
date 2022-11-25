from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd

OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/road_density')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

area_lut = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')

###########################################
# Driving Net
input_files = sorted([i for i in Path('./temp_output/osm_filter/road_network/city_level').glob('*driving.geojson')])

area_list = []
road_length_list = []
road_density_list = []
city_code_list = []
city_name_list = []

for f in input_files:
    df = gpd.read_file(f, driver='GeoJSON')
    road_length = df['length'].dropna().sum() / 1000

    city_code = f.stem.split('_')[0]
    area_lut_for_city = area_lut.loc[area_lut.CityCode == city_code]

    area_list.append(area_lut_for_city['Area'].iloc[0])
    road_length_list.append(road_length)
    road_density_list.append(road_length/area_lut_for_city['Area'].iloc[0])
    city_code_list.append(city_code)
    city_name_list.append(area_lut_for_city['CityName'].iloc[0])

df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'RoadLength':road_length_list, 'Area':area_list, 'RoadDensity':road_density_list})
df.to_csv(OUTPUT_PATH.joinpath('driving_road_density_city.csv'),index=False)


###########################################
# cycling Net
input_files = sorted([i for i in Path('./temp_output/osm_filter/road_network/city_level').glob('*cycling.geojson')])

area_list = []
road_length_list = []
road_density_list = []
city_code_list = []
city_name_list = []

for f in input_files:
    df = gpd.read_file(f, driver='GeoJSON')
    road_length = df['length'].dropna().sum() / 1000

    city_code = f.stem.split('_')[0]
    area_lut_for_city = area_lut.loc[area_lut.CityCode == city_code]

    area_list.append(area_lut_for_city['Area'].iloc[0])
    road_length_list.append(road_length)
    road_density_list.append(road_length/area_lut_for_city['Area'].iloc[0])
    city_code_list.append(city_code)
    city_name_list.append(area_lut_for_city['CityName'].iloc[0])

df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'RoadLength':road_length_list, 'Area':area_list, 'RoadDensity':road_density_list})
df.to_csv(OUTPUT_PATH.joinpath('cycling_road_density_city.csv'),index=False)

###########################################
# walking Net
input_files = sorted([i for i in Path('./temp_output/osm_filter/road_network/city_level').glob('*walking.geojson')])

area_list = []
road_length_list = []
road_density_list = []
city_code_list = []
city_name_list = []

for f in input_files:
    df = gpd.read_file(f, driver='GeoJSON')
    road_length = df['length'].dropna().sum() / 1000

    city_code = f.stem.split('_')[0]
    area_lut_for_city = area_lut.loc[area_lut.CityCode == city_code]

    area_list.append(area_lut_for_city['Area'].iloc[0])
    road_length_list.append(road_length)
    road_density_list.append(road_length/area_lut_for_city['Area'].iloc[0])
    city_code_list.append(city_code)
    city_name_list.append(area_lut_for_city['CityName'].iloc[0])

df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'RoadLength':road_length_list, 'Area':area_list, 'RoadDensity':road_density_list})
df.to_csv(OUTPUT_PATH.joinpath('walking_road_density_city.csv'),index=False)
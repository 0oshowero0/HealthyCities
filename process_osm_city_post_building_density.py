from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd

OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/building_density')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

area_lut = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')

input_files = sorted([i for i in Path('./temp_output/osm_filter/building/city_level').glob('*.geojson')])

area_list = []
building_num_list = []
building_density_list = []
city_code_list = []
city_name_list = []

for f in input_files:
    df = gpd.read_file(f, driver='GeoJSON')
    building_num = df.shape[0]
    city_code = f.stem
    area_lut_for_city = area_lut.loc[area_lut.CityCode == city_code]

    area_list.append(area_lut_for_city['Area'].iloc[0])
    building_num_list.append(building_num)
    building_density_list.append(building_num/area_lut_for_city['Area'].iloc[0])
    city_code_list.append(city_code)
    city_name_list.append(area_lut_for_city['CityName'].iloc[0])

df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'BuildingNum':building_num_list, 'Area':area_list, 'BuildingDensity':building_density_list})
df.to_csv(OUTPUT_PATH.joinpath('building_density_city.csv'),index=False)

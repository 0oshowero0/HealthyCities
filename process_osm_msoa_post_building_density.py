from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd
from multiprocessing import Process, Pool

MULTI_PROCESS_NUM = 20

PROCESS_OUTPUT_PATH = Path('./temp_output/multi_process_temp/building_density_msoa_temp')
PROCESS_OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/building_density')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

INPUT_PATH = Path('./temp_output/osm_filter/building/msoa_level')


def process_all_city():
    area_lut = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_msoa.csv')
    p = Pool(MULTI_PROCESS_NUM)
    result = [p.apply_async(process_single_city, args=(city_dir, area_lut)) for city_dir in INPUT_PATH.iterdir()]
    for i in result:
        i.get()
    p.close()
    p.join()


def process_single_city(city_dir, area_lut):
    city_code = city_dir.stem
    
    area_list = []
    building_num_list = []
    building_density_list = []
    city_code_list = []
    city_name_list = []
    msoa_code_list = []
    msoa_name_list = []
    input_files = sorted([i for i in city_dir.glob('*.geojson')])

    for f in input_files:
        df = gpd.read_file(f, driver='GeoJSON')
        building_num = df.shape[0]
        msoa_code = f.stem
        area_lut_for_msoa = area_lut.loc[area_lut.MSOACode == msoa_code]

        area_list.append(area_lut_for_msoa['Area'].iloc[0])
        building_num_list.append(building_num)
        building_density_list.append(building_num/area_lut_for_msoa['Area'].iloc[0])
        city_code_list.append(city_code)
        city_name_list.append(area_lut_for_msoa['CityName'].iloc[0])
        msoa_code_list.append(msoa_code)
        msoa_name_list.append(area_lut_for_msoa['MSOAName'].iloc[0])

    df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'MSOAName':msoa_name_list, 'MSOACode':msoa_code_list,'BuildingNum':building_num_list, 'Area':area_list, 'BuildingDensity':building_density_list})
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath(city_code + '.csv'),index=False)


def post_process():
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))

    df = df.sort_values(['CityCode','MSOACode'], ascending=True)
    df.to_csv(OUTPUT_PATH.joinpath('building_density_msoa.csv'), index=False)


if __name__ == "__main__":
    begin_time = datetime.now()
    process_all_city()
    post_process()
    end_time = datetime.now()
    print('Time Consumption：' + str((end_time-begin_time).total_seconds() / 60 ) + ' minutes')


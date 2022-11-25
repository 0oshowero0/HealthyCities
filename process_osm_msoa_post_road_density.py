from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd
from multiprocessing import Process, Pool

MULTI_PROCESS_NUM = 20

PROCESS_OUTPUT_PATH = Path('./temp_output/multi_process_temp/road_density_msoa_temp')
PROCESS_OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/road_density')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

INPUT_PATH = Path('./temp_output/osm_filter/road_network/msoa_level')


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
    
    ###########################################
    # Driving Net
    area_list = []
    road_length_list = []
    road_density_list = []
    city_code_list = []
    city_name_list = []
    msoa_code_list = []
    msoa_name_list = []
    input_files = sorted([i for i in city_dir.glob('*driving.geojson')])

    for f in input_files:
        df = gpd.read_file(f, driver='GeoJSON')
        road_length = df['length'].dropna().sum() / 1000

        msoa_code = f.stem.split('_')[0]
        area_lut_for_msoa = area_lut.loc[area_lut.MSOACode == msoa_code]
        area_list.append(area_lut_for_msoa['Area'].iloc[0])
        road_length_list.append(road_length)
        road_density_list.append(road_length/area_lut_for_msoa['Area'].iloc[0])
        city_code_list.append(city_code)
        city_name_list.append(area_lut_for_msoa['CityName'].iloc[0])
        msoa_code_list.append(msoa_code)
        msoa_name_list.append(area_lut_for_msoa['MSOAName'].iloc[0])

    df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'MSOAName':msoa_name_list, 'MSOACode':msoa_code_list,'RoadLength':road_length_list, 'Area':area_list, 'RoadDensity':road_density_list})
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath('driving_' + city_code + '.csv'),index=False)

    ###########################################
    # cycling Net
    area_list = []
    road_length_list = []
    road_density_list = []
    city_code_list = []
    city_name_list = []
    msoa_code_list = []
    msoa_name_list = []
    input_files = sorted([i for i in city_dir.glob('*cycling.geojson')])

    for f in input_files:
        df = gpd.read_file(f, driver='GeoJSON')
        road_length = df['length'].dropna().sum() / 1000

        msoa_code = f.stem.split('_')[0]
        area_lut_for_msoa = area_lut.loc[area_lut.MSOACode == msoa_code]
        area_list.append(area_lut_for_msoa['Area'].iloc[0])
        road_length_list.append(road_length)
        road_density_list.append(road_length/area_lut_for_msoa['Area'].iloc[0])
        city_code_list.append(city_code)
        city_name_list.append(area_lut_for_msoa['CityName'].iloc[0])
        msoa_code_list.append(msoa_code)
        msoa_name_list.append(area_lut_for_msoa['MSOAName'].iloc[0])

    df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'MSOAName':msoa_name_list, 'MSOACode':msoa_code_list,'RoadLength':road_length_list, 'Area':area_list, 'RoadDensity':road_density_list})
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath('cycling_' + city_code + '.csv'),index=False)

    ###########################################
    # walking Net
    area_list = []
    road_length_list = []
    road_density_list = []
    city_code_list = []
    city_name_list = []
    msoa_code_list = []
    msoa_name_list = []
    input_files = sorted([i for i in city_dir.glob('*walking.geojson')])

    for f in input_files:
        df = gpd.read_file(f, driver='GeoJSON')
        road_length = df['length'].dropna().sum() / 1000

        msoa_code = f.stem.split('_')[0]
        area_lut_for_msoa = area_lut.loc[area_lut.MSOACode == msoa_code]
        area_list.append(area_lut_for_msoa['Area'].iloc[0])
        road_length_list.append(road_length)
        road_density_list.append(road_length/area_lut_for_msoa['Area'].iloc[0])
        city_code_list.append(city_code)
        city_name_list.append(area_lut_for_msoa['CityName'].iloc[0])
        msoa_code_list.append(msoa_code)
        msoa_name_list.append(area_lut_for_msoa['MSOAName'].iloc[0])

    df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'MSOAName':msoa_name_list, 'MSOACode':msoa_code_list,'RoadLength':road_length_list, 'Area':area_list, 'RoadDensity':road_density_list})
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath('walking_' + city_code + '.csv'),index=False)


def post_process():

    # driving
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('driving*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))

    df = df.sort_values(['CityCode','MSOACode'], ascending=True)
    df.to_csv(OUTPUT_PATH.joinpath('driving_road_density_msoa.csv'), index=False)

    # cycling
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('cycling*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))

    df = df.sort_values(['CityCode','MSOACode'], ascending=True)
    df.to_csv(OUTPUT_PATH.joinpath('cycling_road_density_msoa.csv'), index=False)


    # walking
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('walking*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))

    df = df.sort_values(['CityCode','MSOACode'], ascending=True)
    df.to_csv(OUTPUT_PATH.joinpath('walking_road_density_msoa.csv'), index=False)


if __name__ == "__main__":
    begin_time = datetime.now()
    process_all_city()
    post_process()
    end_time = datetime.now()
    print('Time Consumption：' + str((end_time-begin_time).total_seconds() / 60 ) + ' minutes')


from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd
from multiprocessing import Process, Pool
import shapely

MULTI_PROCESS_NUM = 29

PROCESS_OUTPUT_PATH = Path('./temp_output/multi_process_temp/walkability/road_intersection_density_city')
PROCESS_OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
OUTPUT_PATH = Path('./temp_output/walkability/road_intersection_density/')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

INPUT_PATH = Path('./temp_output/osm_filter/road_network/city_level')


def process_all_city():
    area_lut = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')
    p = Pool(MULTI_PROCESS_NUM)

    result = [p.apply_async(process_single_city, args=(area_lut.iloc[idx,:],)) for idx in range(area_lut.shape[0])]
    
    for i in result:
        i.get()
    p.close()
    p.join()


def process_single_city(area_lut):
    ###########################################
    # walking Net
    area_list = []
    road_intersection_list = []
    road_intersection_density_list = []
    city_code_list = []
    city_name_list = []
    input_file = INPUT_PATH.joinpath(area_lut['CityCode'] + '_walking.geojson')

    df = gpd.read_file(input_file, driver='GeoJSON')
    intersection = 0
    for i in range(df.shape[0]):
        for j in range(i+1, df.shape[0]):
            if i !=j:
                k = df['geometry'].iloc[i].intersection(df['geometry'].iloc[j])
                if type(k) == shapely.geometry.multipoint.MultiPoint:
                    intersection += 1
                elif type(k) == shapely.geometry.multilinestring.MultiLineString:
                    intersection += 1
                elif type(k) == shapely.geometry.multipolygon.MultiPolygon:
                    intersection += 1
                elif type(k) == shapely.geometry.collection.GeometryCollection:
                    intersection += 1
                else:
                    if len(k.coords[:]) > 0:
                        intersection += 1


    area_list.append(area_lut['Area'])
    road_intersection_list.append(intersection)
    road_intersection_density_list.append(intersection/area_lut['Area'])
    city_code_list.append(area_lut['CityCode'])
    city_name_list.append(area_lut['CityName'])


    df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'RoadIntersection':road_intersection_list, 'Area':area_list, 'RoadIntersectionDensity':road_intersection_density_list})
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath(area_lut['CityCode'] + '.csv'),index=False)


def post_process():
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))

    df = df.sort_values(['CityCode'], ascending=True)
    df.to_csv(OUTPUT_PATH.joinpath('walking_road_density_city.csv'), index=False)



if __name__ == "__main__":
    begin_time = datetime.now()
    process_all_city()
    post_process()
    end_time = datetime.now()
    print('Time Consumption：' + str((end_time-begin_time).total_seconds() / 60 ) + ' minutes')



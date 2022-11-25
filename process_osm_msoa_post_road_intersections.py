from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import geopandas as gpd
from multiprocessing import Process, Pool
import shapely

MULTI_PROCESS_NUM = 40

PROCESS_OUTPUT_PATH = Path('./temp_output/multi_process_temp/walkability/road_intersection_density_msoa')
PROCESS_OUTPUT_PATH.mkdir(exist_ok=True, parents=True)
OUTPUT_PATH = Path('./temp_output/walkability/road_intersection_density/')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

INPUT_PATH = Path('./temp_output/osm_filter/road_network/msoa_level')


def process_all_msoa():
    area_lut = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_msoa.csv')
    p = Pool(MULTI_PROCESS_NUM)

    result = [p.apply_async(process_single_msoa, args=(area_lut.iloc[idx,:],)) for idx in range(area_lut.shape[0])]
    
    for i in result:
        i.get()
    p.close()
    p.join()


def process_single_msoa(area_lut):
    ###########################################
    # walking Net
    area_list = []
    road_intersection_list = []
    road_intersection_density_list = []
    city_code_list = []
    city_name_list = []
    msoa_code_list = []
    msoa_name_list = []
    input_file = INPUT_PATH.joinpath(area_lut['CityCode']).joinpath(area_lut['MSOACode'] + '_walking.geojson')

    df = gpd.read_file(input_file, driver='GeoJSON')
    intersection = 0
    for i in range(df.shape[0]):
        for j in range(i+1, df.shape[0]):
            if i !=j:
                try:
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
                except:
                    print(input_file)
                    print(type(k))


    area_list.append(area_lut['Area'])
    road_intersection_list.append(intersection)
    road_intersection_density_list.append(intersection/area_lut['Area'])
    city_code_list.append(area_lut['CityCode'])
    city_name_list.append(area_lut['CityName'])
    msoa_code_list.append(area_lut['MSOACode'])
    msoa_name_list.append(area_lut['MSOAName'])

    df = pd.DataFrame({'CityName':city_name_list, 'CityCode':city_code_list,'MSOAName':msoa_name_list, 'MSOACode':msoa_code_list,'RoadIntersection':road_intersection_list, 'Area':area_list, 'RoadIntersectionDensity':road_intersection_density_list})
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath(area_lut['MSOACode'] + '.csv'),index=False)


def post_process():
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))

    df = df.sort_values(['CityCode','MSOACode'], ascending=True)
    df.to_csv(OUTPUT_PATH.joinpath('walking_road_density_msoa.csv'), index=False)



if __name__ == "__main__":
    begin_time = datetime.now()
    process_all_msoa()
    post_process()
    end_time = datetime.now()
    print('Time Consumption：' + str((end_time-begin_time).total_seconds() / 60 ) + ' minutes')



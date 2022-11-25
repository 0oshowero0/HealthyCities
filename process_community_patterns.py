from datetime import datetime
import numpy as np
import pandas as pd
import geopandas as gpd
from pathlib import Path
from shapely.geometry import Point
from multiprocessing import Process, Pool

INPUT_PATH = Path('./temp_output/GoogleStreetView_Segmentation')
PROCESS_OUTPUT_PATH = Path('./temp_output/multi_process_temp/GoogleStreetView')
OUTPUT_PATH = Path('./output/environmental_determinants/built_environment/community_pattern')
PROCESS_OUTPUT_PATH.mkdir(exist_ok=True,parents=True)
OUTPUT_PATH.mkdir(exist_ok=True,parents=True)

MULTI_PROCESS_NUM = 29

def process_all_city():
    msoa_boundary = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson', driver='geojson')
    city_code_list = msoa_boundary['CityCode'].drop_duplicates().to_list()
    p = Pool(MULTI_PROCESS_NUM)
    result = [p.apply_async(process_single_city, args=(city_code_list[i],)) for i in range(len(city_code_list))]
    for i in result:
        i.get()
    p.close()
    p.join()

def process_single_city(city_code,):
    msoa_boundary = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson', driver='geojson')
    df = pd.DataFrame()
    for input_sub_dir in INPUT_PATH.iterdir():
        specific_city_msoa_boundary = msoa_boundary.loc[msoa_boundary['CityCode']==city_code]
        seg_result = pd.read_csv(input_sub_dir.joinpath('segmentation_meta_info.csv'))
        for _, row in seg_result.iterrows():
            loc = Point(row['real_longti'],row['real_lati'])
            loc_msoa_info = specific_city_msoa_boundary.loc[specific_city_msoa_boundary['geometry'].map(lambda x:x.contains(loc))]
            if loc_msoa_info.shape[0] > 0:
                new_df = row[9:]
                new_df['CityName'] = loc_msoa_info['CityName'].iloc[0]
                new_df['CityCode'] = loc_msoa_info['CityCode'].iloc[0]
                new_df['MSOAName'] = loc_msoa_info['MSOAName'].iloc[0]
                new_df['MSOACode'] = loc_msoa_info['MSOACode'].iloc[0]
                df = df.append(new_df)
    df.to_csv(PROCESS_OUTPUT_PATH.joinpath('community_patterns_all_' + city_code + '.csv'), index=False)
    print("City " + city_code + ' completed.')

def post_process():
    input_files = sorted([i for i in PROCESS_OUTPUT_PATH.glob('*.csv')])
    df = pd.DataFrame()
    for i in input_files:
        df = df.append(pd.read_csv(i))
    #df.to_csv(OUTPUT_PATH.joinpath('community_patterns_all.csv'), index=False)

    df_agg_msoa = df.groupby(['CityName','CityCode','MSOAName','MSOACode']).mean().reset_index()
    df_agg_msoa = df_agg_msoa.sort_values(['CityCode','MSOACode'],ascending=True)
    #df_agg_msoa = df_agg_msoa[['CityName','CityCode','MSOAName','MSOACode'] + df_agg_msoa.columns.to_list()[:-4]]
    df_agg_msoa.to_csv(OUTPUT_PATH.joinpath('community_patterns_msoa.csv'), index=False)


    df_agg_city = df.drop(['MSOACode','MSOAName'],axis=1)
    df_agg_city = df_agg_city.groupby(['CityName','CityCode']).mean().reset_index()
    df_agg_city = df_agg_city.sort_values(['CityCode'],ascending=True)
    #df_agg_city = df_agg_city[['CityName','CityCode'] + df_agg_city.columns.to_list()[:-2]]
    df_agg_city.to_csv(OUTPUT_PATH.joinpath('community_patterns_city.csv'), index=False)


if __name__ == "__main__":
    begin_time = datetime.now()
    process_all_city()
    post_process()
    end_time = datetime.now()
    print('Time Consumption：' + str((end_time-begin_time).total_seconds() / 60 ) + ' minutes')
    


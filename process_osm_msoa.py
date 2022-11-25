from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path
import matplotlib.pyplot as plt
import pyrosm
import geopandas as gpd
from multiprocessing import Process, Pool
import warnings
warnings.filterwarnings("ignore")


MULTI_PROCESS_NUM = 20

OUTPUT_PATH_ROAD_NETWORK = Path('./temp_output/osm_filter/road_network/msoa_level')
OUTPUT_PATH_ROAD_NETWORK.mkdir(exist_ok=True, parents=True)

OUTPUT_PATH_BUILDING = Path('./temp_output/osm_filter/building/msoa_level')
OUTPUT_PATH_BUILDING.mkdir(exist_ok=True, parents=True)

OUTPUT_PATH_POI = Path('./temp_output/osm_filter/poi/msoa_level')
OUTPUT_PATH_POI.mkdir(exist_ok=True, parents=True)

OUTPUT_PATH_LANDUSE = Path('./temp_output/osm_filter/landuse/msoa_level')
OUTPUT_PATH_LANDUSE.mkdir(exist_ok=True, parents=True)

OUTPUT_PATH_NATURAL = Path('./temp_output/osm_filter/natural/msoa_level')
OUTPUT_PATH_NATURAL.mkdir(exist_ok=True, parents=True)

def process_all_msoa():
    msoa_boundary = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson', driver='GeoJSON')[['CityCode','MSOACode','geometry']]
    osm_lut = pd.read_csv('./city_defination_and_LUTs/osm_look_up_table.csv')

    msoa_boundary_with_osm_loc = msoa_boundary.merge(osm_lut,left_on='CityCode',right_on='CityCode')

    p = Pool(MULTI_PROCESS_NUM)
    result = [p.apply_async(process_single_msoa, args=(msoa_boundary_with_osm_loc, idx)) for idx in range(msoa_boundary_with_osm_loc.shape[0])]
    for i in result:
        i.get()
    p.close()
    p.join()


def process_single_msoa(msoa_boundary_with_osm_loc, idx):
    single_msoa = msoa_boundary_with_osm_loc.iloc[idx,:]
    osm = pyrosm.OSM('./osm/' + single_msoa['OSMFileName'], bounding_box=single_msoa['geometry'])

    OUTPUT_PATH_ROAD_NETWORK.joinpath(single_msoa['CityCode']).mkdir(exist_ok=True, parents=True)
    drive_net = osm.get_network(network_type="driving")
    drive_net.to_file(OUTPUT_PATH_ROAD_NETWORK.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '_' + 'driving.geojson') , driver='GeoJSON')
    walking_net = osm.get_network(network_type="walking")
    walking_net.to_file(OUTPUT_PATH_ROAD_NETWORK.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '_' + 'walking.geojson'), driver='GeoJSON')
    cycling_net = osm.get_network(network_type="cycling")
    cycling_net.to_file(OUTPUT_PATH_ROAD_NETWORK.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '_' + 'cycling.geojson'), driver='GeoJSON')

    OUTPUT_PATH_BUILDING.joinpath(single_msoa['CityCode']).mkdir(exist_ok=True, parents=True)
    buildings = osm.get_buildings()
    buildings.to_file(OUTPUT_PATH_BUILDING.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '.geojson'), driver='GeoJSON')

    # OUTPUT_PATH_POI.joinpath(single_msoa['CityCode']).mkdir(exist_ok=True, parents=True)
    # pois = osm.get_pois()
    # pois.to_file(OUTPUT_PATH_POI.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '.geojson'), driver='GeoJSON')

    # OUTPUT_PATH_LANDUSE.joinpath(single_msoa['CityCode']).mkdir(exist_ok=True, parents=True)
    # landuse = osm.get_landuse()
    # landuse.to_file(OUTPUT_PATH_LANDUSE.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '.geojson'), driver='GeoJSON')

    # OUTPUT_PATH_NATURAL.joinpath(single_msoa['CityCode']).mkdir(exist_ok=True, parents=True)
    # natural = osm.get_natural()
    # natural.to_file(OUTPUT_PATH_NATURAL.joinpath(single_msoa['CityCode']).joinpath(single_msoa['MSOACode'] + '.geojson'), driver='GeoJSON')


if __name__ == "__main__":
    begin_time = datetime.now()
    process_all_msoa()
    end_time = datetime.now()
    print('Time Consumption：' + str((end_time-begin_time).total_seconds() / 60 ) + ' minutes')



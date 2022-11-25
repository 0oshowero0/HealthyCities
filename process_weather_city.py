import pandas as pd
import geopandas as gpd
from pathlib import Path
import h5netcdf
from haversine import haversine


OUTPUT_PATH = Path('./output/environmental_determinants/natural_environment/weather')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)


############################
# city centroid
centroid = gpd.read_file('./output/environmental_determinants/basic_statistics/centroid/geographical_centroid_city.geojson', driver='geojson')
centroid['longti'] = centroid['geometry'].map(lambda x:x.x)
centroid['latit'] = centroid['geometry'].map(lambda x:x.y)


############################
# generate city-grid look-up table

# you can open any other .nc file in ./weather since they use the same spatial partition method
with h5netcdf.File('./weather/12km/temperature_min/tasmin_hadukgrid_uk_12km_day_20190101-20190131.nc', 'r') as f:
    latitude = f['latitude'][:]  # (112, 82)
    longitude = f['longitude'][:]  # (112, 82)
    y_list = []
    x_list = []
    for _, row in centroid.iterrows():
        min_dist = 999
        min_y = -1
        min_x = -1
        for y in range(latitude.shape[0]):
            for x in range(latitude.shape[1]):
                dist = haversine((row['latit'],row['longti']), (latitude[y,x], longitude[y,x]), unit='mi')
                if dist < min_dist:
                    min_dist = dist
                    min_y = y
                    min_x = x
        y_list.append(min_y)
        x_list.append(min_x)
    centroid['y_index'] = pd.Series(y_list)
    centroid['x_index'] = pd.Series(x_list)

centroid = centroid.drop(['geometry','longti','latit'],axis=1)

############################
# Daily: temperature min and max
temperature_min_loc = Path('./weather/12km/temperature_min')
file_loc = sorted([i for i in temperature_min_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
temperature_list = []
time_list = []
for single_file in file_loc:
    year_month = single_file.stem.split('_')[-1].split('-')[0][:4] + '-' + single_file.stem.split('_')[-1].split('-')[0][4:6]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['tasmin'][:].shape[0]):
            year_month_day = year_month + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month_day)
                temperature_list.append(f['tasmin'][t, row['y_index'], row['x_index']])

temperature_min_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'TemperatureMin':temperature_list,'Time':time_list})
temperature_min_df = temperature_min_df.sort_values(['CityCode','Time'],ascending=True)
temperature_min_df.to_csv(OUTPUT_PATH.joinpath('tempetature_min_city.csv'), index=False)


temperature_max_loc = Path('./weather/12km/temperature_max')
file_loc = sorted([i for i in temperature_max_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
temperature_list = []
time_list = []
for single_file in file_loc:
    year_month = single_file.stem.split('_')[-1].split('-')[0][:4] + '-' + single_file.stem.split('_')[-1].split('-')[0][4:6]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['tasmax'][:].shape[0]):
            year_month_day = year_month + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month_day)
                temperature_list.append(f['tasmax'][t, row['y_index'], row['x_index']])

temperature_max_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'TemperatureMax':temperature_list,'Time':time_list})
temperature_max_df = temperature_max_df.sort_values(['CityCode','Time'],ascending=True)
temperature_max_df.to_csv(OUTPUT_PATH.joinpath('tempetature_max_city.csv'), index=False)


############################
# Daily: rainfall
rainfall_loc = Path('./weather/12km/rainfall')
file_loc = sorted([i for i in rainfall_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
rainfall_list = []
time_list = []
for single_file in file_loc:
    year_month = single_file.stem.split('_')[-1].split('-')[0][:4] + '-' + single_file.stem.split('_')[-1].split('-')[0][4:6]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['rainfall'][:].shape[0]):
            year_month_day = year_month + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month_day)
                rainfall_list.append(f['rainfall'][t, row['y_index'], row['x_index']])

rainfall_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'Rainfall':rainfall_list,'Time':time_list})
rainfall_df = rainfall_df.sort_values(['CityCode','Time'],ascending=True)
rainfall_df.to_csv(OUTPUT_PATH.joinpath('rainfall_city.csv'), index=False)


############################
# Monthly: relative_humidity
humidity_loc = Path('./weather/12km/relative_humidity')
file_loc = sorted([i for i in humidity_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
humidity_list = []
time_list = []
for single_file in file_loc:
    year = single_file.stem.split('_')[-1].split('-')[0][:4]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['hurs'][:].shape[0]):
            year_month = year + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month)
                humidity_list.append(f['hurs'][t, row['y_index'], row['x_index']])

humidity_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'RelativeHumidity':humidity_list,'Time':time_list})
humidity_df = humidity_df.sort_values(['CityCode','Time'],ascending=True)
humidity_df.to_csv(OUTPUT_PATH.joinpath('relative_humidity_city.csv'), index=False)

############################
# Monthly: snow lying days
snow_loc = Path('./weather/12km/snow_lying_days')
file_loc = sorted([i for i in snow_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
snow_list = []
time_list = []
for single_file in file_loc:
    year = single_file.stem.split('_')[-1].split('-')[0][:4]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['snowLying'][:].shape[0]):
            year_month = year + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month)
                snow_list.append(f['snowLying'][t, row['y_index'], row['x_index']])

snow_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'SnowLyingDays':snow_list,'Time':time_list})
snow_df = snow_df.sort_values(['CityCode','Time'],ascending=True)
snow_df.to_csv(OUTPUT_PATH.joinpath('snow_lying_days_city.csv'), index=False)



############################
# Monthly: sunshine hours
sun_loc = Path('./weather/12km/sunshine_hours')
file_loc = sorted([i for i in sun_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
sun_list = []
time_list = []
for single_file in file_loc:
    year = single_file.stem.split('_')[-1].split('-')[0][:4]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['sun'][:].shape[0]):
            year_month = year + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month)
                sun_list.append(f['sun'][t, row['y_index'], row['x_index']])

sun_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'SunshineHours':sun_list,'Time':time_list})
sun_df = sun_df.sort_values(['CityCode','Time'],ascending=True)
sun_df.to_csv(OUTPUT_PATH.joinpath('sunshine_hours_city.csv'), index=False)


############################
# Monthly: wind speed
wind_loc = Path('./weather/12km/wind_speed')
file_loc = sorted([i for i in wind_loc.glob('*.nc')])
city_name_list = []
city_code_list = []
wind_list = []
time_list = []
for single_file in file_loc:
    year = single_file.stem.split('_')[-1].split('-')[0][:4]
    with h5netcdf.File(single_file, 'r') as f:
        for t in range(f['sfcWind'][:].shape[0]):
            year_month = year + '-' + str(t+1).zfill(2)
            for _, row in centroid.iterrows():
                city_name_list.append(row['CityName'])
                city_code_list.append(row['CityCode'])
                time_list.append(year_month)
                wind_list.append(f['sfcWind'][t, row['y_index'], row['x_index']])

wind_df = pd.DataFrame({'CityName':city_name_list,'CityCode':city_code_list,'WindSpeed':wind_list,'Time':time_list})
wind_df = wind_df.sort_values(['CityCode','Time'],ascending=True)
wind_df.to_csv(OUTPUT_PATH.joinpath('wind_speed_city.csv'), index=False)
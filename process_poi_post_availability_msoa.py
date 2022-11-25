import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./temp_output/poi')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

OUTPUT_PATH_AVAIL = Path('./output/environmental_determinants/health_related_behaviour_environment/')
OUTPUT_PATH_AVAIL.mkdir(exist_ok=True, parents=True)

poi = pd.read_csv('./temp_output/poi/poi.csv',dtype='str')

tobacco_naics = ['453991','4451','44551','445110','44512','445120']
alcohol_naics = ['7224','72241','722410','4453','44531','445310','4451','44551','445110','44512','445120']
health_naics = ['446','4461','44611','446110','622','623','621']
physical_exercise_naics = ['71394','71219','713940','712190']

poi['NAICSCode_3'] = poi['NAICSCode'].map(lambda x: x[:3])

tobacco_poi = poi[poi['NAICSCode'].isin(tobacco_naics)].drop(['NAICSCode_3'],axis=1)
alcohol_poi = poi[poi['NAICSCode'].isin(alcohol_naics)].drop(['NAICSCode_3'],axis=1)
health_poi = poi[poi['NAICSCode'].isin(health_naics) | poi['NAICSCode_3'].isin(health_naics)].drop(['NAICSCode_3'],axis=1)
physical_exercise_poi = poi[poi['NAICSCode'].isin(physical_exercise_naics)].drop(['NAICSCode_3'],axis=1)

tobacco_poi.to_csv(OUTPUT_PATH.joinpath('tobacco_poi.csv'),index=False)
alcohol_poi.to_csv(OUTPUT_PATH.joinpath('alcohol_poi.csv'),index=False)
health_poi.to_csv(OUTPUT_PATH.joinpath('health_poi.csv'),index=False)
physical_exercise_poi.to_csv(OUTPUT_PATH.joinpath('physical_exercise_poi.csv'),index=False)


tobacco_poi_availability = tobacco_poi[['MSOACode']].value_counts().reset_index()
tobacco_poi_availability = tobacco_poi_availability.rename(columns={0:'POINum'})
alcohol_poi_availability = alcohol_poi[['MSOACode']].value_counts().reset_index()
alcohol_poi_availability = alcohol_poi_availability.rename(columns={0:'POINum'})
health_poi_availability = health_poi[['MSOACode']].value_counts().reset_index()
health_poi_availability = health_poi_availability.rename(columns={0:'POINum'})
physical_exercise_poi_availability = physical_exercise_poi[['MSOACode']].value_counts().reset_index()
physical_exercise_poi_availability = physical_exercise_poi_availability.rename(columns={0:'POINum'})

population = pd.read_csv('./output/environmental_determinants/basic_statistics/population/population_msoa.csv')
tobacco_poi_availability = tobacco_poi_availability.merge(population,left_on='MSOACode',right_on='MSOACode',how='right')
tobacco_poi_availability = tobacco_poi_availability.fillna(0.0)
tobacco_poi_availability['Availability'] = tobacco_poi_availability['POINum'] / tobacco_poi_availability['Population']
tobacco_poi_availability = tobacco_poi_availability[['CityName','CityCode','MSOAName','MSOACode','POINum','Population','Availability']]
alcohol_poi_availability = alcohol_poi_availability.merge(population,left_on='MSOACode',right_on='MSOACode',how='right')
alcohol_poi_availability = alcohol_poi_availability.fillna(0.0)
alcohol_poi_availability['Availability'] = alcohol_poi_availability['POINum'] / alcohol_poi_availability['Population']
alcohol_poi_availability = alcohol_poi_availability[['CityName','CityCode','MSOAName','MSOACode','POINum','Population','Availability']]
health_poi_availability = health_poi_availability.merge(population,left_on='MSOACode',right_on='MSOACode',how='right')
health_poi_availability = health_poi_availability.fillna(0.0)
health_poi_availability['Availability'] = health_poi_availability['POINum'] / health_poi_availability['Population']
health_poi_availability = health_poi_availability[['CityName','CityCode','MSOAName','MSOACode','POINum','Population','Availability']]
physical_exercise_poi_availability = physical_exercise_poi_availability.merge(population,left_on='MSOACode',right_on='MSOACode',how='right')
physical_exercise_poi_availability = physical_exercise_poi_availability.fillna(0.0)
physical_exercise_poi_availability['Availability'] = physical_exercise_poi_availability['POINum'] / physical_exercise_poi_availability['Population']
physical_exercise_poi_availability = physical_exercise_poi_availability[['CityName','CityCode','MSOAName','MSOACode','POINum','Population','Availability']]

tobacco_poi_availability = tobacco_poi_availability.sort_values(['CityCode','MSOACode'], ascending=True)
alcohol_poi_availability = alcohol_poi_availability.sort_values(['CityCode','MSOACode'], ascending=True)
health_poi_availability = health_poi_availability.sort_values(['CityCode','MSOACode'], ascending=True)
physical_exercise_poi_availability = physical_exercise_poi_availability.sort_values(['CityCode','MSOACode'], ascending=True)

tobacco_poi_availability.to_csv(OUTPUT_PATH_AVAIL.joinpath('tobacco_availability_msoa.csv'),index=False)
alcohol_poi_availability.to_csv(OUTPUT_PATH_AVAIL.joinpath('alcohol_availability_msoa.csv'),index=False)
health_poi_availability.to_csv(OUTPUT_PATH_AVAIL.joinpath('health_availability_msoa.csv'),index=False)
physical_exercise_poi_availability.to_csv(OUTPUT_PATH_AVAIL.joinpath('physical_exercise_availability_msoa.csv'),index=False)

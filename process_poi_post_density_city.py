import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./temp_output/walkability/daily_living_score')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

poi = pd.read_csv('./temp_output/poi/poi.csv',dtype='str')

selected_naics = ['4451','44551','445110','44512','445120','71219','481','482','483','485']
poi['NAICSCode_3'] = poi['NAICSCode'].map(lambda x: x[:3])

poi = poi[poi['NAICSCode'].isin(selected_naics) | poi['NAICSCode_3'].isin(selected_naics)].drop(['NAICSCode_3'],axis=1)
poi['Count'] = pd.Series([1 for _ in range(poi.shape[0])])
poi = poi[['CityName','CityCode','Count']]
poi = poi.groupby(['CityName','CityCode']).sum().reset_index()

area_lut = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')[['CityCode','Area']]
poi = poi.merge(area_lut, left_on='CityCode', right_on='CityCode')

poi['DailyLivingScore'] = poi['Count'] / poi['Area']
poi = poi.drop(['Count','Area'],axis=1)

poi.to_csv(OUTPUT_PATH.joinpath('daily_living_score_city.csv'),index=False)

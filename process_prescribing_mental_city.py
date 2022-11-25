from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

INPUT_PATH = Path('./prescribing/original_data/mental')
OUTPUT_PATH =  Path('./output/health_outcome/mental_health/prescribing')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

# postcode - LTLA lookup table
lut = pd.read_csv('./city_defination_and_LUTs/pcd_oa_lsoa_msoa_ltla_utla_rgn_ctry_ew_may_2021_lu.csv',dtype=str)
lut = lut[['pcd','ltla22cd']]

# city list
city = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv',dtype=str)
city = city[['CityName','CityCode','LTLACode']]
city = city.merge(lut, left_on='LTLACode', right_on='ltla22cd', how='left').drop('ltla22cd',axis=1)



total_data = pd.DataFrame()
for fp in sorted([i for i in INPUT_PATH.glob('*.csv')]):
    data = pd.read_csv(fp,dtype=str)
    total_data = pd.concat([total_data,data])

total_data = total_data.reset_index()
total_data = total_data.dropna()

def process_pcd(x):
    if len(x) > 7:
        return ''.join(x.split(' '))
    elif len(x) == 6:
        return '  '.join(x.split(' '))
    else:
        return x

total_data['postcode'] = total_data['postcode'].map(process_pcd)
total_data = total_data.loc[total_data['postcode'] != '-']  

total_data = city.merge(total_data,left_on='pcd',right_on='postcode',how='left')
total_data = total_data.dropna()

total_data = total_data.drop(['index','pcd','postcode'],axis=1)
total_data['actual_cost'] = total_data['actual_cost'].astype(float)
total_data = total_data.groupby(['CityName','CityCode','LTLACode','year_month']).sum().reset_index()

total_data['year_month'] = total_data['year_month'].map(lambda x: x[:4]+'-'+x[4:])


pop = pd.read_csv('./output/environmental_determinants/basic_statistics/population/population_city.csv')[['CityCode','Population']]
total_data = total_data.merge(pop, left_on='CityCode', right_on='CityCode', how='inner')
total_data = total_data.rename(columns={'year_month':'Date', 'actual_cost':'ActualCost'})
total_data['PerCitizenCost'] = total_data['ActualCost'] / total_data['Population']
total_data = total_data.drop(['LTLACode','Population'],axis=1)
total_data = total_data.sort_values(['CityCode'], ascending=True)
total_data.to_csv(OUTPUT_PATH.joinpath('mental_prescribing_city.csv'),index=False)

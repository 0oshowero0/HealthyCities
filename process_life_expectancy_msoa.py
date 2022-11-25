from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/health_outcome/life_expectancy')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

msoa = pd.read_csv('./city_defination_and_LUTs/msoa_look_up_table.csv')
msoa = msoa[['CityName','CityCode','MSOAName','MSOACode']]

le_male = pd.read_csv('./life_expectancy/life_expectancy_males.csv')
le_female = pd.read_csv('./life_expectancy/life_expectancy_females.csv')
hle_male = pd.read_csv('./life_expectancy/healthy_life_expectancy_males.csv')
hle_female = pd.read_csv('./life_expectancy/healthy_life_expectancy_females.csv')

le_male = msoa.merge(le_male, left_on='MSOACode', right_on='MSOACode',how='left')
le_female = msoa.merge(le_female, left_on='MSOACode', right_on='MSOACode',how='left')
hle_male = msoa.merge(hle_male, left_on='MSOACode', right_on='MSOACode',how='left')
hle_female = msoa.merge(hle_female, left_on='MSOACode', right_on='MSOACode',how='left')

le_value = []
le_gender = []
le_upper = []
le_lower = []
le_cityname = []
le_citycode = []
le_msoaname = []
le_msoacode = []

for _, row in le_male.iterrows():
    le_value.append(row['Value'])
    le_upper.append(row['UpperConfidenceInterval'])
    le_lower.append(row['LowerConfidenceInterval'])
    le_cityname.append(row['CityName'])
    le_citycode.append(row['CityCode'])
    le_msoaname.append(row['MSOAName'])
    le_msoacode.append(row['MSOACode'])
    le_gender.append('Male')

for _, row in le_female.iterrows():
    le_value.append(row['Value'])
    le_upper.append(row['UpperConfidenceInterval'])
    le_lower.append(row['LowerConfidenceInterval'])
    le_cityname.append(row['CityName'])
    le_citycode.append(row['CityCode'])
    le_msoaname.append(row['MSOAName'])
    le_msoacode.append(row['MSOACode'])
    le_gender.append('Female')

le = pd.DataFrame({'CityName':le_cityname, 'CityCode':le_citycode, 'MSOAName':le_msoaname, 'MSOACode':le_msoacode, 'Value':le_value, 'LowerConfidenceInterval':le_lower, 'UpperConfidenceInterval':le_upper, 'Gender':le_gender})


hle_value = []
hle_gender = []
hle_upper = []
hle_lower = []
hle_cityname = []
hle_citycode = []
hle_msoaname = []
hle_msoacode = []

for _, row in hle_male.iterrows():
    hle_value.append(row['Value'])
    hle_upper.append(row['UpperConfidenceInterval'])
    hle_lower.append(row['LowerConfidenceInterval'])
    hle_cityname.append(row['CityName'])
    hle_citycode.append(row['CityCode'])
    hle_msoaname.append(row['MSOAName'])
    hle_msoacode.append(row['MSOACode'])
    hle_gender.append('Male')

for _, row in hle_female.iterrows():
    hle_value.append(row['Value'])
    hle_upper.append(row['UpperConfidenceInterval'])
    hle_lower.append(row['LowerConfidenceInterval'])
    hle_cityname.append(row['CityName'])
    hle_citycode.append(row['CityCode'])
    hle_msoaname.append(row['MSOAName'])
    hle_msoacode.append(row['MSOACode'])
    hle_gender.append('Female')

hle = pd.DataFrame({'CityName':hle_cityname, 'CityCode':hle_citycode, 'MSOAName':hle_msoaname, 'MSOACode':hle_msoacode, 'Value':hle_value, 'LowerConfidenceInterval':hle_lower, 'UpperConfidenceInterval':hle_upper, 'Gender':hle_gender})

le = le.sort_values(by=['CityCode','MSOACode'])
hle = hle.sort_values(by=['CityCode','MSOACode'])
le.to_csv(OUTPUT_PATH.joinpath('life_expectancy_msoa.csv'),index=False,sep=',')
hle.to_csv(OUTPUT_PATH.joinpath('healthy_life_expectancy_msoa.csv'),index=False,sep=',')

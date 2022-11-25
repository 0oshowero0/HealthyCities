from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/health_outcome/physical_health/covid_data')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

msoa_lut = pd.read_csv('./city_defination_and_LUTs/msoa_look_up_table.csv')
msoa_lut = msoa_lut[['CityName','CityCode','MSOAName','MSOACode']]
msoa_lut = msoa_lut.drop_duplicates()

data = pd.read_csv('./COVID/msoa.csv').drop(['regionCode','regionName','UtlaCode','UtlaName','LtlaCode','LtlaName','areaType','areaName'],axis=1)
#################################
data = msoa_lut.merge(data,left_on='MSOACode', right_on='areaCode',how='left').drop(['areaCode'],axis = 1)
data = data.drop(['MSOACode','MSOAName'],axis=1)
data = data.groupby(['CityName','CityCode','date']).sum().reset_index()

rename_dict = {'date':'Date','newCasesBySpecimenDateRollingSum':'NewCasesBySpecimenDateRollingSum'}
data = data.rename(columns=rename_dict)

#data = data.loc[data['Date']<'2022-11-01']
data = data.sort_values(by=['CityCode','Date'], ascending=True)
data = data[['CityName','CityCode','Date','NewCasesBySpecimenDateRollingSum']]

data.to_csv(OUTPUT_PATH.joinpath('COVID_city.csv'),index=False)
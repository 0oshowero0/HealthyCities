import pandas as pd
from pathlib import Path


city_lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
msoa_lut = pd.read_csv('./city_defination_and_LUTs/Middle_Layer_Super_Output_Area_(2011)_to_Major_Towns_and_Cities_(December_2015)_Lookup_in_England_and_Wales.csv')[['MSOA11CD','MSOA11NM','TCITY15CD']]
msoa_lut = msoa_lut.rename(columns={'MSOA11NM':'MSOAName','MSOA11CD':'MSOACode'})
msoa_in_city = city_lut.merge(msoa_lut, left_on='CityCode', right_on='TCITY15CD', how='left').drop(['TCITY15CD'],axis=1)
msoa_in_city = msoa_in_city.sort_values(['CityCode','MSOACode'], ascending=True)
msoa_in_city.to_csv('./city_defination_and_LUTs/msoa_look_up_table.csv',index=False)
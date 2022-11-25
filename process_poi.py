import pandas as pd
from pathlib import Path


poi = pd.read_csv('./POI/UK_places.csv',dtype='str')
poi['pcd_len'] = poi['postal_code'].map(lambda x: len(str(x)))
poi = poi.loc[(poi['pcd_len']>=6) & (poi['pcd_len']<=8)]
def process_pcd(x):
    if len(x) > 7:
        return ''.join(x.split(' '))
    elif len(x) == 6:
        return '  '.join(x.split(' '))
    else:
        return x

poi['PostCode'] = poi['postal_code'].map(process_pcd)
poi = poi.rename(columns={'placekey':'POICode','location_name':'POIName','top_category':'TopCategory','sub_category':'SubCategory',
'naics_code':'NAICSCode','latitude':'Latitude','longitude':'Longitude'})

lut = pd.read_csv('./city_defination_and_LUTs/pcd_oa_lsoa_msoa_ltla_utla_rgn_ctry_ew_may_2021_lu.csv',dtype=str)
lut = lut[['pcd','msoa21cd']]

city = pd.read_csv('msoa_look_up_table.csv',dtype=str)
city = city[['CityName','CityCode','LTLAName','LTLACode','MSOAName','MSOACode']]
city = city.merge(lut, left_on='MSOACode', right_on='msoa21cd', how='left').drop(['msoa21cd'],axis=1)

city = city.merge(poi,left_on='pcd',right_on='PostCode',how='left')[['POIName','POICode','TopCategory','SubCategory','NAICSCode','Latitude','Longitude','PostCode','CityName','CityCode','MSOAName','MSOACode']]
city = city.loc[~city['POIName'].isnull()]
city = city.loc[~city['NAICSCode'].isnull()]
city.to_csv('./temp_output/poi/poi.csv',index=False)
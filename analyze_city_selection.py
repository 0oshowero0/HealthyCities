from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
sns.set_theme(style="white", palette=None)

plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13

'''
######################################################################################################
# with built up area
built_up_area = pd.read_csv('./built_up_area/Built-up_Areas_(December_2011)_Boundaries_V2.csv')
built_up_area = built_up_area.loc[built_up_area['urban_bua']=='Yes'][['bua11cd','st_areashape']]
built_up_area['st_areashape'] /=  1000000
msoa_pop = pd.read_csv('./msoa_pop/msoa_pop.csv')
built_up_msoa_lut = pd.read_csv('./built_up_area/Middle_Layer_Super_Output_Area_(2011)_to_Built-up_Area_Sub_Division_to_Built-up_Area_to_Local_Authority_District_to_Region_(December_2011)_Lookup_in_England_and_Wales.csv')
built_up_msoa_lut = built_up_msoa_lut[['MSOA11CD','BUA11CD']].dropna(how='any')
built_up_msoa_lut = built_up_msoa_lut.merge(built_up_area,left_on='BUA11CD', right_on='bua11cd', how='right').drop(['bua11cd','st_areashape'],axis=1)
built_up_pop = built_up_msoa_lut.merge(msoa_pop, left_on='MSOA11CD', right_on='MSOACode', how='left').drop(['MSOA11CD','MSOACode'],axis=1).groupby('BUA11CD').sum().reset_index()
built_up_pop_den = built_up_pop.merge(built_up_area,left_on='BUA11CD',right_on='bua11cd')[['bua11cd','Population','st_areashape']]
built_up_pop_den['Density'] = built_up_pop_den['Population'] / (built_up_pop_den['st_areashape'])


city_area = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')
city_pop = pd.read_csv('./output/environmental_determinants/basic_statistics/population/population_city.csv')
city_pop_den = city_area.merge(city_pop,left_on='CityCode',right_on='CityCode')[['CityCode','Area','Population']]
city_pop_den['Density'] = city_pop_den['Population'] / city_pop_den['Area']


# merge to long table for ploting
area_bua = built_up_area['st_areashape'].to_list()
area_city = city_area['Area'].to_list()
area_list = area_bua + area_city
type_list_area = ['Urban Built-up Areas' for _ in range(len(area_bua))] + ['Selected Cities' for _ in range(len(area_city))]
area = pd.DataFrame({'Type':type_list_area, 'Area':area_list})

pop_bua = built_up_pop['Population'].to_list()
pop_city = city_pop['Population'].to_list()
pop_list = pop_bua + pop_city
type_list_pop = ['Urban Built-up Areas' for _ in range(len(pop_bua))] + ['Selected Cities' for _ in range(len(pop_city))]
pop = pd.DataFrame({'Type':type_list_pop, 'Population':pop_list})

pop_den_bua = built_up_pop_den['Density'].to_list()
pop_den_city = city_pop_den['Density'].to_list()
pop_den_list = pop_den_bua + pop_den_city
type_list_pop_den = ['Urban Built-up Areas' for _ in range(len(built_up_pop_den))] + ['Selected Cities' for _ in range(len(pop_den_city))]
pop_den = pd.DataFrame({'Type':type_list_pop_den, 'Density':pop_den_list})


# plot
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=area, x='Type',y='Area')
ax1.set_ylabel('Area',size=20)
ax1.set_xlabel('',size=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='x', labelsize=20)
plt.show()

fig, ax2 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=pop, x='Type',y='Population')
ax2.set_ylabel('Population',size=20)
ax2.set_xlabel('',size=20)
ax2.tick_params(axis='y', labelsize=20)
ax2.tick_params(axis='x', labelsize=20)
plt.show()

fig, ax3 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=pop_den, x='Type',y='Density')
ax3.set_ylabel('Population Density',size=20)
ax3.set_xlabel('',size=20)
ax3.tick_params(axis='y', labelsize=20)
ax3.tick_params(axis='x', labelsize=20)
plt.show()

'''

######################################################################################################
# with all England cities
selected_city_area = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')
selected_city_pop = pd.read_csv('./output/environmental_determinants/basic_statistics/population/population_city.csv')
selected_city_pop_density = selected_city_area.merge(selected_city_pop,left_on='CityCode',right_on='CityCode')[['CityCode','Area','Population']]
selected_city_pop_density['Density'] = selected_city_pop_density['Population'] / selected_city_pop_density['Area']

all_city_msoa_lut = pd.read_csv('./city_defination_and_LUTs/Middle_Layer_Super_Output_Area_(2011)_to_Major_Towns_and_Cities_(December_2015)_Lookup_in_England_and_Wales.csv')[['MSOA11CD', 'TCITY15CD']]
msoa_pop = pd.read_csv('./msoa_pop/msoa_pop.csv')
all_city_pop = msoa_pop.merge(all_city_msoa_lut, left_on='MSOACode', right_on='MSOA11CD', how='right')[['Population','TCITY15CD']]
all_city_pop = all_city_pop.groupby('TCITY15CD').sum().reset_index()
all_city_area = pd.read_csv('./city_defination_and_LUTs/Major_Towns_and_Cities_(December_2015)_Boundaries_V2.csv')[['TCITY15CD','Shape__Area']]
all_city_area['Shape__Area'] /= 1000000
all_city_pop_density = all_city_area.merge(all_city_pop,left_on='TCITY15CD',right_on='TCITY15CD')[['TCITY15CD','Shape__Area','Population']]
all_city_pop_density['Density'] = all_city_pop_density['Population'] / (all_city_pop_density['Shape__Area'])

# merge to long table for ploting
area_all_city = all_city_area['Shape__Area'].to_list()
area_selected_city = selected_city_area['Area'].to_list()
area_list = area_all_city + area_selected_city
type_list_area = ['All' for _ in range(len(area_all_city))] + ['Selected' for _ in range(len(area_selected_city))]
area = pd.DataFrame({'Type':type_list_area, 'Area':area_list})

pop_all_city = all_city_pop['Population'].to_list()
pop_selected_city = selected_city_pop['Population'].to_list()
pop_list = pop_all_city + pop_selected_city
type_list_pop = ['All' for _ in range(len(pop_all_city))] + ['Selected' for _ in range(len(pop_selected_city))]
pop = pd.DataFrame({'Type':type_list_pop, 'Population':pop_list})

pop_den_all_city = all_city_pop_density['Density'].to_list()
pop_den_selected_city = selected_city_pop_density['Density'].to_list()
pop_den_list = pop_den_all_city + pop_den_selected_city
type_list_pop_den = ['All' for _ in range(len(pop_den_all_city))] + ['Selected' for _ in range(len(pop_den_selected_city))]
pop_den = pd.DataFrame({'Type':type_list_pop_den, 'Density':pop_den_list})


# plot
fig, axes = plt.subplots(ncols=3, nrows=1, figsize=(15,6))
sns.boxplot(data=area, x='Type',y='Area',ax=axes[0])
axes[0].grid()
axes[0].set_ylim(bottom=0,top=150)
axes[0].set_ylabel('Area',size=28)
axes[0].set_xlabel('',size=20)
axes[0].tick_params(axis='y', labelsize=24)
axes[0].tick_params(axis='x', labelsize=24)

sns.boxplot(data=pop, x='Type',y='Population',ax=axes[1])
t = axes[1].yaxis.get_offset_text()
t.set_size(20)
axes[1].grid()
axes[1].set_ylim(bottom=0,top=1e6)
axes[1].set_ylabel('Population',size=28)
axes[1].set_xlabel('',size=20)
axes[1].tick_params(axis='y', labelsize=24)
axes[1].tick_params(axis='x', labelsize=24)

sns.boxplot(data=pop_den, x='Type',y='Density',ax=axes[2])
axes[2].grid()
axes[2].set_ylim(bottom=0,top=9000)
axes[2].set_ylabel('Population Density',size=28)
axes[2].set_xlabel('',size=20)
axes[2].tick_params(axis='y', labelsize=24)
axes[2].tick_params(axis='x', labelsize=24)

plt.tight_layout()
plt.show()

from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13

street_view_features = pd.read_csv('./output/environmental_determinants/built_environment/street_view_features/street_view_features_all_msoa.csv')
street_view_features_city_agg = street_view_features.groupby(['CityName','CityCode']).mean().reset_index()

# plot vegetation
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=street_view_features, x='CityName',y='vegetation',order=street_view_features_city_agg.sort_values('vegetation',ascending=False)['CityName'].to_list())
ax1.set_ylabel('Vegetation',size=20)
ax1.set_xlabel('',size=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='x', labelsize=16,rotation=90)
plt.tight_layout()
plt.show()

# plot road
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=street_view_features, x='CityName',y='road',order=street_view_features_city_agg.sort_values('road',ascending=False)['CityName'].to_list())
ax1.set_ylabel('Road',size=20)
ax1.set_xlabel('',size=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='x', labelsize=16,rotation=90)
plt.tight_layout()
plt.show()

# plot sidewalk
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=street_view_features, x='CityName',y='sidewalk',order=street_view_features_city_agg.sort_values('sidewalk',ascending=False)['CityName'].to_list())
ax1.set_ylabel('Sidewalk',size=20)
ax1.set_xlabel('',size=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='x', labelsize=16,rotation=90)
plt.tight_layout()
plt.show()

# plot building
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
sns.boxplot(data=street_view_features, x='CityName',y='building',order=street_view_features_city_agg.sort_values('building',ascending=False)['CityName'].to_list())
ax1.set_ylabel('Building',size=20)
ax1.set_xlabel('',size=20)
ax1.tick_params(axis='y', labelsize=20)
ax1.tick_params(axis='x', labelsize=16,rotation=90)
plt.tight_layout()
plt.show()
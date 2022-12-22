from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from scipy import stats
import geopandas as gpd
sns.set_theme(style="white", palette=None)

plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13

street_view_featuress = pd.read_csv('./output/environmental_determinants/built_environment/street_view_features/street_view_features_msoa.csv')
street_view_featuress_city_agg = street_view_featuress.groupby(['CityName','CityCode']).median().reset_index()

###########################################################################
# Box plot
fig, axes = plt.subplots(ncols=1, nrows=2, figsize=(8,10))

msoa_boundary = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson',driver='geojson')
birmingham_boundary = msoa_boundary.loc[msoa_boundary['CityName']=='Birmingham']

# plot vegetation
sns.boxplot(data=street_view_featuress, x='CityName',y='vegetation',order=street_view_featuress_city_agg.sort_values('vegetation',ascending=False)['CityName'].to_list(),ax=axes[0])
axes[0].set_ylabel('Vegetation',size=24)
axes[0].set_xlabel('',size=20)
axes[0].set_ylim(bottom=0)
axes[0].tick_params(axis='y', labelsize=20)
axes[0].tick_params(axis='x', labelsize=16,rotation=90)
axes[0].grid()


sns.boxplot(data=street_view_featuress, x='CityName',y='sidewalk',order=street_view_featuress_city_agg.sort_values('sidewalk',ascending=False)['CityName'].to_list(),ax=axes[1])
axes[1].set_ylabel('Sidewalk',size=24)
axes[1].set_xlabel('',size=20)
axes[1].set_ylim(bottom=0)
axes[1].tick_params(axis='y', labelsize=20)
axes[1].tick_params(axis='x', labelsize=16,rotation=90)
axes[1].grid()

plt.tight_layout()
# plt.show()
plt.savefig('vegetation_sidewalk_box.pdf',dpi=300)

###########################################################################
# geo plot
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(8,6))
vegetation = street_view_featuress[['MSOACode','vegetation']]
birmingham_vegetation = birmingham_boundary.merge(vegetation,left_on='MSOACode',right_on='MSOACode', how='left')
birmingham_vegetation.to_crs(4326).plot(ax=ax1,column='vegetation',cmap='Greens',legend=True)
ax1.axis('off')
# cbar = ax1.collections[0].colorbar
# cbar.ax1.tick_params(labelsize=20)
plt.show()

fig, ax2 = plt.subplots(ncols=1, nrows=1, figsize=(8,6))
vegetation = street_view_featuress[['MSOACode','sidewalk']]
birmingham_vegetation = birmingham_boundary.merge(vegetation,left_on='MSOACode',right_on='MSOACode', how='left')
birmingham_vegetation.to_crs(4326).plot(ax=ax2,column='sidewalk',cmap='Blues',legend=True)
ax2.axis('off')
# cbar = ax1.collections[0].colorbar
# cbar.ax1.tick_params(labelsize=20)
plt.show()
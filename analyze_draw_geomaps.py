from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
import geopandas as gpd
# import geoplot as gplt

plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13

# draw birmingham MSOA grid map
msoa_boundary = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson',driver='geojson')
birmingham_boundary = msoa_boundary.loc[msoa_boundary['CityName']=='Birmingham']
fig, ax1 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
birmingham_boundary.geometry.plot(ax=ax1,facecolor='grey',edgecolor='white',alpha=0.8)
# albers_proj = '+proj=aea +lat_1=25 +lat_2=47 +lon_0=105'
# birmingham_boundary.geometry.to_crs(albers_proj).plot(ax=ax1,facecolor='grey',edgecolor='white',alpha=0.8)
ax1.axis('off')
plt.show()




# draw all selected MSOA grid map
fig, ax2 = plt.subplots(ncols=1, nrows=1, figsize=(10,6))
UK_boundary = gpd.read_file('./UK_boundary/Countries_(December_2021)_UK_BUC.geojson',driver='geojson')
UK_boundary.geometry.plot(ax=ax2,facecolor='grey',edgecolor='white',alpha=0.8)
msoa_boundary = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson',driver='geojson')
msoa_boundary.geometry.plot(ax=ax2,facecolor='#3988c1',edgecolor='#3988c1',alpha=0.8)
# albers_proj = '+proj=aea +lat_1=25 +lat_2=47 +lon_0=105'
# birmingham_boundary.geometry.to_crs(albers_proj).plot(ax=ax1,facecolor='grey',edgecolor='white',alpha=0.8)
ax2.axis('off')
plt.show()
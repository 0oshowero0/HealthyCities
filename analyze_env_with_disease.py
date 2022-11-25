from datetime import datetime
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import r2_score
from scipy import stats

sns.set_theme(style="white", palette=None)

plt.rcParams['ps.fonttype'] = 42
plt.rcParams['pdf.fonttype'] = 42
plt.rcParams['font.family'] = ['Arial']
plt.rcParams['xtick.labelsize']=13
plt.rcParams['ytick.labelsize']=13


########################################################
# walkability and dementia
walkability = pd.read_csv('./output/environmental_determinants/built_environment/walkability/walkability_msoa.csv')[['MSOACode','Walkability']]
dementia = pd.read_csv('./output/health_outcome/physical_health/dementia/dementia_prescribing_msoa.csv')[['MSOACode','PerCitizenCost']]
dementia = dementia.groupby('MSOACode').sum().reset_index()

dementia = dementia.merge(walkability,left_on='MSOACode',right_on='MSOACode',how='inner')

r2 = r2_score(dementia['Walkability'].to_list(), dementia['PerCitizenCost'].to_list())
pearson_corr = stats.pearsonr(dementia['Walkability'].to_list(), dementia['PerCitizenCost'].to_list())
spearman_corr = stats.spearmanr(dementia['Walkability'].to_list(), dementia['PerCitizenCost'].to_list())

fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(8,6))
sns.regplot(data=dementia, x='Walkability',y='PerCitizenCost',fit_reg=False,ci=95,ax=axes,scatter_kws={'s':20},line_kws={'color':'r', 'linewidth':2})
axes.grid()
axes.set_xlim(xmax=4)
axes.set_ylabel('Per Citizen Cost of Dementia',size=24)
axes.set_xlabel('Walkability Score',size=24)
axes.tick_params(axis='y', labelsize=20)
axes.tick_params(axis='x', labelsize=20)
xlim = axes.get_xlim()
ylim = axes.get_ylim()
axes.text((xlim[1]-xlim[0]) / 6*4 + xlim[0], (ylim[1]-ylim[0]) / 8 *7 + ylim[0],'Pearson R:'+"%(r2).3f"%{'r2':pearson_corr[0]},fontdict = {'size': 16, 'color': 'black'})
plt.tight_layout()
plt.show()

########################################################
# tobacco and asthma
tobacco = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/tobacco_availability_msoa.csv')[['MSOACode','Availability']]
asthma = pd.read_csv('./output/health_outcome/physical_health/asthma/asthma_prescribing_msoa.csv')[['MSOACode','PerCitizenCost']]
asthma = asthma.groupby('MSOACode').sum().reset_index()

asthma = asthma.merge(tobacco,left_on='MSOACode',right_on='MSOACode',how='inner')

r2 = r2_score(asthma['Availability'].to_list(), asthma['PerCitizenCost'].to_list())
pearson_corr = stats.pearsonr(asthma['Availability'].to_list(), asthma['PerCitizenCost'].to_list())
spearman_corr = stats.spearmanr(asthma['Availability'].to_list(), asthma['PerCitizenCost'].to_list())

fig, axes = plt.subplots(ncols=1, nrows=1, figsize=(8,6))
sns.regplot(data=asthma, x='Availability',y='PerCitizenCost',fit_reg=False,ci=95,ax=axes,scatter_kws={'s':20},line_kws={'color':'r', 'linewidth':2})
axes.grid()
# axes.set_xlim(xmax=4)
# axes.set_ylim(bottom=-2)
axes.set_ylabel('Per Citizen Cost of asthma',size=24)
axes.set_xlabel('Tobacco Availability',size=24)
axes.tick_params(axis='y', labelsize=20)
axes.tick_params(axis='x', labelsize=18)
xlim = axes.get_xlim()
ylim = axes.get_ylim()
axes.text((xlim[1]-xlim[0]) / 6*4 + xlim[0], (ylim[1]-ylim[0]) / 8 *7 + ylim[0],'Pearson R:'+"%(r2).3f"%{'r2':pearson_corr[0]},fontdict = {'size': 16, 'color': 'black'})
plt.tight_layout()
plt.show()

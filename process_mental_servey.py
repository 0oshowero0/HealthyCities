from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

OUTPUT_PATH = Path('./output/health_outcome/mental_health/mental_servey_data')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

city_lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
city_lut = city_lut[['RegionCode','RegionName']]
city_lut = city_lut.drop_duplicates()

def file_path():
    anxiety = Path('./mental_health_servey/WICH_Wellbeing_Wellbeing_Anxiety_all.csv')
    happiness = Path('./mental_health_servey/WICH_Wellbeing_Wellbeing_Happiness_all.csv')
    satisfaction = Path('./mental_health_servey/WICH_Wellbeing_Wellbeing_Life satisfaction_all.csv')
    self_worth = Path('./mental_health_servey/WICH_Wellbeing_Wellbeing_Self-worth_all.csv')
    lonely = Path('./mental_health_servey/WICH_Wellbeing_Loneliness_Often lonely_all.csv')

    data_dict = {'anxiety':anxiety, 'happiness':happiness, 'satisfaction':satisfaction, 'self_worth':self_worth, 'lonely':lonely}
    return data_dict


data_path = file_path()

#################################
# anxiety
anxiety_data = pd.read_csv(data_path['anxiety'])
anxiety_data = anxiety_data.loc[anxiety_data['Category Type'] == 'Region']
anxiety_data = anxiety_data[['Time period','Category','Value','Lower confidence interval', 'Upper confidence interval']]
anxiety_data = anxiety_data.merge(city_lut, left_on='Category', right_on='RegionName').drop(labels=['Category'],axis=1)
anxiety_data = anxiety_data.rename(columns={'Time period':'Time','Lower confidence interval':'LowerConfidenceInterval','Upper confidence interval':'UpperConfidenceInterval'})
anxiety_data['Time'] = anxiety_data['Time'].map(lambda x:datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))
anxiety_data = anxiety_data.sort_values(by=['Time','RegionCode'],ascending=True)
anxiety_data.to_csv(OUTPUT_PATH.joinpath('anxiety.csv'),index=False,sep=',')


#################################
# happiness
happiness_data = pd.read_csv(data_path['happiness'])
happiness_data = happiness_data.loc[happiness_data['Category Type'] == 'Region']
happiness_data = happiness_data[['Time period','Category','Value','Lower confidence interval', 'Upper confidence interval']]
happiness_data = happiness_data.merge(city_lut, left_on='Category', right_on='RegionName').drop(labels=['Category'],axis=1)
happiness_data = happiness_data.rename(columns={'Time period':'Time','Lower confidence interval':'LowerConfidenceInterval','Upper confidence interval':'UpperConfidenceInterval'})
happiness_data['Time'] = happiness_data['Time'].map(lambda x:datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))
happiness_data = happiness_data.sort_values(by=['Time','RegionCode'],ascending=True)
happiness_data.to_csv(OUTPUT_PATH.joinpath('happiness.csv'),index=False,sep=',')

#################################
# satisfaction
satisfaction_data = pd.read_csv(data_path['satisfaction'])
satisfaction_data = satisfaction_data.loc[satisfaction_data['Category Type'] == 'Region']
satisfaction_data = satisfaction_data[['Time period','Category','Value','Lower confidence interval', 'Upper confidence interval']]
satisfaction_data = satisfaction_data.merge(city_lut, left_on='Category', right_on='RegionName').drop(labels=['Category'],axis=1)
satisfaction_data = satisfaction_data.rename(columns={'Time period':'Time','Lower confidence interval':'LowerConfidenceInterval','Upper confidence interval':'UpperConfidenceInterval'})
satisfaction_data['Time'] = satisfaction_data['Time'].map(lambda x:datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))
satisfaction_data = satisfaction_data.sort_values(by=['Time','RegionCode'],ascending=True)
satisfaction_data.to_csv(OUTPUT_PATH.joinpath('life_satisfaction.csv'),index=False,sep=',')

#################################
# self_worth
self_worth_data = pd.read_csv(data_path['self_worth'])
self_worth_data = self_worth_data.loc[self_worth_data['Category Type'] == 'Region']
self_worth_data = self_worth_data[['Time period','Category','Value','Lower confidence interval', 'Upper confidence interval']]
self_worth_data = self_worth_data.merge(city_lut, left_on='Category', right_on='RegionName').drop(labels=['Category'],axis=1)
self_worth_data = self_worth_data.rename(columns={'Time period':'Time','Lower confidence interval':'LowerConfidenceInterval','Upper confidence interval':'UpperConfidenceInterval'})
self_worth_data['Time'] = self_worth_data['Time'].map(lambda x:datetime.strptime(x, '%d/%m/%Y').strftime('%Y-%m-%d'))
self_worth_data = self_worth_data.sort_values(by=['Time','RegionCode'],ascending=True)
self_worth_data.to_csv(OUTPUT_PATH.joinpath('self_worth.csv'),index=False,sep=',')

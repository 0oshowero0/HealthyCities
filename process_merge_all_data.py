import numpy as np
import pandas as pd
import geopandas as gpd
from pathlib import Path

###################################################
# Generate Dataset Framework
TopCategory = []  # 'HealthOutcome', 'EnvironmentalDeterminants'
SecondCategory = [] # 'PhysicalHealth', 'MentalHealth', 'LifeExpectancy', 'NaturalEnvironment', 'BehaviourEnvironment','BuiltEnvironment','BasicStatistics'
ThirdCategory = [] 
CityCode = []
CityName = []
MSOACode = []
MSOAName = []
Time = [] # 'None', 'xxxx-xx-xx' (year-month-day for time series data)
Key = []
Value = []
###################################################
# HealthOutcome - PhysicalHealth
# obesity
tmp = pd.read_csv('./output/health_outcome/physical_health/obesity/obesity_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('ObesityExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('ObesityExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/obesity/obesity_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('ObesityExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('ObesityExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# hypertension
tmp = pd.read_csv('./output/health_outcome/physical_health/hypertension/hypertension_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HypertensionExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HypertensionExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/hypertension/hypertension_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HypertensionExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HypertensionExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# hyperlipidemia
tmp = pd.read_csv('./output/health_outcome/physical_health/hyperlipidemia/hyperlipidemia_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HyperlipidemiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HyperlipidemiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/hyperlipidemia/hyperlipidemia_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HyperlipidemiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('HyperlipidemiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# diabetes
tmp = pd.read_csv('./output/health_outcome/physical_health/diabetes/diabetes_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DiabetesExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DiabetesExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/diabetes/diabetes_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DiabetesExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DiabetesExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# dementia
tmp = pd.read_csv('./output/health_outcome/physical_health/dementia/dementia_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DementiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DementiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/dementia/dementia_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DementiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('DementiaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# cancer
tmp = pd.read_csv('./output/health_outcome/physical_health/cancer/cancer_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('CancerExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('CancerExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/cancer/cancer_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('CancerExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('CancerExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# asthma
tmp = pd.read_csv('./output/health_outcome/physical_health/asthma/asthma_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('AsthmaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('AsthmaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/physical_health/asthma/asthma_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('AsthmaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('AsthmaExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

# covid
tmp = pd.read_csv('./output/health_outcome/physical_health/covid_data/COVID_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('COVID')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('NewCasesBySpecimenDateRollingSum')
    Value.append(row['NewCasesBySpecimenDateRollingSum'])

tmp = pd.read_csv('./output/health_outcome/physical_health/covid_data/COVID_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('PhysicalHealth')
    ThirdCategory.append('COVID')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('NewCasesBySpecimenDateRollingSum')
    Value.append(row['NewCasesBySpecimenDateRollingSum'])

###################################################
# HealthOutcome - MentalHealth
# mental health
tmp = pd.read_csv('./output/health_outcome/mental_health/mental_prescribing_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('MentalHealth')
    ThirdCategory.append('MentalHealthExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('MentalHealth')
    ThirdCategory.append('MentalHealthExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

tmp = pd.read_csv('./output/health_outcome/mental_health/mental_prescribing_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('MentalHealth')
    ThirdCategory.append('MentalHealthExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('ActualCost')
    Value.append(row['ActualCost'])

    TopCategory.append('HealthOutcome')
    SecondCategory.append('MentalHealth')
    ThirdCategory.append('MentalHealthExpenditure')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Date'])
    Key.append('PerCitizenCost')
    Value.append(row['PerCitizenCost'])

###################################################
# HealthOutcome - LifeExpectancy
# life expectancy
tmp = pd.read_csv('./output/health_outcome/life_expectancy/life_expectancy_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('LifeExpectancy')
    ThirdCategory.append('LifeExpectancy')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append(row['Gender'])
    Value.append(row['Value'])

# healthy life expectancy
tmp = pd.read_csv('./output/health_outcome/life_expectancy/healthy_life_expectancy_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('HealthOutcome')
    SecondCategory.append('LifeExpectancy')
    ThirdCategory.append('HealthyLifeExpectancy')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append(row['Gender'])
    Value.append(row['Value'])


###################################################
# EnvironmentalDeterminants - NaturalEnvironment
# weather - windspeed
tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/wind_speed_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('WindSpeed')
    Value.append(row['WindSpeed'])

tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/wind_speed_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('WindSpeed')
    Value.append(row['WindSpeed'])


# weather - temperature_min
tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/tempetature_min_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('TemperatureMin')
    Value.append(row['TemperatureMin'])

tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/tempetature_min_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('TemperatureMin')
    Value.append(row['TemperatureMin'])


# weather - temperature_max
tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/tempetature_max_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('TemperatureMax')
    Value.append(row['TemperatureMax'])

tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/tempetature_max_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('TemperatureMax')
    Value.append(row['TemperatureMax'])

# weather - sunshine hours
tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/sunshine_hours_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('SunshineHours')
    Value.append(row['SunshineHours'])

tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/sunshine_hours_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('SunshineHours')
    Value.append(row['SunshineHours'])

# weather - relative humidity
tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/relative_humidity_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('RelativeHumidity')
    Value.append(row['RelativeHumidity'])

tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/relative_humidity_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('RelativeHumidity')
    Value.append(row['RelativeHumidity'])

# weather - rainfall
tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/rainfall_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Rainfall')
    Value.append(row['Rainfall'])

tmp = pd.read_csv('./output/environmental_determinants/natural_environment/weather/rainfall_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('NaturalEnvironment')
    ThirdCategory.append('Weather')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Rainfall')
    Value.append(row['Rainfall'])


# air quality
air_quality_locs = Path('./output/environmental_determinants/natural_environment/air_quality/air_quality_data/').glob('*.csv')
air_quality_locs = [i for i in air_quality_locs]
lut = pd.read_csv('./city_defination_and_LUTs/city_look_up_table.csv')
for i in air_quality_locs:
    city_code = i.stem
    city_name = str(lut.loc[lut['CityCode']==city_code]['CityName'].iloc[0])
    tmp = pd.read_csv(i)
    for _, row in tmp.iterrows():
        for j in range(len(row) -1):
            TopCategory.append('EnvironmentalDeterminants')
            SecondCategory.append('NaturalEnvironment')
            ThirdCategory.append('AirQuality')
            CityCode.append(city_code)
            CityName.append(city_name)
            MSOACode.append('None')
            MSOAName.append('None')
            Time.append(row['Date'])
            Key.append(row.index[j + 1]) 
            if row[row.index[j + 1]] == 'No data':
                Value.append('None')
            else:
                Value.append(row[row.index[j + 1]])


###################################################
# EnvironmentalDeterminants - BehaviourEnvironment
# tobacco
tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/tobacco_availability_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('TobaccoAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/tobacco_availability_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('TobaccoAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

# physical exercise
tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/physical_exercise_availability_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('PhysicalExerciseAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/physical_exercise_availability_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('PhysicalExerciseAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])


# health
tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/health_availability_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('HealthAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/health_availability_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('HealthAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

# alcohol
tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/alcohol_availability_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('AlcoholAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

tmp = pd.read_csv('./output/environmental_determinants/health_related_behaviour_environment/alcohol_availability_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BehaviourEnvironment')
    ThirdCategory.append('AlcoholAvailability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Availability')
    Value.append(row['Availability'])

###################################################
# EnvironmentalDeterminants - BuiltEnvironment
# walkability
tmp = pd.read_csv('./output/environmental_determinants/built_environment/walkability/walkability_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('Walkability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Walkability')
    Value.append(row['Walkability'])

tmp = pd.read_csv('./output/environmental_determinants/built_environment/walkability/walkability_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('Walkability')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Walkability')
    Value.append(row['Walkability'])

# road density - walking
tmp = pd.read_csv('./output/environmental_determinants/built_environment/road_density/walking_road_density_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('RoadDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('WalkingRoadDensity')
    Value.append(row['RoadDensity'])

tmp = pd.read_csv('./output/environmental_determinants/built_environment/road_density/walking_road_density_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('RoadDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('WalkingRoadDensity')
    Value.append(row['RoadDensity'])


# road density - driving
tmp = pd.read_csv('./output/environmental_determinants/built_environment/road_density/driving_road_density_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('RoadDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('DrivingRoadDensity')
    Value.append(row['RoadDensity'])

tmp = pd.read_csv('./output/environmental_determinants/built_environment/road_density/driving_road_density_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('RoadDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('DrivingRoadDensity')
    Value.append(row['RoadDensity'])


# road density - cycling
tmp = pd.read_csv('./output/environmental_determinants/built_environment/road_density/cycling_road_density_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('RoadDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('CyclingRoadDensity')
    Value.append(row['RoadDensity'])

tmp = pd.read_csv('./output/environmental_determinants/built_environment/road_density/cycling_road_density_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('RoadDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('CyclingRoadDensity')
    Value.append(row['RoadDensity'])

# house price
tmp = pd.read_csv('./output/environmental_determinants/built_environment/house_price/house_price_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('HousePrice')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append(row['Time'])
    Key.append(row['Aggregation'])
    Value.append(row['Price'])

tmp = pd.read_csv('./output/environmental_determinants/built_environment/house_price/house_price_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('HousePrice')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append(row['Time'])
    Key.append(row['Aggregation'])
    Value.append(row['Price'])

# building density
tmp = pd.read_csv('./output/environmental_determinants/built_environment/building_density/building_density_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('BuildingDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('BuildingDensity')
    Value.append(row['BuildingDensity'])

tmp = pd.read_csv('./output/environmental_determinants/built_environment/building_density/building_density_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BuiltEnvironment')
    ThirdCategory.append('BuildingDensity')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('BuildingDensity')
    Value.append(row['BuildingDensity'])

# street_view
tmp = pd.read_csv('./output/environmental_determinants/built_environment/street_view_features/street_view_features_msoa.csv')
for _, row in tmp.iterrows():
    for j in range(len(row) - 4):
        TopCategory.append('EnvironmentalDeterminants')
        SecondCategory.append('BuiltEnvironment')
        ThirdCategory.append('StreetViewFeatures')
        CityCode.append(row['CityCode'])
        CityName.append(row['CityName'])
        MSOACode.append(row['MSOACode'])
        MSOAName.append(row['MSOAName'])
        Time.append('None')
        Key.append(row.index[j + 4]) 
        Value.append(row[row.index[j + 4]])


tmp = pd.read_csv('./output/environmental_determinants/built_environment/street_view_features/street_view_features_city.csv')
for _, row in tmp.iterrows():
    for j in range(len(row) - 2):
        TopCategory.append('EnvironmentalDeterminants')
        SecondCategory.append('BuiltEnvironment')
        ThirdCategory.append('StreetViewFeatures')
        CityCode.append(row['CityCode'])
        CityName.append(row['CityName'])
        MSOACode.append('None')
        MSOAName.append('None')
        Time.append('None')
        Key.append(row.index[j + 2]) 
        Value.append(row[row.index[j + 2]])

# satellite view
tmp = pd.read_csv('./output/environmental_determinants/built_environment/satellite_view_features/satellite_view_features_msoa.csv')
for _, row in tmp.iterrows():
    for j in range(len(row) - 4):
        TopCategory.append('EnvironmentalDeterminants')
        SecondCategory.append('BuiltEnvironment')
        ThirdCategory.append('SatelliteViewFeatures')
        CityCode.append(row['CityCode'])
        CityName.append(row['CityName'])
        MSOACode.append(row['MSOACode'])
        MSOAName.append(row['MSOAName'])
        Time.append('None')
        Key.append(row.index[j + 4]) 
        Value.append(row[row.index[j + 4]])


tmp = pd.read_csv('./output/environmental_determinants/built_environment/satellite_view_features/satellite_view_features_city.csv')
for _, row in tmp.iterrows():
    for j in range(len(row) - 2):
        TopCategory.append('EnvironmentalDeterminants')
        SecondCategory.append('BuiltEnvironment')
        ThirdCategory.append('SatelliteViewFeatures')
        CityCode.append(row['CityCode'])
        CityName.append(row['CityName'])
        MSOACode.append('None')
        MSOAName.append('None')
        Time.append('None')
        Key.append(row.index[j + 2]) 
        Value.append(row[row.index[j + 2]])

###################################################
# EnvironmentalDeterminants - BasicStatistics
# population
tmp = pd.read_csv('./output/environmental_determinants/basic_statistics/population/population_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Population')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('PopulationDensity')
    Value.append(row['PopulationDensity'])

    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Population')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Population')
    Value.append(row['Population'])


tmp = pd.read_csv('./output/environmental_determinants/basic_statistics/population/population_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Population')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('PopulationDensity')
    Value.append(row['PopulationDensity'])

    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Population')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Population')
    Value.append(row['Population'])

# area
tmp = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_msoa.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Area')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Area')
    Value.append(row['Area'])

tmp = pd.read_csv('./output/environmental_determinants/basic_statistics/area/area_city.csv')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Area')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Area')
    Value.append(row['Area'])


# centroid
tmp = gpd.read_file('./output/environmental_determinants/basic_statistics/centroid/geographical_centroid_msoa.geojson', driver='geojson')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Centroid')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('GeographicalCentroid')
    Value.append(row['geometry'])

tmp = gpd.read_file('./output/environmental_determinants/basic_statistics/centroid/geographical_centroid_city.geojson', driver='geojson')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Centroid')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('GeographicalCentroid')
    Value.append(row['geometry'])


# boundary
tmp = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_msoa.geojson', driver='geojson')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Boundary')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append(row['MSOACode'])
    MSOAName.append(row['MSOAName'])
    Time.append('None')
    Key.append('Boundary')
    Value.append(row['geometry'])

tmp = gpd.read_file('./output/environmental_determinants/basic_statistics/boundary/boundary_city.geojson', driver='geojson')
for _, row in tmp.iterrows():
    TopCategory.append('EnvironmentalDeterminants')
    SecondCategory.append('BasicStatistics')
    ThirdCategory.append('Boundary')
    CityCode.append(row['CityCode'])
    CityName.append(row['CityName'])
    MSOACode.append('None')
    MSOAName.append('None')
    Time.append('None')
    Key.append('Boundary')
    Value.append(row['geometry'])


data = pd.DataFrame({'TopCategory':TopCategory,'SecondCategory':SecondCategory,\
                     'ThirdCategory':ThirdCategory,'CityCode':CityCode,'CityName':CityName,\
                     'MSOACode':MSOACode,'MSOAName':MSOAName,'Time':Time,'Key':Key,'Value':Value})
data.to_csv('./output/all_data.csv',index=False)

# data = gpd.DataFrame({'TopCategory':TopCategory,'SecondCategory':SecondCategory,\
#                      'ThirdCategory':ThirdCategory,'CityCode':CityCode,'CityName':CityName,\
#                      'MSOACode':MSOACode,'MSOAName':MSOAName,'Time':Time,'Key':Key,'Value':Value})
# data.to_file(OUTPUT_PATH.joinpath('boundary_msoa.geojson'), driver='GeoJSON')
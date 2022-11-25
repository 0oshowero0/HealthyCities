from datetime import datetime
import numpy as np
import pandas as pd
from pathlib import Path

INPUT_PATH = Path('./temp_output/air_quality_data')
OUTPUT_PATH = Path('./output/environmental_determinants/natural_environment/air_quality/air_quality_data')
OUTPUT_PATH.mkdir(exist_ok=True, parents=True)

for fp in sorted([i for i in INPUT_PATH.glob('*.csv')]):
    data = pd.read_csv(fp)
    data['Date'] = data['Date'].map(lambda x: datetime.strptime(x, '%Y/%m/%d').strftime('%Y-%m-%d'))

    data = data.loc[data['Date']<'2022-09-01']
    data.to_csv(OUTPUT_PATH.joinpath(fp.name),index=False)

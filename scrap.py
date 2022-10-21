import os
import pandas as pd
import numpy as np


os.listdir('.\input')

RECEIPTS_PATH = os.path.abspath(os.path.join("", 'input', 'Mixed_Beverage_Gross_Receipts.csv'))

df = pd.read_csv(RECEIPTS_PATH)

# Convert to TimeStamps
df['Responsibility Begin Date'] = pd.to_datetime(df['Responsibility Begin Date'])
df['Responsibility End Date'] = pd.to_datetime(df['Responsibility End Date'])
df['Obligation End Date'] = pd.to_datetime(df['Obligation End Date'])
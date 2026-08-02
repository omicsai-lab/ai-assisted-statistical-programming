import os
import pandas as pd

clinic = pd.read_csv("data_raw/clinic_visits.csv")
print(os.getcwd())
print(clinic.shape)
print(clinic.columns.tolist())
print(clinic.head())
print(clinic.info())
print(clinic.dtypes)
print(clinic.isna().sum())

import subprocess
import sys
import numpy as np
import pandas as pd
import statsmodels.formula.api as smf

try:
    clean_clinic = pd.read_csv("output/clean_clinic.csv")
except FileNotFoundError:
    subprocess.run([sys.executable, "scripts/python/ch09_clean_recode.py"], check=True)
    clean_clinic = pd.read_csv("output/clean_clinic.csv")

model1 = smf.ols("followup ~ baseline", data=clean_clinic).fit()
print(model1.summary())
print(model1.conf_int())

model2 = smf.ols("followup ~ baseline + age + group_clean", data=clean_clinic).fit()
print(model2.summary())
print(model2.conf_int())

clean_clinic["improved"] = clean_clinic["change"].gt(0).astype("boolean")
clean_clinic.loc[clean_clinic["change"].isna(), "improved"] = pd.NA
logit_data = clean_clinic.dropna(subset=["improved", "age", "group_clean"]).copy()
logit_data["improved"] = logit_data["improved"].astype(int)
# This tiny synthetic dataset can trigger warnings; it is included to show syntax.
if logit_data["improved"].nunique() == 2:
    logit_model = smf.logit("improved ~ age + group_clean", data=logit_data).fit(disp=False)
    print(logit_model.summary())
    print(np.exp(logit_model.params))
    print(np.exp(logit_model.conf_int()))
else:
    print("Logistic regression skipped because only one outcome class is present.")

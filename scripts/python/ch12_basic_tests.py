import subprocess
import sys
import pandas as pd
from scipy import stats
from scipy.stats import chi2_contingency, fisher_exact

try:
    clean_clinic = pd.read_csv("output/clean_clinic.csv")
except FileNotFoundError:
    subprocess.run([sys.executable, "scripts/python/ch09_clean_recode.py"], check=True)
    clean_clinic = pd.read_csv("output/clean_clinic.csv")

control = clean_clinic.loc[clean_clinic["group_clean"] == "control", "change"].dropna()
treatment = clean_clinic.loc[clean_clinic["group_clean"] == "treatment", "change"].dropna()
print(control.describe())
print(treatment.describe())
print(stats.ttest_ind(treatment, control, equal_var=False))

clean_clinic["improved"] = clean_clinic["change"].gt(0).astype("boolean")
clean_clinic.loc[clean_clinic["change"].isna(), "improved"] = pd.NA
improved_display = clean_clinic["improved"].astype("string").fillna("missing")
print(pd.crosstab(clean_clinic["group_clean"], improved_display))

test_data = clean_clinic.dropna(subset=["group_clean", "improved"])
tab = pd.crosstab(test_data["group_clean"], test_data["improved"])
print(tab)
chi2, p, dof, expected = chi2_contingency(tab)
print({"chi2": chi2, "p_value": p, "dof": dof})
print(expected)
if tab.shape == (2, 2):
    odds_ratio, fisher_p = fisher_exact(tab)
    print({"odds_ratio": odds_ratio, "fisher_p": fisher_p})

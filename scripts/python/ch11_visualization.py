import subprocess
import sys
import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt

try:
    clean_clinic = pd.read_csv("output/clean_clinic.csv")
except FileNotFoundError:
    subprocess.run([sys.executable, "scripts/python/ch09_clean_recode.py"], check=True)
    clean_clinic = pd.read_csv("output/clean_clinic.csv")

plt.figure()
plt.hist(clean_clinic["age"].dropna(), bins=5)
plt.title("Distribution of age")
plt.xlabel("Age")
plt.ylabel("Number of observations")
plt.tight_layout()
plt.savefig("output/figure_age_histogram.png", dpi=300, bbox_inches="tight")
plt.close()

groups = [
    clean_clinic.loc[clean_clinic["group_clean"] == "control", "change"].dropna(),
    clean_clinic.loc[clean_clinic["group_clean"] == "treatment", "change"].dropna(),
]
plt.figure()
plt.boxplot(groups, labels=["control", "treatment"])
plt.title("Change score by group")
plt.xlabel("Group")
plt.ylabel("Follow-up minus baseline")
plt.tight_layout()
plt.savefig("output/figure_change_by_group.png", dpi=300, bbox_inches="tight")
plt.close()
print("Saved figures to output/.")

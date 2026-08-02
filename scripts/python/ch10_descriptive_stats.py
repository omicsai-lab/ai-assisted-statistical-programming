import pandas as pd

try:
    clean_clinic = pd.read_csv("output/clean_clinic.csv")
except FileNotFoundError:
    import subprocess, sys
    subprocess.run([sys.executable, "scripts/python/ch09_clean_recode.py"], check=True)
    clean_clinic = pd.read_csv("output/clean_clinic.csv")

summary = clean_clinic.groupby("group_clean").agg(
    n=("id", "size"),
    missing_age=("age", lambda x: x.isna().sum()),
    mean_age=("age", "mean"),
    median_age=("age", "median"),
    sd_age=("age", "std"),
    mean_change=("change", "mean"),
    median_change=("change", "median"),
).reset_index()
print(summary)
summary.to_csv("output/table1_group_summary.csv", index=False)

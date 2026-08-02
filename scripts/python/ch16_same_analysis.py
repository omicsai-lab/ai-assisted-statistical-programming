import pandas as pd
import matplotlib
matplotlib.use("Agg")
import matplotlib.pyplot as plt
import statsmodels.formula.api as smf

wellness = pd.read_csv("data_raw/wellness.csv")
print(wellness.shape)
print(wellness.info())
print(wellness.describe(include="all"))
print(wellness.isna().sum())
print(wellness["program"].value_counts(dropna=False))

wellness_clean = wellness.copy()
wellness_clean["program"] = pd.Categorical(wellness_clean["program"], categories=["no", "yes"])
wellness_clean["change"] = wellness_clean["followup"] - wellness_clean["baseline"]
wellness_clean["has_followup"] = wellness_clean["followup"].notna()

print(pd.Series({
    "n_total": len(wellness_clean),
    "missing_age": wellness_clean["age"].isna().sum(),
    "missing_followup": wellness_clean["followup"].isna().sum(),
    "missing_change": wellness_clean["change"].isna().sum(),
}))

summary_by_program = wellness_clean.groupby("program").agg(
    n=("id", "size"),
    n_change=("change", lambda x: x.notna().sum()),
    mean_age=("age", "mean"),
    mean_baseline=("baseline", "mean"),
    mean_change=("change", "mean"),
    sd_change=("change", "std"),
).reset_index()
print(summary_by_program)
summary_by_program.to_csv("output/wellness_summary_by_program.csv", index=False)

groups = [
    wellness_clean.loc[wellness_clean["program"] == "no", "change"].dropna(),
    wellness_clean.loc[wellness_clean["program"] == "yes", "change"].dropna(),
]
plt.figure()
plt.boxplot(groups, labels=["no", "yes"])
plt.title("Change score by program participation")
plt.xlabel("Program participation")
plt.ylabel("Follow-up minus baseline")
plt.tight_layout()
plt.savefig("output/wellness_change_by_program.png", dpi=300, bbox_inches="tight")
plt.close()

model = smf.ols("change ~ program + baseline + age", data=wellness_clean).fit()
print(model.summary())
print(model.conf_int())
print(int(model.nobs))

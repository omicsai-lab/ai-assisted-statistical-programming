import pandas as pd

clinic = pd.read_csv("data_raw/clinic_visits.csv")
recode_group = {
    "Control": "control",
    "control": "control",
    "Treatment": "treatment",
    "treat": "treatment",
}

print(clinic["group"].value_counts(dropna=False))
clean_clinic = clinic.copy()
clean_clinic["group_clean"] = clean_clinic["group"].map(recode_group)
clean_clinic["change"] = clean_clinic["followup"] - clean_clinic["baseline"]
clean_clinic["complete_outcome"] = clean_clinic["followup"].notna()
clean_clinic = clean_clinic[clean_clinic["group_clean"].notna()]
clean_clinic = clean_clinic[[
    "id", "group_clean", "age", "baseline",
    "followup", "change", "complete_outcome",
]]

print(clean_clinic)
print(clean_clinic.isna().sum())
print(clean_clinic["group_clean"].value_counts(dropna=False))
clean_clinic.to_csv("output/clean_clinic.csv", index=False)

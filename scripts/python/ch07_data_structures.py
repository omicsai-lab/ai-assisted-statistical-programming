import pandas as pd
import numpy as np

clinic = pd.DataFrame({
    "id": [1, 2, 3, 4, 5],
    "age": [34, 50, 29, 41, np.nan],
    "group": ["control", "treatment", "control", "treatment", "control"],
    "score": [7.2, 8.1, 6.9, 8.5, 7.0],
})

print(clinic)
print(clinic.info())
print(clinic.describe(include="all"))
print(clinic["age"].isna().sum())
clinic["group"] = clinic["group"].astype("category")
print(clinic["group"].cat.categories)

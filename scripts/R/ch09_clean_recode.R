library(readr)
library(dplyr)

clinic <- read_csv("data_raw/clinic_visits.csv", show_col_types = FALSE)
print(table(clinic$group, useNA = "ifany"))

clean_clinic <- clinic %>%
  mutate(
    group_clean = case_when(
      group %in% c("Control", "control") ~ "control",
      group %in% c("Treatment", "treat") ~ "treatment",
      TRUE ~ NA_character_
    ),
    change = followup - baseline,
    complete_outcome = !is.na(followup)
  ) %>%
  filter(!is.na(group_clean)) %>%
  select(id, group_clean, age, baseline, followup, change, complete_outcome)

print(clean_clinic)
print(colSums(is.na(clean_clinic)))
write_csv(clean_clinic, "output/clean_clinic.csv")

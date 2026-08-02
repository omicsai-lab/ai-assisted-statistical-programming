library(readr)
library(dplyr)

if (!file.exists("output/clean_clinic.csv")) {
  source("scripts/R/ch09_clean_recode.R")
}
clean_clinic <- read_csv("output/clean_clinic.csv", show_col_types = FALSE)

summary <- clean_clinic %>%
  group_by(group_clean) %>%
  summarise(
    n = n(),
    missing_age = sum(is.na(age)),
    mean_age = mean(age, na.rm = TRUE),
    median_age = median(age, na.rm = TRUE),
    sd_age = sd(age, na.rm = TRUE),
    mean_change = mean(change, na.rm = TRUE),
    median_change = median(change, na.rm = TRUE),
    .groups = "drop"
  )
print(summary)
write_csv(summary, "output/table1_group_summary.csv")

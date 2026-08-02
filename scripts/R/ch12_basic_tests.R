library(readr)
library(dplyr)

if (!file.exists("output/clean_clinic.csv")) {
  source("scripts/R/ch09_clean_recode.R")
}
clean_clinic <- read_csv("output/clean_clinic.csv", show_col_types = FALSE)

print(clean_clinic %>%
  group_by(group_clean) %>%
  summarise(n = sum(!is.na(change)), mean_change = mean(change, na.rm = TRUE), sd_change = sd(change, na.rm = TRUE), .groups = "drop"))
print(t.test(change ~ group_clean, data = clean_clinic))

clean_clinic <- clean_clinic %>%
  mutate(improved = case_when(
    is.na(change) ~ NA,
    change > 0 ~ TRUE,
    TRUE ~ FALSE
  ))
print(table(clean_clinic$group_clean, clean_clinic$improved, useNA = "ifany"))

test_data <- clean_clinic %>% filter(!is.na(group_clean), !is.na(improved))
tab <- table(test_data$group_clean, test_data$improved)
print(tab)
print(prop.table(tab, margin = 1))
print(chisq.test(tab))
print(fisher.test(tab))

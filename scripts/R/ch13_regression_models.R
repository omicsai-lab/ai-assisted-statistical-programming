library(readr)
library(dplyr)

if (!file.exists("output/clean_clinic.csv")) {
  source("scripts/R/ch09_clean_recode.R")
}
clean_clinic <- read_csv("output/clean_clinic.csv", show_col_types = FALSE)
clean_clinic$group_clean <- factor(clean_clinic$group_clean, levels = c("control", "treatment"))

model1 <- lm(followup ~ baseline, data = clean_clinic)
print(summary(model1))
print(confint(model1))

model2 <- lm(followup ~ baseline + age + group_clean, data = clean_clinic)
print(summary(model2))
print(confint(model2))

clean_clinic <- clean_clinic %>%
  mutate(improved = case_when(is.na(change) ~ NA, change > 0 ~ TRUE, TRUE ~ FALSE))
if (length(unique(na.omit(clean_clinic$improved))) == 2) {
  logit_model <- glm(improved ~ age + group_clean, data = clean_clinic, family = binomial)
  print(summary(logit_model))
  print(exp(coef(logit_model)))
  print(exp(confint(logit_model)))
}

library(readr)
library(dplyr)
library(ggplot2)

wellness <- read_csv("data_raw/wellness.csv", show_col_types = FALSE)
print(dim(wellness))
str(wellness)
print(summary(wellness))
print(colSums(is.na(wellness)))
print(table(wellness$program, useNA = "ifany"))

wellness_clean <- wellness %>%
  mutate(
    program = factor(program, levels = c("no", "yes")),
    change = followup - baseline,
    has_followup = !is.na(followup)
  )

print(wellness_clean %>%
  summarise(n_total = n(), missing_age = sum(is.na(age)), missing_followup = sum(is.na(followup)), missing_change = sum(is.na(change))))

summary_by_program <- wellness_clean %>%
  group_by(program) %>%
  summarise(
    n = n(),
    n_change = sum(!is.na(change)),
    mean_age = mean(age, na.rm = TRUE),
    mean_baseline = mean(baseline, na.rm = TRUE),
    mean_change = mean(change, na.rm = TRUE),
    sd_change = sd(change, na.rm = TRUE),
    .groups = "drop"
  )
print(summary_by_program)
write_csv(summary_by_program, "output/wellness_summary_by_program.csv")

p <- ggplot(wellness_clean, aes(x = program, y = change)) +
  geom_boxplot() +
  labs(title = "Change score by program participation", x = "Program participation", y = "Follow-up minus baseline")
ggsave("output/wellness_change_by_program.png", p, width = 6, height = 4, dpi = 300)

model <- lm(change ~ program + baseline + age, data = wellness_clean)
print(summary(model))
print(confint(model))
print(nobs(model))

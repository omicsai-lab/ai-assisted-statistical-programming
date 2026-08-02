library(readr)
library(ggplot2)

if (!file.exists("output/clean_clinic.csv")) {
  source("scripts/R/ch09_clean_recode.R")
}
clean_clinic <- read_csv("output/clean_clinic.csv", show_col_types = FALSE)

p1 <- ggplot(clean_clinic, aes(x = age)) +
  geom_histogram(binwidth = 10, boundary = 0) +
  labs(title = "Distribution of age", x = "Age", y = "Number of observations")
ggsave("output/figure_age_histogram.png", p1, width = 6, height = 4, dpi = 300)

p2 <- ggplot(clean_clinic, aes(x = group_clean, y = change)) +
  geom_boxplot() +
  labs(title = "Change score by group", x = "Group", y = "Follow-up minus baseline")
ggsave("output/figure_change_by_group.png", p2, width = 6, height = 4, dpi = 300)

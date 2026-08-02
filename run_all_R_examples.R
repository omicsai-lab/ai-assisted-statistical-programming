scripts <- c(
  "ch07_data_structures.R",
  "ch08_import_inspect.R",
  "ch09_clean_recode.R",
  "ch10_descriptive_stats.R",
  "ch11_visualization.R",
  "ch12_basic_tests.R",
  "ch13_regression_models.R",
  "ch16_same_analysis.R"
)
for (script in scripts) {
  cat("\n", paste(rep("=", 72), collapse = ""), "\n", sep = "")
  cat("Running ", script, "\n", sep = "")
  cat(paste(rep("=", 72), collapse = ""), "\n", sep = "")
  source(file.path("scripts", "R", script))
}

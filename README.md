# AI-Assisted Statistical Programming — Companion Code and Prompt Library

Companion repository for **AI-Assisted Statistical Programming: R and Python Workflows for Data Analysis, Debugging, and Verification** by **James Li**.

This repository is designed to support readers, students, and instructors who want to run the examples from the book, compare R and Python workflows, and reuse the prompt templates for AI-assisted statistical programming.

## What is included

- `scripts/R/` — R scripts for the main hands-on chapters.
- `scripts/python/` — Python scripts for the same workflows.
- `data_raw/` — small synthetic CSV datasets used in examples.
- `prompts/` — prompt templates for code generation, debugging, verification, R/Python translation, reproducibility review, and responsible AI use.
- `run_all_python_examples.py` — smoke-test runner for all Python examples.
- `run_all_R_examples.R` — smoke-test runner for all R examples.

The book manuscript, cover files, and full LaTeX source are not included here. This repository is for companion code, datasets, prompts, errata, and updates.

## Quick start: Python

From the repository root:

```bash
python -m venv .venv
source .venv/bin/activate      # Windows: .venv\Scripts\activate
python -m pip install --upgrade pip
python -m pip install -r requirements.txt
python run_all_python_examples.py
```

The scripts write generated files to `output/`.

## Quick start: R

From the repository root, install the required packages once:

```r
install.packages(c("readr", "dplyr", "ggplot2"))
```

Then run:

```bash
Rscript run_all_R_examples.R
```

The scripts write generated files to `output/`.

## Chapter-to-file map

| Book chapter | R script | Python script |
|---|---|---|
| Ch. 7 Data structures | `scripts/R/ch07_data_structures.R` | `scripts/python/ch07_data_structures.py` |
| Ch. 8 Import and inspect | `scripts/R/ch08_import_inspect.R` | `scripts/python/ch08_import_inspect.py` |
| Ch. 9 Clean and recode | `scripts/R/ch09_clean_recode.R` | `scripts/python/ch09_clean_recode.py` |
| Ch. 10 Descriptive statistics | `scripts/R/ch10_descriptive_stats.R` | `scripts/python/ch10_descriptive_stats.py` |
| Ch. 11 Visualization | `scripts/R/ch11_visualization.R` | `scripts/python/ch11_visualization.py` |
| Ch. 12 Basic tests | `scripts/R/ch12_basic_tests.R` | `scripts/python/ch12_basic_tests.py` |
| Ch. 13 Regression models | `scripts/R/ch13_regression_models.R` | `scripts/python/ch13_regression_models.py` |
| Ch. 16 Same analysis in R and Python | `scripts/R/ch16_same_analysis.R` | `scripts/python/ch16_same_analysis.py` |

## Recommended AI-assisted workflow

Use AI assistants as drafting and review tools, not as statistical authorities:

1. Ask for a small, explainable draft.
2. Inspect variable names, data types, row counts, and missing values.
3. Run the code in a clean session.
4. Debug one issue at a time.
5. Verify denominators, assumptions, and outputs.
6. Document what AI helped with and what you checked yourself.

See `prompts/` for reusable templates.

## Synthetic data only

The CSV files in `data_raw/` are synthetic teaching datasets. They are intentionally small so that readers can inspect the full data and understand each step.

## Citation

Suggested citation:

> Li, James. *AI-Assisted Statistical Programming: R and Python Workflows for Data Analysis, Debugging, and Verification*. Companion code and prompt library, Version 1.0.0.

A machine-readable citation file is included as `CITATION.cff`.

## Errata and updates

Use `ERRATA.md` to track corrections after publication. For a printed book, this repository is the easiest place to keep code corrections, clarification notes, and updated prompts synchronized with the book version.

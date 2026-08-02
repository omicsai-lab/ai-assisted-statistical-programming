# Checklists

## Before trusting AI-generated code

- Does the code use the correct dataset and variable names?
- Are missing values counted before analysis?
- Are filtering rules explicit?
- Are categorical reference levels clear?
- Are denominators shown for percentages?
- Does the model use the intended outcome and predictors?
- Did the code run from top to bottom in a clean session?
- Are outputs saved with clear filenames?
- Is the interpretation descriptive, associative, or causal? Is that wording justified?

## Before comparing R and Python outputs

- Did both languages read the same CSV file?
- Are missing values represented consistently?
- Are categories ordered the same way?
- Are row counts identical after filtering?
- Are grouped summaries using the same denominators?
- Are model formulas equivalent?
- Are confidence intervals and p-values produced by comparable methods?

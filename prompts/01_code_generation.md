# Code-generation prompts

## Cautious code-generation template

```text
I am learning statistical programming. My task is [describe task]. I am using [R/Python] with [packages]. My data object is named [object name]. The relevant variables are [names and types]. Please write beginner-friendly code that performs the task in small steps. Include checks for missing values, variable types, and row counts. Explain each line and list what I should verify before trusting the result.
```

## R summary example

```text
I am learning statistical programming. My data frame is named df. It has columns age, sex, group, and outcome. Please write simple R code to summarize age by group. Include counts, missing values, mean, median, and standard deviation. Explain each line.
```

## Python import-and-summary example

```text
I am learning Python pandas. Please write code to read a CSV file, check variable names, preview the first rows, summarize a numeric variable by group, and explain each step. Include missing-value checks.
```

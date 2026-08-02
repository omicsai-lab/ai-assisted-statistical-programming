# Verification and review prompts

## Skeptical statistical programming review

```text
Please act as a skeptical statistical programming reviewer. Review my code and output for wrong variable names, hidden missing-value decisions, unintended filtering, inappropriate method choice, unclear denominators, overclaiming, and reproducibility problems. Do not rewrite the code unless you identify a specific issue.
```

## Verify analysis logic

```text
My outcome variable is binary and my predictor is treatment group. I want to compare groups. What statistical approaches might be appropriate? Please explain the assumptions and what I should check before choosing a method.
```

## Reproducibility review

```text
Please review this script for reproducibility. Check whether it can run from top to bottom, whether file paths are relative, whether raw data are preserved, whether outputs are saved clearly, and whether important assumptions are documented.
```

# Model

**Modeling language: TODO (undecided: Python/scikit-learn or R/tidymodels).** One pipeline, one language.

## Rules
- Train/test split fixed by a random seed (TODO: seed).
- All preprocessing is fit on training data only (inside the pipeline).

## Planned steps
1. [ ] Define task and metric
2. [ ] Baseline model
3. [ ] Stronger models
4. [ ] Cross-validation (training data only) for tuning
5. [ ] One final test-set evaluation
6. [ ] Save the model (`model/artifacts/`, git-ignored)

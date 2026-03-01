Model Design
============

SPOP uses a Random Forest Regressor to predict daily GHI.

Why Random Forest?
------------------

- Handles nonlinear relationships
- Robust to noise
- Minimal preprocessing required
- Performs well on tabular weather data

Training Process
----------------

1. Train/test split
2. Model fitting
3. MAE evaluation
4. Artifact persistence

Evaluation Metrics
------------------

- Mean Absolute Error (MAE)
- Standard deviation of residuals

These metrics are used to generate forecast uncertainty bands.

Model Artifacts
---------------

Saved artifacts include:

- Trained model
- Evaluation metrics
- Feature configuration
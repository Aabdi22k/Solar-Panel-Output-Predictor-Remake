Feature Engineering
===================

Feature engineering transforms raw solar and weather data into model-ready inputs.

Cleaning
--------

- Missing value handling
- Type normalization
- Date parsing

Seasonality Encoding
--------------------

Cyclical encoding is applied using sine and cosine transforms:

- Day-of-year
- Seasonal cycles

This preserves periodic behavior without introducing discontinuities.

Derived Features
----------------

- Weather-based predictors
- Interaction terms
- Rolling or smoothed values

Engineering Philosophy
----------------------

Features are separated from model logic to ensure:

- Reproducibility
- Maintainability
- Clear experimentation boundaries
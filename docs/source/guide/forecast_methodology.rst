Forecast Methodology
====================

Forecasting involves two stages:

1. Predict GHI
2. Convert GHI to energy output

GHI Prediction
--------------

Weather forecasts are passed into the trained model to predict daily GHI.

Energy Conversion
-----------------

Energy output is computed using:

::

    Energy (kWh) = GHI × panel_area × efficiency

Where:

- GHI is predicted irradiance
- panel_area is user-configurable
- efficiency is panel efficiency (0–1)

Uncertainty Bands
-----------------

Uncertainty intervals are computed using:

- ± MAE
- ± 1 Standard Deviation
- ± 2 Standard Deviations
- ± 3 Standard Deviations

These provide approximate prediction confidence ranges.
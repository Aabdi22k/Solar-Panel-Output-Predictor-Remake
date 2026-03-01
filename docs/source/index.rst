Solar Panel Output Predictor (DPOP)
===================================

The Solar Panel Output Predictor (SPOP) is a modular machine learning forecasting system
designed to estimate daily solar energy production for a given geographic location.

The system predicts Global Horizontal Irradiance (GHI) using weather forecast data,
converts irradiance into expected solar panel energy output (kWh), and provides
uncertainty bands to communicate prediction confidence.

SPOP is structured as a reproducible ML pipeline with clear separation between:

- Data ingestion
- Dataset construction
- Feature engineering
- Model training
- Forecast generation
- Uncertainty estimation
- User interface

This is not a single notebook experiment. It is a fully organized forecasting system.

Core Capabilities
-----------------

- Predict daily Global Horizontal Irradiance (GHI)
- Convert GHI to solar energy output (kWh)
- Generate uncertainty intervals (±MAE, ±1–3 STD)
- Expose forecasts via a Streamlit web interface
- Provide formal documentation via Sphinx
- Persist trained model artifacts for reuse

System Architecture
-------------------

SPOP follows a modular design:

::

    Data Sources
        ↓
    Data Pipeline
        ↓
    Feature Engineering
        ↓
    Model Training
        ↓
    Forecasting
        ↓
    Uncertainty Bands
        ↓
    Streamlit UI

Each layer is isolated to ensure maintainability, extensibility, and reproducibility.

Technology Stack
----------------

- Python
- scikit-learn (Random Forest)
- Pandas / NumPy
- Streamlit (UI)
- Sphinx (Documentation)

Forecasting Methodology
-----------------------

1. Weather forecasts are retrieved for a specified latitude and longitude.
2. Engineered features are generated using cyclical seasonality encoding and derived weather predictors.
3. A trained Random Forest model predicts daily GHI.
4. GHI is converted to energy output using:

   ::

       Energy (kWh) = GHI × panel_area × efficiency

5. Uncertainty bands are computed using residual statistics from model evaluation.

Design Philosophy
-----------------

SPOP is built with the following principles:

- Reproducible training pipeline
- Clear separation of concerns
- Config-driven behavior
- Modular architecture
- Production-aware project structure
- Formal documentation

Project Scope
-------------

SPOP is designed as a scalable foundation for solar forecasting research and
portfolio demonstration. The current implementation focuses on:

- Tabular weather-based forecasting
- Model evaluation via MAE
- Approximate uncertainty intervals
- Interactive 5-day forecast visualization

Future extensions may include time-series validation, model comparison,
quantile regression, and full deployment automation.

Navigation
----------

Use the sidebar to explore:

- Quickstart instructions
- Architectural design
- Data sources
- Feature engineering approach
- Model design decisions
- Forecast methodology
- Configuration details
- Deployment guidance
- API reference documentation

.. toctree::
   :maxdepth: 2
   :hidden:

   guide/quick_start
   guide/architecture
   guide/data_sources
   guide/feature_engineering
   guide/model_design
   guide/forecast_methodology
   guide/configuration
   guide/deployment
   guide/future_improvements
   api/index
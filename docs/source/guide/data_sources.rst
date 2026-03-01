Data Sources
============

SPOP integrates external solar and weather APIs.

NREL Solar Data
---------------

Provides historical Global Horizontal Irradiance (GHI) data.

Used for:

- Training dataset construction
- Historical performance benchmarking

Open-Meteo
----------

Provides:

- Weather forecasts
- Meteorological features used for prediction

Data Flow
---------

1. Raw API responses retrieved
2. Parsed into structured data
3. Passed into dataset builder

API Abstraction
---------------

All external requests are isolated in the ``data_sources`` module.

This ensures:

- Replaceable APIs
- Testable data ingestion
- No leakage into modeling logic
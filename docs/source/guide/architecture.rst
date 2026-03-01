Architecture
============

SPOP is designed as a modular machine learning forecasting system.

System Overview
---------------

The pipeline follows this structure:

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

Separation of Concerns
----------------------

Each directory has a clear responsibility:

**data_sources/**
    Handles raw API integration (NREL, Open-Meteo).

**data_pipeline/**
    Constructs training datasets from raw inputs.

**features/**
    Cleans and transforms data into model-ready features.

**models/**
    Handles model training, evaluation, and inference.

**math/**
    Computes uncertainty bands and forecast intervals.

**app/**
    Provides the Streamlit interface layer.

**config.py**
    Centralized configuration for model and app settings.

**paths.py**
    Handles project-relative paths and artifact storage.

Design Principles
-----------------

- Modular architecture
- Reproducible training pipeline
- Clear abstraction boundaries
- Config-driven behavior
- Minimal coupling between layers
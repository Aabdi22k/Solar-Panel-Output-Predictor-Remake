API Reference
=============

This section documents the internal modules that power the Solar Panel Output Predictor (SPOP).

The API is organized according to the system architecture and reflects the
separation of concerns implemented in the codebase.

Each module is responsible for a clearly defined layer of the forecasting pipeline.

The documentation exposes public classes, functions, and configuration
components used throughout the system.

Design Principles
-----------------

The API is designed with:

- Clear abstraction boundaries
- Minimal cross-layer coupling
- Reproducible pipeline flow
- Config-driven behavior
- Explicit artifact handling

Only stable, reusable components are documented here.

.. toctree::
   :maxdepth: 2
   :hidden:

   app
   data_pipeline
   data_sources
   features
   models
   math
   core
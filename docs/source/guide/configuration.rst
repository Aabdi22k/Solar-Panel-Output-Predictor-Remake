Configuration
=============

Configuration is centralized in ``config.py``.

Model Settings
--------------

- Random Forest parameters
- Train/test split ratio
- Feature toggles

Application Settings
--------------------

- Default panel area
- Default efficiency
- Forecast horizon

Path Handling
-------------

All filesystem paths are abstracted via ``paths.py``.

This ensures:

- OS independence
- Clean artifact management
- Centralized path control
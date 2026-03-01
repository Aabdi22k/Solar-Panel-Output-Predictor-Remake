Deployment
==========

Local Deployment
----------------

Run Streamlit locally:

.. code-block:: bash

    streamlit run src/main/app/app.py

Documentation Build
-------------------

Build Sphinx documentation:

.. code-block:: bash

    make html

Output will be generated in:

::

    docs/build/html/

Production Considerations
-------------------------

For production deployment:

- Containerize using Docker
- Use environment variables for configuration
- Add CI pipeline for testing
- Deploy via Streamlit Cloud or similar platform
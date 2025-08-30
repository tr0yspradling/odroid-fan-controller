=====================
odroid-fan-controller
=====================


.. image:: https://img.shields.io/pypi/v/odroid_fan_controller.svg
        :target: https://pypi.python.org/pypi/odroid_fan_controller

.. image:: https://img.shields.io/travis/tr0yspradling/odroid_fan_controller.svg
        :target: https://travis-ci.org/tr0yspradling/odroid_fan_controller

.. image:: https://readthedocs.org/projects/odroid-fan-controller/badge/?version=latest
        :target: https://odroid-fan-controller.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status




Simple CLI to manage fan mode and speed for ODROID-XU3/XU4 SBCs.


* Free software: MIT license
* Documentation: https://odroid-fan-controller.readthedocs.io.


Usage
-----

After installation the console entry point is ``odroid_fan_controller``.

- Show status::

    odroid_fan_controller status

- Get or set mode::

    odroid_fan_controller mode
    odroid_fan_controller mode manual
    odroid_fan_controller mode auto

- Get or set speed (25–100%)::

    odroid_fan_controller speed
    odroid_fan_controller speed 60
    odroid_fan_controller speed 60 --force-manual

Notes:

- The ODROID fan is noisy below ~25%; values under 25 are rejected.
- For testing, override the sysfs device path with ``--device-path`` or the
  ``ODROID_FAN_DEVICE_PATH`` environment variable.

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage

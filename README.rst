Introduction
============


.. image:: https://readthedocs.org/projects/adafruit-circuitpython-qualia/badge/?version=latest
    :target: https://docs.circuitpython.org/projects/qualia/en/latest/
    :alt: Documentation Status


.. image:: https://raw.githubusercontent.com/adafruit/Adafruit_CircuitPython_Bundle/main/badges/adafruit_discord.svg
    :target: https://adafru.it/discord
    :alt: Discord


.. image:: https://github.com/adafruit/Adafruit_CircuitPython_Qualia/workflows/Build%20CI/badge.svg
    :target: https://github.com/adafruit/Adafruit_CircuitPython_Qualia/actions
    :alt: Build Status


.. image:: https://img.shields.io/badge/code%20style-black-000000.svg
    :target: https://github.com/psf/black
    :alt: Code Style: Black

Portal Style Library for the Adafruit Qualia ESP32-S3


Dependencies
=============
This driver depends on:

* `Adafruit CircuitPython <https://github.com/adafruit/circuitpython>`_
* `Adafruit CircuitPython Connection Manager <https://github.com/adafruit/Adafruit_CircuitPython_ConnectionManager/>`_
* `Adafruit CircuitPython CST8XX <https://github.com/adafruit/Adafruit_CircuitPython_CST8XX/>`_
* `Adafruit CircuitPython FocalTouch <https://github.com/adafruit/Adafruit_CircuitPython_FocalTouch/>`_
* `Adafruit CircuitPython MiniMQTT <https://github.com/adafruit/Adafruit_CircuitPython_MiniMQTT/>`_
* `Adafruit CircuitPython MiniQR <https://github.com/adafruit/Adafruit_CircuitPython_MiniQR/>`_
* `Adafruit CircuitPython PCA9554 <https://github.com/adafruit/Adafruit_CircuitPython_PCA9554/>`_
* `Adafruit CircuitPython PortalBase <https://github.com/adafruit/Adafruit_CircuitPython_PortalBase/>`_
* `Adafruit CircuitPython Requests <https://github.com/adafruit/Adafruit_CircuitPython_Requests/>`_

Please ensure all dependencies are available on the CircuitPython filesystem.
This is easily achieved by downloading
`the Adafruit library and driver bundle <https://circuitpython.org/libraries>`_
or individual libraries can be installed using
`circup <https://github.com/adafruit/circup>`_.

* Adafruit Qualia ESP32-S3 for TTL RGB-666 Displays

`Purchase one from the Adafruit shop <http://www.adafruit.com/products/5800>`_

Installing from PyPI
=====================
On supported GNU/Linux systems like the Raspberry Pi, you can install the driver locally `from
PyPI <https://pypi.org/project/adafruit-circuitpython-qualia/>`_.
To install for current user:

.. code-block:: shell

    pip3 install adafruit-circuitpython-qualia

To install system-wide (this may be required in some cases):

.. code-block:: shell

    sudo pip3 install adafruit-circuitpython-qualia

To install in a virtual environment in your current project:

.. code-block:: shell

    mkdir project-name && cd project-name
    python3 -m venv .venv
    source .env/bin/activate
    pip3 install adafruit-circuitpython-qualia

Installing to a Connected CircuitPython Device with Circup
==========================================================

Make sure that you have ``circup`` installed in your Python environment.
Install it with the following command if necessary:

.. code-block:: shell

    pip3 install circup

With ``circup`` installed and your CircuitPython device connected use the
following command to install:

.. code-block:: shell

    circup install adafruit_qualia

Or the following command to update an existing version:

.. code-block:: shell

    circup update

Usage Example
=============

.. code-block:: python

    from adafruit_qualia import Qualia
    from adafruit_qualia.graphics import Displays

    # Set a data source URL
    TEXT_URL = "http://wifitest.adafruit.com/testwifi/index.html"

    # Create the PyPortal object
    qualia = Qualia(Displays.SQUARE34, url=TEXT_URL)

    # Go get that data
    print("Fetching text from", TEXT_URL)
    data = qualia.fetch()

    # Print out what we got
    print("-" * 40)
    print(data)
    print("-" * 40)

Documentation
=============
API documentation for this library can be found on `Read the Docs <https://docs.circuitpython.org/projects/qualia/en/latest/>`_.

For information on building library documentation, please check out
`this guide <https://learn.adafruit.com/creating-and-sharing-a-circuitpython-library/sharing-our-docs-on-readthedocs#sphinx-5-1>`_.

Contributing
============

Contributions are welcome! Please read our `Code of Conduct
<https://github.com/adafruit/Adafruit_CircuitPython_Qualia/blob/HEAD/CODE_OF_CONDUCT.md>`_
before contributing to help this project stay welcoming.

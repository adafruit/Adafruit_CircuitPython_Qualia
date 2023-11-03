# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_qualia`
================================================================================

Portal Style Library for the Adafruit Qualia ESP32-S3


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Adafruit Qualia ESP32-S3 <https://www.adafruit.com/product/5800>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://circuitpython.org/downloads

* Adafruit's PortalBase library: https://github.com/adafruit/Adafruit_CircuitPython_PortalBase

"""

import gc
from adafruit_portalbase import PortalBase
from .network import Network
from .graphics import Graphics
from .peripherals import Peripherals

try:
    from typing import Optional, Dict, Union, Callable, Sequence, List
except ImportError:
    pass

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Qualia.git"


class Qualia(PortalBase):
    """Class representing the Adafruit Qualia ESP32-S3.

    :param display_type: The lowercase model of the display that you are using.
    :param url: The URL of your data source. Defaults to ``None``.
    :param headers: The headers for authentication, typically used by Azure API's.
    :param json_path: The list of json traversal to get data out of. Can be list of lists for
                      multiple data points. Defaults to ``None`` to not use json.
    :param regexp_path: The list of regexp strings to get data out (use a single regexp group). Can
                        be list of regexps for multiple data points. Defaults to ``None`` to not
                        use regexp.
    :param default_bg: The path to your default background image file or a hex color.
                       Defaults to 0x000000.
    :param json_transform: A function or a list of functions to call with the parsed JSON.
                           Changes and additions are permitted for the ``dict`` object.
    :param rotation: Default rotation is landscape (270) but can be 0, 90, or 180 for
                     portrait/rotated
    :param scale: Default scale is 1, but can be an integer of 1 or greater
    :param debug: Turn on debug print outs. Defaults to False.
    :param use_network: Enable network initialization. Defaults to True.
                        Setting to False will allow you to use the library without a secrets.py
                        file with wifi configuration in it.

    """

    # pylint: disable=too-few-public-methods
    def __init__(
        self,
        display_type: str,
        *,
        url: Optional[str] = None,
        headers: Dict[str, str] = None,
        json_path: Optional[Union[List[str], List[List[str]]]] = None,
        regexp_path: Optional[Sequence[str]] = None,
        default_bg: int = 0,
        json_transform: Optional[Union[Callable, List[Callable]]] = None,
        rotation: int = 0,
        scale: int = 1,
        debug: bool = False,
        use_network: bool = True
    ) -> None:
        if use_network:
            network = Network(
                extract_values=False,
                debug=debug,
            )
        else:
            network = None

        graphics = Graphics(
            display_type,
            default_bg=default_bg,
            rotation=rotation,
            scale=scale,
            debug=debug,
        )

        super().__init__(
            network,
            graphics,
            url=url,
            headers=headers,
            json_path=json_path,
            regexp_path=regexp_path,
            json_transform=json_transform,
            debug=debug,
        )

        self.peripherals = Peripherals(i2c_bus=graphics.i2c_bus)

        gc.collect()

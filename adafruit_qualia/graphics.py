# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_qualia.graphics`
================================================================================

Portal Style Library for the Adafruit Qualia ESP32-S3


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Adafruit Qualia ESP32-S3 <https://www.adafruit.com/product/5800>`_

**Software and Dependencies:**

* Adafruit CircuitPython firmware for the supported boards:
  https://github.com/adafruit/circuitpython/releases

* Adafruit's PortalBase library: https://github.com/adafruit/Adafruit_CircuitPython_PortalBase

"""

import os
from adafruit_portalbase.graphics import GraphicsBase

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Qualia.git"


class Displays:
    """Class that automatically loads displays from the displays folder."""

    @staticmethod
    def load_displays():
        """Load a list of available displays and set them as attributes"""
        display_folder = __file__.split("/")[0:-1]
        display_folder = "/".join(display_folder) + "/displays"
        displays = os.listdir(display_folder)
        Displays._valid_displays = [
            x.split(".")[0]
            for x in displays
            if not (x.startswith("_")) and not (x.startswith("."))
        ]
        for display in Displays._valid_displays:
            setattr(Displays, display.upper(), display)

    @staticmethod
    def valid_displays():
        """Return the available valid displays"""
        return Displays._valid_displays


# Load the displays before it can be used
Displays.load_displays()


class Graphics(GraphicsBase):
    """Graphics Helper Class for the Adafruit Qualia ESP32-S3 Library

    :param display_type: The lowercase model of the display that you are using.
    :param auto_refresh: Set to False to disable auto refresh. Defaults to True.
    :param default_bg: The path to your default background image file or a hex color.
                       Defaults to 0x000000.
    :param rotation: Default rotation is landscape (270) but can be 0, 90, 180 for portrait/rotated
    :param debug: Turn on debug print outs. Defaults to False.

    """

    def __init__(
        self,
        display_type: str,
        *,
        auto_refresh: bool = True,
        default_bg: int = 0,
        rotation: int = 0,
        scale: int = 1,
        debug: bool = False
    ) -> None:
        self._dotclock_display = None
        self.init_display(display_type, auto_refresh=auto_refresh)
        super().__init__(
            self._dotclock_display.display,
            default_bg=default_bg,
            scale=scale,
            debug=debug,
        )
        self.display.rotation = rotation

    def init_display(self, display_type: str, *, auto_refresh: bool = True):
        """Load the Display Class, then initialize the display and touch driver"""

        def case_insensitive_find(list_to_search, name):
            for item in list_to_search:
                if item.lower() == name.lower():
                    return item
            return None

        if display_type not in Displays.valid_displays():
            raise ValueError(
                "Invalid display type. "
                "Use Displays.valid_displays() to get a list of valid displays."
            )

        parent_class = self.__module__.split(".")[0]  # pylint: disable=use-maxsplit-arg
        class_path = (parent_class, "displays", display_type.lower())

        display_class = __import__(".".join(class_path))
        for item in class_path[1:]:
            display_class = getattr(display_class, item)
        class_name = case_insensitive_find(dir(display_class), display_type)

        display_class = getattr(display_class, class_name)
        self._dotclock_display = display_class()  # Instantiate the class
        self._dotclock_display.init(auto_refresh=auto_refresh)  # Initialize the display
        self._dotclock_display.init_touch()  # Initialize the touch driver

    @property
    def i2c_bus(self):
        """Return the I2C bus"""
        return self._dotclock_display.i2c_bus

    @property
    def touch(self):
        """Return the touch driver"""
        return self._dotclock_display.touch

    @property
    def dotclockdisplay(self):
        """Return the dotclock display object"""
        return self._dotclock_display

# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2022 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT
"""
`adafruit_qualia.peripherals`
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
* Adafruit's PCA9554 library: https://github.com/adafruit/Adafruit_CircuitPython_PCA9554
* Adafruit's CST8XX library: https://github.com/adafruit/Adafruit_CircuitPython_CST8XX
* Adafruit's FocalTouch library: https://github.com/adafruit/Adafruit_CircuitPython_FocalTouch

"""

import board
import busio
from digitalio import Pull
import adafruit_pca9554

__version__ = "0.0.0+auto.0"
__repo__ = "https://github.com/adafruit/Adafruit_CircuitPython_Qualia.git"


class Peripherals:
    """Peripherals Helper Class for the Adafruit Qualia ESP32-S3 Library"""

    def __init__(self, *, i2c_bus: busio.I2C = None, address: int = 0x3F) -> None:
        if i2c_bus is None:
            i2c_bus = busio.I2C(board.SCL, board.SDA)

        pcf = adafruit_pca9554.PCA9554(i2c_bus, address=address)

        # Buttons
        self._buttons = []
        for pin in (board.BTN_DN, board.BTN_UP):
            switch = pcf.get_pin(pin)
            switch.switch_to_input(pull=Pull.UP)
            self._buttons.append(switch)

        # TFT Backlight
        self._backlight = pcf.get_pin(board.BACKLIGHT)
        self._backlight.switch_to_output(value=True)

    def deinit(self) -> None:
        """Call deinit on all resources to free them"""
        for button in self._buttons:
            button.deinit()

    @property
    def button_down(self) -> bool:
        """
        Return whether Down Button is pressed
        """
        return not self._buttons[0].value

    @property
    def button_up(self) -> bool:
        """
        Return whether Up Button is pressed
        """
        return not self._buttons[1].value

    @property
    def backlight(self) -> bool:
        """
        Return whether the backlight is on
        """
        return self._backlight.value

    @backlight.setter
    def backlight(self, value: bool) -> None:
        """
        Set the backlight on or off
        """
        self._backlight.value = value

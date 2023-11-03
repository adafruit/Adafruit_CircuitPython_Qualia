# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays.square40`
================================================================================

4" 720x720 Square DotClock Display Class


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Square RGB TTL TFT Display - 4" 720x720 - with Capacitive Touch
  <https://www.adafruit.com/product/5794>`_
* `Square RGB 666 TTL TFT Display - 4" 720x720 - No Touchscreen
  <https://www.adafruit.com/product/5795>`_

"""

from . import DotClockDisplay


class Square40(DotClockDisplay):
    """TL040HDS20 display driver"""

    def __init__(self):
        super().__init__()
        self._touch_address = 0x48
        self._timings = {
            "frequency": 16000000,
            "width": 720,
            "height": 720,
            "hsync_pulse_width": 2,
            "hsync_front_porch": 46,
            "hsync_back_porch": 44,
            "vsync_pulse_width": 2,
            "vsync_front_porch": 16,
            "vsync_back_porch": 18,
            "hsync_idle_low": False,
            "vsync_idle_low": False,
            "de_idle_high": False,
            "pclk_active_high": False,
            "pclk_idle_high": False,
        }

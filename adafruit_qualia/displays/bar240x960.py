# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays.bar240x960`
================================================================================

3.71" 240x960 Bar DotClock Display Class


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Rectangle Bar RGB TTL TFT Display - 3.7" 240x960 No Touchscreen
  <https://www.adafruit.com/product/5799>`_

"""

from . import DotClockDisplay


class Bar240x960(DotClockDisplay):
    """HD371001C40 display driver"""

    def __init__(self):
        super().__init__()
        self._init_sequence = bytes(
            b"\xff\x05w\x01\x00\x00\x13"
            b"\xef\x01\x08"
            b"\xff\x05w\x01\x00\x00\x10"
            b"\xc0\x02w\x00"
            b"\xc1\x02\x11\x0c"
            b"\xc2\x02\x07\x02"
            b"\xcc\x010"
            b"\xb0\x10\x06\xcf\x14\x0c\x0f\x03\x00\n\x07\x1b\x03\x12\x10%6\x1e"
            b"\xb1\x10\x0c\xd4\x18\x0c\x0e\x06\x03\x06\x08#\x06\x12\x100/\x1f"
            b"\xff\x05w\x01\x00\x00\x11"
            b"\xb0\x01s"
            b"\xb1\x01|"
            b"\xb2\x01\x83"
            b"\xb3\x01\x80"
            b"\xb5\x01I"
            b"\xb7\x01\x87"
            b"\xb8\x013"
            b"\xb9\x02\x10\x1f"
            b"\xbb\x01\x03"
            b"\xc1\x01\x08"
            b"\xc2\x01\x08"
            b"\xd0\x01\x88"
            b"\xe0\x06\x00\x00\x02\x00\x00\x0c"
            b"\xe1\x0b\x05\x96\x07\x96\x06\x96\x08\x96\x00DD"
            b"\xe2\x0c\x00\x00\x03\x03\x00\x00\x02\x00\x00\x00\x02\x00"
            b"\xe3\x04\x00\x0033"
            b"\xe4\x02DD"
            b"\xe5\x10\r\xd4(\x8c\x0f\xd6(\x8c\t\xd0(\x8c\x0b\xd2(\x8c"
            b"\xe6\x04\x00\x0033"
            b"\xe7\x02DD"
            b"\xe8\x10\x0e\xd5(\x8c\x10\xd7(\x8c\n\xd1(\x8c\x0c\xd3(\x8c"
            b"\xeb\x06\x00\x01\xe4\xe4D\x00"
            b"\xed\x10\xf3\xc1\xba\x0ffwDUUDwf\xf0\xab\x1c?"
            b"\xef\x06\x10\r\x04\x08?\x1f"
            b"\xff\x05w\x01\x00\x00\x13"
            b"\xe8\x02\x00\x0e"
            b"\x11\x80x"
            b"\xe8\x82\x00\x0c\n"
            b"\xe8\x02@\x00"
            b"\xff\x05w\x01\x00\x00\x00"
            b"6\x01\x00"
            b":\x01f"
            b")\x80\x14"
            b"\xff\x05w\x01\x00\x00\x10"
            b"\xe5\x02\x00\x00"
        )

        self._timings = {
            "frequency": 16000000,
            "width": 240,
            "height": 960,
            "overscan_left": 120,
            "hsync_pulse_width": 8,
            "hsync_back_porch": 20,
            "hsync_front_porch": 20,
            "hsync_idle_low": False,
            "vsync_pulse_width": 8,
            "vsync_back_porch": 20,
            "vsync_front_porch": 20,
            "vsync_idle_low": False,
            "pclk_active_high": True,
            "pclk_idle_high": False,
            "de_idle_high": False,
        }

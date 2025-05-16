# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays.round40_480x480`
================================================================================

4" 480x480 Square DotClock Display Class


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Square RGB TTL TFT Display - 4" 480x480 - with Capacitive Touch
  <https://www.adafruit.com/product/5826>`_
* `Square RGB TTL TFT Display - 4" 480x480 - No Touchscreen
  <https://www.adafruit.com/product/5827>`_
"""

from . import DotClockDisplay


class Square40_480x480(DotClockDisplay):
    """TL040WVS03 display driver"""

    def __init__(self):
        super().__init__()
        self._init_sequence = bytes(
            b"\xff\x05w\x01\x00\x00\x10"
            b"\xc0\x02;\x00"
            b"\xc1\x02\r\x02"
            b"\xc2\x021\x05"
            b"\xcd\x01\x08"
            b'\xb0\x10\x00\x11\x18\x0e\x11\x06\x07\x08\x07"\x04\x12\x0f\xaa1\x18'
            b'\xb1\x10\x00\x11\x19\x0e\x12\x07\x08\x08\x08"\x04\x11\x11\xa92\x18'
            b"\xff\x05w\x01\x00\x00\x11"
            b"\xb0\x01`"
            b"\xb1\x012"
            b"\xb2\x01\x07"
            b"\xb3\x01\x80"
            b"\xb5\x01I"
            b"\xb7\x01\x85"
            b"\xb8\x01!"
            b"\xc1\x01x"
            b"\xc2\x01x"
            b"\xe0\x03\x00\x1b\x02"
            b"\xe1\x0b\x08\xa0\x00\x00\x07\xa0\x00\x00\x00DD"
            b"\xe2\x0c\x11\x11DD\xed\xa0\x00\x00\xec\xa0\x00\x00"
            b"\xe3\x04\x00\x00\x11\x11"
            b"\xe4\x02DD"
            b"\xe5\x10\n\xe9\xd8\xa0\x0c\xeb\xd8\xa0\x0e\xed\xd8\xa0\x10\xef\xd8\xa0"
            b"\xe6\x04\x00\x00\x11\x11"
            b"\xe7\x02DD"
            b"\xe8\x10\t\xe8\xd8\xa0\x0b\xea\xd8\xa0\r\xec\xd8\xa0\x0f\xee\xd8\xa0"
            b"\xeb\x07\x02\x00\xe4\xe4\x88\x00@"
            b"\xec\x02<\x00"
            b"\xed\x10\xab\x89vT\x02\xff\xff\xff\xff\xff\xff Eg\x98\xba"
            b"6\x01\x00"
            b"\xff\x05w\x01\x00\x00\x13"
            b"\xe5\x01\xe4"
            b"\xff\x05w\x01\x00\x00\x00"
            b":\x01f"
            b"!\x80\n"
            b"\x11\x80x"
            b")\x00"
        )

        self._timings = {
            "frequency": 16000000,
            "width": 480,
            "height": 480,
            "hsync_pulse_width": 2,
            "hsync_back_porch": 44,
            "hsync_front_porch": 50,
            "hsync_idle_low": False,
            "vsync_pulse_width": 2,
            "vsync_back_porch": 18,
            "vsync_front_porch": 16,
            "vsync_idle_low": False,
            "pclk_active_high": True,
            "pclk_idle_high": False,
            "de_idle_high": False,
        }

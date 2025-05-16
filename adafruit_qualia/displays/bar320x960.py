# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays.bar320x960`
================================================================================

4.58" 320x960 Bar DotClock Display Class


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Rectangle Bar RGB TTL TFT Display - 4.58" 320x960 No Touchscreen
  <https://www.adafruit.com/product/5805>`_

"""

from . import DotClockDisplay


class Bar320x960(DotClockDisplay):
    """HD458002C40 display driver"""

    def __init__(self):
        super().__init__()
        self._init_sequence = bytes(
            b"\xff\x05w\x01\x00\x00\x13"
            b"\xef\x01\x08"
            b"\xff\x05w\x01\x00\x00\x10"
            b"\xc0\x02w\x00"
            b"\xc1\x02\t\x08"
            b"\xc2\x02\x01\x02"
            b"\xc3\x01\x02"
            b"\xcc\x01\x10"
            b"\xb0\x10@\x14Y\x10\x12\x08\x03\t\x05\x1e\x05\x14\x10h3\x15"
            b"\xb1\x10@\x08S\t\x11\t\x02\x07\t\x1a\x04\x12\x12d))"
            b"\xff\x05w\x01\x00\x00\x11"
            b"\xb0\x01m"
            b"\xb1\x01\x1d"
            b"\xb2\x01\x87"
            b"\xb3\x01\x80"
            b"\xb5\x01I"
            b"\xb7\x01\x85"
            b"\xb8\x01 "
            b"\xc1\x01x"
            b"\xc2\x01x"
            b"\xd0\x01\x88"
            b"\xe0\x03\x00\x00\x02"
            b"\xe1\x0b\x02\x8c\x00\x00\x03\x8c\x00\x00\x0033"
            b"\xe2\r3333\xc9<\x00\x00\xca<\x00\x00\x00"
            b"\xe3\x04\x00\x0033"
            b"\xe4\x02DD"
            b"\xe5\x10\x05\xcd\x82\x82\x01\xc9\x82\x82\x07\xcf\x82\x82\x03\xcb\x82\x82"
            b"\xe6\x04\x00\x0033"
            b"\xe7\x02DD"
            b"\xe8\x10\x06\xce\x82\x82\x02\xca\x82\x82\x08\xd0\x82\x82\x04\xcc\x82\x82"
            b"\xeb\x07\x08\x01\xe4\xe4\x88\x00@"
            b"\xec\x03\x00\x00\x00"
            b"\xed\x10\xff\xf0\x07eO\xfc\xc2/\xf2,\xcf\xf4Vp\x0f\xff"
            b"\xef\x06\x10\r\x04\x08?\x1f"
            b"\xff\x05w\x01\x00\x00\x00"
            b"\x11\x80x"
            b"5\x01\x00"
            b":\x81fd"
            b")\x00"
        )

        self._timings = {
            "frequency": 16000000,
            "width": 320,
            "height": 960,
            "overscan_left": 80,
            "hsync_pulse_width": 10,
            "hsync_front_porch": 30,
            "hsync_back_porch": 50,
            "hsync_idle_low": False,
            "vsync_pulse_width": 2,
            "vsync_front_porch": 15,
            "vsync_back_porch": 17,
            "vsync_idle_low": False,
            "pclk_active_high": False,
            "pclk_idle_high": False,
            "de_idle_high": False,
        }

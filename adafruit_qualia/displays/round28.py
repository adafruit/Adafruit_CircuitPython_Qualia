# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays.round28`
================================================================================

2.8" 480x480 Round DotClock Display Class


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Round RGB 666 TTL TFT Display - 2.8" 480x480 - No Touch
  <https://www.adafruit.com/product/5852>`_

"""

from . import DotClockDisplay


class Round28(DotClockDisplay):
    """TL028WVC01 display driver"""

    def __init__(self):
        super().__init__()
        self._init_sequence = bytes(
            b"\xff\x05w\x01\x00\x00\x13"
            b"\xef\x01\x08"
            b"\xff\x05w\x01\x00\x00\x10"
            b"\xc0\x02;\x00"
            b"\xc1\x02\x10\x0c"
            b"\xc2\x02\x07\n"
            b"\xc7\x01\x00"
            b"\xcc\x01\x10"
            b"\xcd\x01\x08"
            b"\xb0\x10\x05\x12\x98\x0e\x0f\x07\x07\t\t#\x05R\x0fg,\x11"
            b'\xb1\x10\x0b\x11\x97\x0c\x12\x06\x06\x08\x08"\x03Q\x11f+\x0f'
            b"\xff\x05w\x01\x00\x00\x11"
            b"\xb0\x01]"
            b"\xb1\x01-"
            b"\xb2\x01\x81"
            b"\xb3\x01\x80"
            b"\xb5\x01N"
            b"\xb7\x01\x85"
            b"\xb8\x01 "
            b"\xc1\x01x"
            b"\xc2\x01x"
            b"\xd0\x01\x88"
            b"\xe0\x03\x00\x00\x02"
            b"\xe1\x0b\x060\x080\x050\x070\x0033"
            b"\xe2\x0c\x11\x1133\xf4\x00\x00\x00\xf4\x00\x00\x00"
            b"\xe3\x04\x00\x00\x11\x11"
            b"\xe4\x02DD"
            b"\xe5\x10\r\xf50\xf0\x0f\xf70\xf0\t\xf10\xf0\x0b\xf30\xf0"
            b"\xe6\x04\x00\x00\x11\x11"
            b"\xe7\x02DD"
            b"\xe8\x10\x0c\xf40\xf0\x0e\xf60\xf0\x08\xf00\xf0\n\xf20\xf0"
            b"\xe9\x026\x01"
            b"\xeb\x07\x00\x01\xe4\xe4D\x88@"
            b"\xed\x10\xff\x10\xafvT+\xcf\xff\xff\xfc\xb2Eg\xfa\x01\xff"
            b"\xef\x06\x08\x08\x08E?T"
            b"\xff\x05w\x01\x00\x00\x00"
            b"\x11\x80x"
            b":\x01f"
            b"6\x01\x00"
            b"5\x01\x00"
            b")\x802"
        )

        self._timings = {
            "frequency": 15_000_000,
            "width": 480,
            "height": 480,
            "hsync_pulse_width": 2,
            "hsync_back_porch": 10,
            "hsync_front_porch": 10,
            "hsync_idle_low": False,
            "vsync_pulse_width": 6,
            "vsync_back_porch": 10,
            "vsync_front_porch": 10,
            "vsync_idle_low": False,
            "pclk_active_high": True,
            "pclk_idle_high": False,
            "de_idle_high": False,
        }

        self._round = True

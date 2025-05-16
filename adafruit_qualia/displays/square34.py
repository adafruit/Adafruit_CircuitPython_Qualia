# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays.square34`
================================================================================

3.4" 480x480 Square DotClock Display Class


* Author(s): Melissa LeBlanc-Williams

Implementation Notes
--------------------

**Hardware:**

* `Square RGB 666 TTL TFT Display - 3.4" 480x480 with Touchscreen
  <https://www.adafruit.com/product/5808>`_
* `Square RGB 666 TTL TFT Display - 3.4" 480x480 No Touchscreen
  <https://www.adafruit.com/product/5825>`_

"""

from . import DotClockDisplay


class Square34(DotClockDisplay):
    """TL034WVS05 display driver"""

    def __init__(self):
        super().__init__()
        self._init_sequence = bytes(
            b"\xff\x05w\x01\x00\x00\x13"
            b"\xef\x01\x08"
            b"\xff\x05w\x01\x00\x00\x10"
            b"\xc0\x02;\x00"
            b"\xc1\x02\x12\n"
            b"\xc2\x02\x07\x03"
            b"\xc3\x01\x02"
            b"\xcc\x01\x10"
            b"\xcd\x01\x08"
            b"\xb0\x10\x0f\x11\x17\x15\x15\t\x0c\x08\x08&\x04Y\x16f-\x1f"
            b"\xb1\x10\x0f\x11\x17\x15\x15\t\x0c\x08\x08&\x04Y\x16f-\x1f"
            b"\xff\x05w\x01\x00\x00\x11"
            b"\xb0\x01m"
            b"\xb1\x01:"
            b"\xb2\x01\x01"
            b"\xb3\x01\x80"
            b"\xb5\x01I"
            b"\xb7\x01\x85"
            b"\xb8\x01 "
            b"\xc1\x01x"
            b"\xc2\x01x"
            b"\xd0\x01\x88"
            b"\xe0\x03\x00\x00\x02"
            b"\xe1\x0b\x07\x00\t\x00\x06\x00\x08\x00\x0033"
            b"\xe2\r\x11\x1133\xf6\x00\xf6\x00\xf6\x00\xf6\x00\x00"
            b"\xe3\x04\x00\x00\x11\x11"
            b"\xe4\x02DD"
            b"\xe5\x10\x0f\xf3=\xff\x11\xf5=\xff\x0b\xef=\xff\r\xf1=\xff"
            b"\xe6\x04\x00\x00\x11\x11"
            b"\xe7\x02DD"
            b"\xe8\x10\x0e\xf2=\xff\x10\xf4=\xff\n\xee=\xff\x0c\xf0=\xff"
            b"\xe9\x026\x00"
            b"\xeb\x07\x00\x01\xe4\xe4D\xaa\x10"
            b"\xec\x02<\x00"
            b"\xed\x10\xffEg\xfa\x01+\xcf\xff\xff\xfc\xb2\x10\xafvT\xff"
            b"\xef\x06\x10\r\x04\x08?\x1f"
            b"\xff\x05w\x01\x00\x00\x00"
            b"5\x01\x00"
            b":\x01f"
            b"\x11\x80x"
            b")\x802"
        )

        self._timings = {
            "frequency": 16000000,
            "width": 480,
            "height": 480,
            "hsync_pulse_width": 20,
            "hsync_front_porch": 40,
            "hsync_back_porch": 40,
            "vsync_pulse_width": 10,
            "vsync_front_porch": 40,
            "vsync_back_porch": 40,
            "hsync_idle_low": False,
            "vsync_idle_low": False,
            "de_idle_high": False,
            "pclk_active_high": False,
            "pclk_idle_high": False,
        }

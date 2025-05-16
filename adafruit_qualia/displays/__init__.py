# SPDX-FileCopyrightText: 2017 Scott Shawcroft, written for Adafruit Industries
# SPDX-FileCopyrightText: Copyright (c) 2023 Melissa LeBlanc-Williams for Adafruit Industries
#
# SPDX-License-Identifier: MIT

"""
`adafruit_qualia.displays`
================================================================================

DotClock Display Base Class


* Author(s): Melissa LeBlanc-Williams

"""

import time

import board
import busio
import dotclockframebuffer
import espidf
from adafruit_cst8xx import Adafruit_CST8XX
from adafruit_focaltouch import Adafruit_FocalTouch
from displayio import release_displays
from framebufferio import FramebufferDisplay

TOUCH_FOCALTOUCH = Adafruit_FocalTouch
TOUCH_CST826 = Adafruit_CST8XX

TOUCH_INIT_DELAY = 0.1  # 100ms


class DotClockDisplay:
    """DotClock Display Base Class for the Adafruit Qualia ESP32-S3 Library"""

    def __init__(self):
        release_displays()
        board.I2C().deinit()
        self._init_sequence = b""
        self._timings = {}
        self._bus_frequency = 100_000
        self._touch_driver = TOUCH_FOCALTOUCH
        self._touch_address = 0x38
        self.display = None
        self.touch = None
        self._i2c = None
        self._round = False

    def init(self, *, auto_refresh: bool = True):
        """Initialize the display"""
        # Initialize the display at the displays bus frequency
        i2c = busio.I2C(board.SCL, board.SDA, frequency=self._bus_frequency)
        tft_io_expander = dict(board.TFT_IO_EXPANDER)
        dotclockframebuffer.ioexpander_send_init_sequence(
            i2c, self._init_sequence, **tft_io_expander
        )
        i2c.deinit()
        params = dict(board.TFT_PINS)
        params.update(self._timings)
        try:
            framebuffer = dotclockframebuffer.DotClockFramebuffer(**params)
        except espidf.IDFError as exc:
            raise RuntimeError(
                "Display dimension error. "
                "Make sure you are running the absolute latest version of CircuitPython."
            ) from exc
        self.display = FramebufferDisplay(framebuffer, auto_refresh=auto_refresh)

    def init_touch(self):
        """Attempt to initialize the touch driver"""
        # Set with I2C at default speed
        self._i2c = busio.I2C(board.SCL, board.SDA)
        time.sleep(TOUCH_INIT_DELAY)  # Wait for Focaltouch Chip to finish resetting
        try:
            self.touch = self._touch_driver(self._i2c, self._touch_address)
        except (RuntimeError, ValueError):
            self.touch = None

    @property
    def width(self):
        """The width of the display in pixels"""
        if "width" not in self._timings:
            raise RuntimeError("Baseclass should not be called directly")
        return self._timings["width"]

    @property
    def height(self):
        """The height of the display in pixels"""
        if "height" not in self._timings:
            raise RuntimeError("Baseclass should not be called directly")
        return self._timings["height"]

    @property
    def i2c_bus(self):
        """Return the I2C bus"""
        if self._i2c is None:
            raise RuntimeError("Touch should be initialized first.")
        return self._i2c

    @property
    def round(self):
        """Return whether the display is circular"""
        return self._round

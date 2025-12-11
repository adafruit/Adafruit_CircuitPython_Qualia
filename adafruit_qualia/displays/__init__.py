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


class Touch:
    """Simple passthrough touch class that allows rotation transformation"""

    def __init__(self, touch_driver, display, rotation=0):
        self._driver = touch_driver
        self._width = display.width
        self._height = display.height
        self._rotation = rotation

    def transform(self, x, y):
        """Transform touch coordinates based on rotation"""
        if self._rotation == 0:
            return x, y
        elif self._rotation == 90:
            return y, self._width - x
        elif self._rotation == 180:
            return self._width - x, self._height - y
        elif self._rotation == 270:
            return self._height - y, x
        else:
            raise ValueError("Rotation must be 0, 90, 180, or 270")

    @property
    def rotation(self):
        """Return the rotation"""
        return self._rotation

    @rotation.setter
    def rotation(self, value):
        """Set the rotation"""
        if value not in {0, 90, 180, 270}:
            raise ValueError("Rotation must be 0, 90, 180, or 270")
        self._rotation = value

    @property
    def touches(self):
        """Return the number of touches"""
        touches = self._driver.touches
        for touch in touches:
            touch["x"], touch["y"] = self.transform(touch["x"], touch["y"])
        return touches

    @property
    def touched(self):
        """Return whether the screen is touched"""
        return self._driver.touched


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
        self._touch = None
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
            self._touch = Touch(self._touch_driver(self._i2c, self._touch_address), self.display)

        except (RuntimeError, ValueError):
            self._touch = None

    def _transform_touch(self, x, y):
        """Transform touch coordinates if needed"""
        return x, y

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

    @property
    def rotation(self):
        """Return the display touch rotation"""
        display_rotation = self.display.rotation if self.display is not None else 0
        touch_rotation = self._touch.rotation if self._touch is not None else 0
        if display_rotation != touch_rotation:
            raise ValueError("Display and touch rotation do not match")
        return self._touch.rotation

    @rotation.setter
    def rotation(self, value: int):
        """Set the display rotation"""
        if value not in {0, 90, 180, 270}:
            raise ValueError("Rotation must be 0, 90, 180, or 270")
        if self._touch:
            self._touch.rotation = value
        # Update the display rotation if already initialized
        if self.display:
            self.display.rotation = value

    @property
    def touch(self):
        """Return the touch driver"""
        return self._touch

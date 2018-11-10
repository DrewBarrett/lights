# Will animate a rainbow color cycle on all pixels.
from __future__ import division
import time

# Import the WS2801 module.
import Adafruit_WS2801
import Adafruit_GPIO.SPI as SPI


# Configure the count of pixels:
PIXEL_COUNT = 32

# The WS2801 library makes use of the BCM pin numbering scheme. See the README.md for details.

# Specify a software SPI connection for Raspberry Pi on the following pins:
#PIXEL_CLOCK = 18
#PIXEL_DOUT  = 23
#pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, clk=PIXEL_CLOCK, do=PIXEL_DOUT)

# Alternatively specify a hardware SPI connection on /dev/spidev0.0:
SPI_PORT   = 0
SPI_DEVICE = 0
pixels = Adafruit_WS2801.WS2801Pixels(PIXEL_COUNT, spi=SPI.SpiDev(SPI_PORT, SPI_DEVICE))

# Clear all the pixels to turn them off.
pixels.clear()
pixels.show()  # Make sure to call show() after changing any pixels!

# Define rainbow cycle function to do a cycle of all hues.
def rainbow_cycle(pixels, wait=0):
    rgb = [255, 3, 3]
    k = 0
    while True:
        print(rgb, k)
        if rgb[k] >= 255:
            if rgb[k-1] > 3:
                print("k-1 greater than 3", rgb[k-1], k)
                rgb[k-1] -= 1
            else:
                print("Incrementing k", k)
                k = (k + 1) % 3
        else:
            rgb[k] += 1
        for i in range(pixels.count()):
            pixels.set_pixel_rgb(i, rgb[0], rgb[1], rgb[2])
        pixels.show()
        if wait > 0:
            time.sleep(wait)

print('Rainbow cycling, press Ctrl-C to quit...')
while True:
    rainbow_cycle(pixels,0.1)

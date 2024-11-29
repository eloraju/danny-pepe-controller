import time
from rpi_ws281x import PixelStrip, Color
from random import randint
import colorsys as col

# test 

# LED strip configuration:
LED_COUNT = 350        # Number of LED pixels.
LED_PIN = 18          # GPIO pin connected to the pixels (must support PWM!).
LED_FREQ_HZ = 800000  # LED signal frequency in hertz (usually 800kHz).
LED_DMA = 10          # DMA channel to use for generating signal (try 10).
LED_BRIGHTNESS = 255  # Set to 0 for darkest and 255 for brightest.
LED_INVERT = False    # True to invert the signal (when using NPN transistor level shift).
LED_CHANNEL = 0

LED_D_OUTER = 156
LED_D_INNER = 143
LED_D_COUNT = LED_D_INNER + LED_D_OUTER

LED_W_LOWER = 232
LED_W_UPPER = 233
LED_W_COUNT = LED_W_LOWER + LED_W_UPPER
LED_W = 233

# Create PixelStrip object
test_strip = PixelStrip(LED_COUNT, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
test_strip.begin()

def init_strip(led_count):
  strip = PixelStrip(led_count, LED_PIN, LED_FREQ_HZ, LED_DMA, LED_INVERT, LED_BRIGHTNESS, LED_CHANNEL)
  strip.begin()
  print("strip initialized")
  return strip

def set_all_pixels(strip, color, wait_ms=100):
  print("Calling set_all for strip" + str(strip))
  print(strip.numPixels())
  for i in range(strip.numPixels()):
    print(i)
    strip.setPixelColor(i, color)

  strip.show()
  time.sleep(wait_ms / 1000.0)

# Function to light up the LEDs in sequence
def color_wipe(strip, color, wait_ms=50):
    for i in range(155,155+strip.numPixels()):
        strip.setPixelColor(i, color)
        strip.show()
        time.sleep(wait_ms / 1000.0)

def set_all(strip, color, wait_ms=160):
    for i in range(strip.numPixels()):
        strip.setPixelColor(i, color)

    strip.show()
    time.sleep(wait_ms / 1000.0)


def color_slide(strip, wait_ms = 50):
  for i in range(0,361):
    color = col.hsv_to_rgb((1.0/360.)*i,1.0,0.8)
    r,g,b = [int(x*255) for x in color]
    set_all(strip, Color(r,g,b), wait_ms)

def blend_hue(strip, col1, col2, time):
  hue1 = col.rgb_to_hsv(r = col1.r, g = col1.g, b = col1.b)[0]
  hue2 = col.rgb_to_hsv(r = col2.r, g = col2.g, b = col2.b)[0]
  fromHue = int(min(hue1,hue2) * 1000)
  toHue = int(max(hue1,hue2) * 1000)


def randcol():
    r = randint(0,255)
    g = randint(0,255)
    b = randint(0,255)

    return Color(r,g,b)

def random_epilepsy(strip, wait_ms=10):
    color = randcol()
    strip_start = 156
    strip_end = strip_start + 142
    for i in range(strip_start,strip_end):
        strip.setPixelColor(i, color)

    strip.show()
    time.sleep(wait_ms / 1000.0)

w_full_strip = init_strip(LED_W)

# Main program logic
if __name__ == '__main__':
    try:
        while True:
          color_slide(w_full_strip,10)
    except KeyboardInterrupt:
        set_all(test_strip, Color(0, 0, 0), 10)

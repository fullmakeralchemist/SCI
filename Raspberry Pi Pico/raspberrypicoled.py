from machine import Pin

import time

ledrojo = Pin(25, Pin.OUT) #Pin 15

while True:
      ledrojo.value(1)
      time.sleep(0.5)
      ledrojo.value(0)
      time.sleep(0.5)
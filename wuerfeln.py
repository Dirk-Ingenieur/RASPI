# Unser Wuerfelprogramm
#
# (c) 2020 Leenke und Dirk Stueker
#
# Das Programm erzeugt auf Knopfdruck Zufallszahlen zwischen 1 und 6
#
# Beschaltung:
# Linke drei LEDs  - GPIO 13 / 19 / 26
# Mittlere LED     - GPIO 12
# Rechte drei LEDs - GPIO 16/20/21


import RPi.GPIO as gpio
import time
import random

# Initialisierung der Ein-/Ausgaenge
gpio.setmode(gpio.BCM)
# LED-Ausgaenge
gpio.setup(13,gpio.OUT)
gpio.setup(19,gpio.OUT)
gpio.setup(26,gpio.OUT)
gpio.setup(12,gpio.OUT)
gpio.setup(16,gpio.OUT)
gpio.setup(20,gpio.OUT)
gpio.setup(21,gpio.OUT)

# Taster-Eingang
gpio.setup(23,gpio.IN,gpio.PUD_UP)

# Test: Alle LEDs an
gpio.setmode(gpio.BCM)
gpio.output(13,gpio.HIGH)
gpio.output(19,gpio.HIGH)
gpio.output(26,gpio.HIGH)
gpio.output(12,gpio.HIGH)
gpio.output(16,gpio.HIGH)
gpio.output(20,gpio.HIGH)
gpio.output(21,gpio.HIGH)
time.sleep(2)

while True:
  # Aufraeumen: Alle LEDs aus
  gpio.output(13,gpio.LOW)
  gpio.output(19,gpio.LOW)
  gpio.output(26,gpio.LOW)
  gpio.output(12,gpio.LOW)
  gpio.output(16,gpio.LOW)
  gpio.output(20,gpio.LOW)
  gpio.output(21,gpio.LOW)
  
  print("Bitte Taste druecken und halten.")
  buttonPressed = False;
  while not buttonPressed:
    buttonPressed = (gpio.input(23) == gpio.LOW)
  print("Wuerfeln laeuft.")
  
  while buttonPressed:
    buttonPressed = (gpio.input(23) == gpio.LOW)
# print("Taste gedrueckt: ",buttonPressed)

    zahl = random.randint(1,6)
    time.sleep(0.05)

    if zahl == 1:
      gpio.output(13,gpio.LOW)
      gpio.output(19,gpio.LOW)
      gpio.output(26,gpio.LOW)
      gpio.output(12,gpio.HIGH)
      gpio.output(16,gpio.LOW)
      gpio.output(20,gpio.LOW)
      gpio.output(21,gpio.LOW)

    if zahl == 2:
      gpio.output(13,gpio.HIGH)
      gpio.output(19,gpio.LOW)
      gpio.output(26,gpio.LOW)
      gpio.output(12,gpio.LOW)
      gpio.output(16,gpio.LOW)
      gpio.output(20,gpio.LOW)
      gpio.output(21,gpio.HIGH)

    if zahl == 3:
      gpio.output(13,gpio.LOW)
      gpio.output(19,gpio.LOW)
      gpio.output(26,gpio.HIGH)
      gpio.output(12,gpio.HIGH)
      gpio.output(16,gpio.HIGH)
      gpio.output(20,gpio.LOW)
      gpio.output(21,gpio.LOW)

    if zahl == 4:
      gpio.output(13,gpio.HIGH)
      gpio.output(19,gpio.LOW)
      gpio.output(26,gpio.HIGH)
      gpio.output(12,gpio.LOW)
      gpio.output(16,gpio.HIGH)
      gpio.output(20,gpio.LOW)
      gpio.output(21,gpio.HIGH)

    if zahl == 5:
      gpio.output(13,gpio.HIGH)
      gpio.output(19,gpio.LOW)
      gpio.output(26,gpio.HIGH)
      gpio.output(12,gpio.HIGH)
      gpio.output(16,gpio.HIGH)
      gpio.output(20,gpio.LOW)
      gpio.output(21,gpio.HIGH)

    if zahl == 6:
      gpio.output(13,gpio.HIGH)
      gpio.output(19,gpio.HIGH)
      gpio.output(26,gpio.HIGH)
      gpio.output(12,gpio.LOW)
      gpio.output(16,gpio.HIGH)
      gpio.output(20,gpio.HIGH)
      gpio.output(21,gpio.HIGH)

  time.sleep(5)

# wg. while true, landen wir hier nie.
gpio.cleanup()


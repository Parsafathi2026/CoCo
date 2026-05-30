#!/usr/bin/env python3

from pidog import Pidog
from time import sleep

dog = Pidog()

sleep(1)

dog.speak("Security scan activated")

for _ in range(3):
    dog.head_move([[60, 0, 0], [-60, 0, 0]], speed=70)

dog.speak("Area secured")

dog.close()
#!/usr/bin/env python3

from pidog import Pidog
from time import sleep

dog = Pidog()

sleep(1)

dog.speak("Dance mode activated")

for _ in range(4):
    dog.head_move([[25, 0, 0], [-25, 0, 0]], speed=100)

dog.do_action('wag_tail')

dog.speak("Thank you, thank you!")

dog.close()
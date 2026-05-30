#!/usr/bin/env python3

from pidog import Pidog
from time import sleep

dog = Pidog()

sleep(1)

dog.speak("Beep boop. I am definitely a real dog.")

dog.head_move([[0, 20, 0], [0, -20, 0]] * 3, speed=90)

dog.do_action('wag_tail')

sleep(2)

dog.close()
#!/usr/bin/env python3

from pidog import Pidog
from time import sleep

dog = Pidog()

sleep(1)

dog.do_action('sit')
sleep(1)

dog.speak("Hello human! Nice to see you!")

dog.head_move([[30, 0, 0], [-30, 0, 0]] * 2, speed=80)

dog.do_action('wag_tail')

sleep(2)

dog.close()
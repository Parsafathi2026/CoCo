#!/usr/bin/env python3

from pidog import Pidog
from pidog.tts import Pico2Wave
from time import sleep

dog = Pidog()
tts = Pico2Wave()

sleep(1)

dog.do_action('sit')

tts.say("Good evening Alex. All systems are ready.")

dog.head_move([[20, 0, 0]], speed=80)

sleep(2)

dog.close()
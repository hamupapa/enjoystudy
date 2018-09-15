# -*- coding: utf-8 -*-

from syaku import syaku_to_cm

print("10尺=", syaku_to_cm(10), "cm")
print("20尺=", syaku_to_cm(20), "cm")

import syaku as sya

print(sya.syaku_to_cm(10))

from syaku import syaku_to_cm as s2cm
print(s2cm(10))

import random, datetime, json

from syaku import syaku, test1, test2
from syaku import syaku as s, test1 as t1, test2

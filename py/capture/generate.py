#!/usr/bin/python
# -*- coding: UTF-8 -*-

import struct
from math import sin, pi
import random

fo = open("1M", "wb")
a = 0;
for i in range(786432):
    a = (0.3 + random.randint(0,50) / 1000.0 - 0.025) * sin(2 * pi * i * 0.1 + pi / 20) * 8192 / 2.5 + 8192
    b = 0
    databuf = struct.pack('<h', a) + struct.pack('<h', b)
    fo.write(databuf)

# 关闭文件
fo.close()

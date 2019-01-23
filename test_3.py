# -*- coding: UTF-8 -*-

import math
import cmath

n = 0;
while True:
    temp_a = n+100;
    temp_b = n+268;
    sqrt_a = math.sqrt(temp_a);
    if sqrt_a.is_integer():
        sqrt_b = math.sqrt(temp_b);
        if sqrt_b.is_integer():
            print n;
    n = n+1;
import math

for i in range(100,1000):
    x = i % 10
    y = i/10 % 10
    z = i / 100
    sum = x**3 + y**3 + z**3
    # print x,y,z,sum,"-",i
    if i == (x**3) + (y**3) + (z**3): print i
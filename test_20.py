height = 100.0
times = 10
route = 0.0

route += height
height /= 2
for i in range(1,10):
    route += height*2
    height /= 2

print "The length of route is:",route
print "The height is:",height
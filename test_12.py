import math

count = 0
for i in range(101,201):
    for j in range(2,int(math.sqrt(i))+1):
        if(i%j == 0):
            break;
    else:
        print i;
        count += 1
print "total is:",count

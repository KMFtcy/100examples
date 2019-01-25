Jia = ['a', 'b', 'c']
Yi = ['x', 'y', 'z']

for i in Yi:
    for j in Yi:
        if i != j :
            for k in Yi :
                if i != k and j != k:
                    if i != 'x' and k != 'x' and k != 'z':
                        print "a<-->{},b<-->{},c<-->{}".format(i,j,k)


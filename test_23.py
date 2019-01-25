max_level = 10

for i in range(1,max_level+1):
    print " "*(max_level-i),
    print "*"*(2*i-1)
for i in range(max_level-1,0,-1):
    print " " * (max_level - i),
    print "*" * (2 * i - 1)


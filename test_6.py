
n1 = 0
n2 = 1

number = int(raw_input("how many numbers do you want to display:"))
if number <=2 : exit(0)
print n1
print n2
for i in range(number-2):
    n2 = n1 + n2
    n1 = n2 - n1
    print n2
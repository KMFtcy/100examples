import math

number = int(raw_input("Please input a number :"))
factor_list = []
n = number
upper_bound = int(math.sqrt(n)) + 1;
i = 2
while i < upper_bound:
    if (n % i == 0):
        factor_list.append(i)
        n /= i
        upper_bound = int(math.sqrt(n)) + 1;
        i = 2;
    else:
        i += 1
factor_list.append(n);

if len(factor_list) == 1:
    print "This is a prime number."
else:
    print "{} =".format(number),
    while len(factor_list) > 1:
        print factor_list.pop(), "*",
    print factor_list.pop()

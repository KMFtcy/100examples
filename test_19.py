
for number in range(2,1001):
    factor_list = []
    for i in range(1, number / 2 + 1):
        if (number % i == 0):
            factor_list.append(i)
    if len(factor_list) == 1 or len(factor_list) == 0:
        continue
    factor_sum = reduce(lambda x,y:x+y ,factor_list)
    if factor_sum == number:
        print number


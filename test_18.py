number = int(raw_input("Please input a number:"))
repeat_times = int(raw_input("Please imput repeating time:"))
sum = 0

digit_num = 0
temp_num = number
while temp_num != 0:
    temp_num /= 10
    digit_num += 1
print "sum = ",
temp_num = 0
temp_num *= 10**digit_num
temp_num += number
sum += temp_num
print "{}".format(sum),
for i in xrange(repeat_times-1):
    temp_num *= 10**digit_num
    temp_num += number
    sum += temp_num
    print "+ {}".format(temp_num),
print "=" ,sum
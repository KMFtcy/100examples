
target_n = 20

a = 1.0
b = 2.0

# fb_number_init1 = 1
# fb_number_init2 = 1
# fb_number_a = 0 # n
# fb_number_b = 0 # n-1
# fb_number_c = 0 # n-2
# for i in range(target_n-4):
#     fb_number_init2 = fb_number_init1 + fb_number_init2
#     fb_number_init1 = fb_number_init2 - fb_number_init1
# fb_number_c = fb_number_init2
# fb_number_b = fb_number_init2 + fb_number_init1
# fb_number_a = fb_number_b + fb_number_init2
#
# denominator = fb_number_c*a+fb_number_b*b
# element = fb_number_b*a+fb_number_a*b
# print "the a20 is:{}/{} = {}".format(element,denominator,float(element)/denominator)

sum = 0.0
for i in range(target_n):
    sum += b/a
    b = a+b
    a = b-a
print sum


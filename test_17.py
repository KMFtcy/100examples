s = raw_input("Please input a string:")

letter_num = 0;
space_num = 0
digit_num = 0
others_num = 0
for i in s:
    if i.isalpha():
        letter_num +=1
    elif i.isspace():
        space_num +=1
    elif i.isdigit():
        digit_num += 1
    else:
        others_num += 1

print "Letter:",letter_num
print "Space:",space_num
print "Digit:",digit_num
print "Others",others_num
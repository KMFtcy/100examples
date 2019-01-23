def return_days(month,year):
    month_dic = {
        1 : 31,
        20 : 28,
        21 : 29,
        3 : 31,
        4 : 30,
        5: 31,
        6: 30,
        7: 31,
        8: 31,
        9: 30,
        10: 31,
        11: 30,
        12: 31,
    }
    if month == 2:
        if is_special_year(year):
            month = 21;
        else:
            month = 20;
    return month_dic[month]

def is_special_year(year):
    if (year % 400 == 0) or ((year % 4 == 0) and (year % 100 != 0)):
        return True;
    return False;


year = int(raw_input('year:'));
month = int(raw_input('month:'));
day = int(raw_input('day:'));

month -= 1;
sum_day = 0;
for i in range(month):
    sum_day += return_days(month ,year);
    month -= 1;
sum_day += day;
print sum_day


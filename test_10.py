import time

this_time = time.localtime(time.time());

print time.strftime("%Y-%m-%d %H:%M:%S ",this_time)
print "Pause 1 sec"
time.sleep(1)
print time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(time.time()))
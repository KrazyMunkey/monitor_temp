import os
import time

def measure_temp():
	temp = os.popen("vcgencmd measure_temp").readline()
	temp = temp.replace("temp=", "").replace("'C\n", "").replace(" ", "")
	return(float(temp))

while True:
	print(measure_temp())
	time.sleep(2)

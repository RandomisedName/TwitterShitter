
def check_temp():	#return temp. yours Rpi
	cmd = '/opt/vc/bin/vcgencmd measure_temp'
	line = os.popen(cmd).readline().strip()
	temp = line.split('=')[1].split("'")[0]
	return temp


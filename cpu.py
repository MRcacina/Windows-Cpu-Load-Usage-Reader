import os
import time
import os

cmd = 'title Cpu Usage'
os.system(cmd)
cmd2 = 'color a'
os.system(cmd2)

def get_cpu_load():
    result = []
    cmd = "WMIC CPU GET LoadPercentage "
    response = os.popen(cmd + ' 2>&1','r').read().strip().split("\r\n")
    for load in response[1:]:
       result.append(int(load))
    return result

while True:
    print get_cpu_load()[0]
    time.sleep(1)
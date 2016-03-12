# !/usr/bin/python
import sys, getopt, io, os
usage = "odroid-fan-controller.py [-m,--mode <0,1>,<'auto','manual'>] [-s, --speed <25-100>] "
usage += "[-v]"
# odroid-xu4 device paths
odroid_device_path = '/sys/devices/odroid_fan.13/'
odroid_pwm_duty_file = 'pwm_duty'
odroid_fan_mode_file = 'fan_mode'
# odroid_fan_file_mode = 0 is manual fan mode
# odroid_fan_file_mode = 1 is auto fan mode
odroid_fan_file_mode = 0
odroid_fan_mode = ['manual', 'auto']
# odroid_pwm_duty_file: 0 is off, 255 is 100% fan power
# fan speed = [0 - 100]% * 2.55
odroid_fan_speed = 0

def main(argv):
    getfanspeed()
    getfanmode()
    try:
       opts, args = getopt.getopt(argv,"hm:s:p:v",["mode=","speed="])
    except getopt.GetoptError:
       print usage
       sys.exit(2)
    for opt, arg in opts:
      if opt in ("-h", "--help"):
          print usage
          sys.exit()
      elif opt in ("-s", "--speed"):
          setfanspeed(float(arg))
      elif opt in ("-m", "--mode"):
          setfanmode(arg)
      elif opt == "-v":
          status()
def status():
    print "Fan Speed: {0}%".format(getfanspeed())
    print "Fan Mode: {0}".format(getfanmode())
def setfanspeed(speed):
    # check fan mode
    if getfanmode() == 'manual':
        if speed < 25:
            print 'Fan power below 25% causes a malfunction with the odroid fan. Returning.'
            return
        odroid_fan_speed = speed
        speed = speed * 2.55
        writetofile(odroid_pwm_duty_file, speed)
    elif getfanmode() == 'auto':
        print 'Fan Mode set to "auto".\r\nPlease set to "manual" and try again.'
def setfanmode(mode):
    if mode == "auto":
        mode == 1
    elif mode == "manual":
        mode == 0

    if mode is '1' or mode is '0':
        if getfanmode() == mode:
            print 'Fan mode already set to {0}'.format(mode)
        writetofile(odroid_fan_mode_file, mode)
    else:
        print 'Invalid mode: {0}'.format(mode)
def getfanmode():
    mode = readfile(odroid_fan_mode_file)
    odroid_fan_mode = 'manual' if 'manual' in mode else 'auto'
    return odroid_fan_mode
def getfanspeed():
    odroid_fan_speed = (float(readfile(odroid_pwm_duty_file)) / 2.55)
    if int(odroid_fan_speed) == 0:
        odroid_fan_speed = 0
    return odroid_fan_speed
def writetofile(filePath, data):
    filePath = os.path.join(odroid_device_path, filePath)
    with open(filePath, 'w') as dataFile:
        dataFile.write(str(data))
def readfile(filePath):
    filePath = os.path.join(odroid_device_path, os.path.join(odroid_device_path, filePath))
    data = ''
    with open(filePath, 'r') as dataFile:
        data = dataFile.read()
        return data

if __name__ == '__main__':
    main(sys.argv[1:])

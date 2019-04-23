# !/usr/bin/python
import sys, getopt, os

from .constants import *

usage = "odroid-fan-controller.py [-m,--mode <0,1>,<'auto','manual'>] [-s, --speed <25-100>] "
usage += "[-v]"


def main(argv):
    get_fan_mode()
    get_fan_mode()

    try:
        opts, args = getopt.getopt(argv, "hm:s:p:v", ["mode=", "speed="])
    except getopt.GetoptError:
        sys.exit(2)
    for opt, arg in opts:
        if opt in ("-h", "--help"):
            print(usage)
            sys.exit()
        elif opt in ("-s", "--speed"):
            set_fan_speed(float(arg))
        elif opt in ("-m", "--mode"):
            set_fan_mode(arg)
        elif opt == "-v":
            status()


def status():
    print("Fan Speed: {0}%".format(get_fan_mode()))
    print("Fan Mode: {0}".format(get_fan_mode(str=True)))


def set_fan_speed(speed):
    # check fan mode
    if get_fan_mode() == 'manual':
        if speed < 25:
            print('Fan power below 25% causes a malfunction with the ODROID fan. Cancelling.')
            return

        speed = speed * 2.55

        write_to_file(odroid_pwm_duty_file, speed)
    elif get_fan_mode() == 'auto':
        print('Fan Mode set to "auto".\r\nPlease set to "manual" and try again.')


def set_fan_mode(fanmode):
    _mode = fanmode
    if (_mode == 'auto'):
        _mode = '1'
    elif (_mode == 'manual'):
        _mode = '0'
    print('_mode: {0}'.format(_mode))
    if (_mode == '1') or (_mode == '0'):
        print('get_fan_mode(str=False): {0}'.format(get_fan_mode()))
        if get_fan_mode(str=False) == _mode:
            print('Fan mode already set to {0}'.format(fanmode))
            return
        write_to_file(odroid_fan_mode_file, _mode)
        print('_mode: {0} written to {1}'.format(_mode, odroid_fan_mode_file))
        print('get_fan_mode(str=False)(after write): {0}'.format(get_fan_mode(str=False)))
    else:
        print('Invalid mode: {0}'.format(_mode))


def get_fan_mode(str=True):
    def number(mode):
        return '1' if 'auto' in mode else 'manual'

    mode = read_file(odroid_fan_mode_file)
    odroid_fan_mode = 'manual' if 'manual' in mode else 'auto'
    if str:
        return odroid_fan_mode
    else:
        return number(odroid_fan_mode)


def get_fan_speed():
    odroid_fan_speed = (float(read_file(odroid_pwm_duty_file)) / 2.55)
    if int(odroid_fan_speed) == 0:
        odroid_fan_speed = 0
    return odroid_fan_speed


def write_to_file(filePath, data):
    filePath = os.path.join(odroid_device_path, filePath)
    with open(filePath, 'w') as dataFile:
        dataFile.write(str(data))


def read_file(filePath):
    filePath = os.path.join(odroid_device_path, os.path.join(odroid_device_path, filePath))
    data = ''
    with open(filePath, 'r') as dataFile:
        data = dataFile.read()
        return data


if __name__ == '__main__':
    main(sys.argv[1:])

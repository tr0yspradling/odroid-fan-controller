
# odroid-fan-controller
A command line fan speed controller for ODROID XU3/XU4 models.

# Usage
Use `python odroid-fan-controller.py -m 0` to set the fan to: `manual` mode

Use `python odroid-fan-controller.py -s 100` to set the fan to: `100%`

Set the fan speed from 25%-100%. Below 25% the fan starts making a weird noise.

# How it works
ODROID controls the fan with a couple of files in `/sys/devices/odroid_fan.13/`

# Special Files
`/sys/devices/odroid_fan.13/pwm_duty` is a special file that takes an integer 0 - 255. 255 being the 100% power.

`/sys/devices/odroid_fan.13/fan_mode` specifies manual or automatic mode.

# Manual fan control without odroid-fan-controller
`echo 0 > /sys/devices/odroid_fan.13/fan_mode` turns the fan to manual mode.

`echo 255 > /sys/devices/odroid_fan.13/pwm_duty` gives the fan 100% power.

`echo 1 > /sys/devices/odroid_fan.13/fan_mode` turns the fan back to auto mode.

# License
The MIT License (MIT)
Copyright (c) 2016 Troy Spradling

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.

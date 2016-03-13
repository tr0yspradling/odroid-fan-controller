
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

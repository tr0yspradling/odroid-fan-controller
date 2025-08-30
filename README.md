
# odroid-fan-controller
A command line fan speed controller for ODROID XU3/XU4 models.

# Usage
After installing the package, use the CLI entrypoint `odroid_fan_controller`.

- Get current status:
  `odroid_fan_controller status`

- Get or set mode:
  - `odroid_fan_controller mode` → prints `auto` or `manual`
  - `odroid_fan_controller mode manual` → switch to manual
  - `odroid_fan_controller mode auto` → switch to auto

- Get or set speed (25–100%):
  - `odroid_fan_controller speed` → prints current percentage
  - `odroid_fan_controller speed 60` → set to 60% (requires manual mode)
  - `odroid_fan_controller speed 60 --force-manual` → switch to manual then set

Notes:
- The ODROID fan makes noise below ~25%, so values under 25% are rejected.
- For testing, you can override the device sysfs path with `--device-path` or env var `ODROID_FAN_DEVICE_PATH`.

# How it works
ODROID controls the fan with a couple of special files in `/sys/devices/odroid_fan.13/`

    `/sys/devices/odroid_fan.13/pwm_duty` takes an integer 0 - 255. 255 being the 100% power.

    `/sys/devices/odroid_fan.13/fan_mode` specifies manual or automatic mode.

# Manual fan control without odroid-fan-controller
`echo 0 > /sys/devices/odroid_fan.13/fan_mode` turns the fan to manual mode.

`echo 255 > /sys/devices/odroid_fan.13/pwm_duty` gives the fan 100% power.

`echo 1 > /sys/devices/odroid_fan.13/fan_mode` turns the fan back to auto mode.

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

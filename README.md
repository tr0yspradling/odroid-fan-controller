
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
  Copyright (c) 2016, Troy Spradling
  All rights reserved.

  Redistribution and use in source and binary forms, with or without modification, are permitted provided that the following conditions are met:

  1. Redistributions of source code must retain the above copyright notice, this list of conditions and the following disclaimer.

  2. Redistributions in binary form must reproduce the above copyright notice, this list of conditions and the following disclaimer in the documentation and/or other materials provided with the distribution.

  3. Neither the name of the copyright holder nor the names of its contributors may be used to endorse or promote products derived from this software without specific prior written permission.

  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS" AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF THE POSSIBILITY OF SUCH DAMAGE.

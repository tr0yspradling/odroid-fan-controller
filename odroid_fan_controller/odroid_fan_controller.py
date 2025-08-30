#!/usr/bin/env python
import os
from .constants import (
    odroid_device_path as DEFAULT_DEVICE_PATH,
    odroid_pwm_duty_file,
    odroid_fan_mode_file,
)


def _join(device_path, filename):
    return os.path.join(device_path, filename)


def _write(path, data):
    with open(path, 'w') as fh:
        fh.write(str(data))


def _read(path):
    with open(path, 'r') as fh:
        return fh.read()


def get_fan_mode(as_string=True, device_path=None):
    """Return current fan mode.

    - When as_string=True: returns 'auto' or 'manual'.
    - When as_string=False: returns '1' (auto) or '0' (manual).
    """
    base = device_path or DEFAULT_DEVICE_PATH
    raw = _read(_join(base, odroid_fan_mode_file)).strip().lower()
    # Support either numeric or string content in sysfs
    is_auto = raw == '1' or 'auto' in raw
    mode_str = 'auto' if is_auto else 'manual'
    if as_string:
        return mode_str
    return '1' if mode_str == 'auto' else '0'


def set_fan_mode(mode, device_path=None):
    """Set fan mode to 'auto' or 'manual'. Returns resulting mode string."""
    base = device_path or DEFAULT_DEVICE_PATH
    normalized = str(mode).strip().lower()
    if normalized in ('1', 'auto'):
        value = '1'
        result = 'auto'
    elif normalized in ('0', 'manual'):
        value = '0'
        result = 'manual'
    else:
        raise ValueError("Invalid mode. Use 'auto'/'manual' or '1'/'0'.")

    current = get_fan_mode(as_string=False, device_path=base)
    if current == value:
        return result
    _write(_join(base, odroid_fan_mode_file), value)
    return get_fan_mode(as_string=True, device_path=base)


def get_fan_speed(device_path=None):
    """Return current fan speed percentage (0-100)."""
    base = device_path or DEFAULT_DEVICE_PATH
    raw = _read(_join(base, odroid_pwm_duty_file)).strip()
    try:
        duty = float(raw)
    except ValueError:
        # Treat non-numeric as 0
        duty = 0.0
    pct = duty / 2.55
    if int(pct) == 0:
        return 0
    return round(pct, 1)


def set_fan_speed(percent, device_path=None, allow_auto_switch=False):
    """Set fan speed percentage (25-100). Returns resulting percent.

    - Requires manual mode, unless allow_auto_switch=True, in which case we
      switch to manual before setting.
    """
    base = device_path or DEFAULT_DEVICE_PATH
    try:
        pct = float(percent)
    except (TypeError, ValueError):
        raise ValueError('Speed must be a number between 25 and 100.')

    if pct < 25 or pct > 100:
        raise ValueError('Speed must be between 25 and 100 percent.')

    mode = get_fan_mode(device_path=base)
    if mode != 'manual':
        if allow_auto_switch:
            set_fan_mode('manual', device_path=base)
        else:
            raise RuntimeError('Fan is in auto mode. Switch to manual before setting speed.')

    duty = pct * 2.55
    _write(_join(base, odroid_pwm_duty_file), duty)
    return get_fan_speed(device_path=base)


def status(device_path=None):
    """Return a dictionary with current mode and speed."""
    base = device_path or DEFAULT_DEVICE_PATH
    return {
        'mode': get_fan_mode(device_path=base),
        'speed': get_fan_speed(device_path=base),
    }

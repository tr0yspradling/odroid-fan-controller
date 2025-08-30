#!/usr/bin/env python
# -*- coding: utf-8 -*-

"""Tests for `odroid_fan_controller` package CLI and core functions."""

import os
import tempfile
from click.testing import CliRunner

from odroid_fan_controller import cli


def make_fake_device(tmpdir):
    # Start in manual mode with 0% duty
    with open(os.path.join(tmpdir, 'fan_mode'), 'w') as f:
        f.write('0')
    with open(os.path.join(tmpdir, 'pwm_duty'), 'w') as f:
        f.write('0')


def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli.main, ['--help'])
    assert result.exit_code == 0
    assert 'status' in result.output
    assert 'mode' in result.output
    assert 'speed' in result.output


def test_status_and_mode_and_speed_commands():
    runner = CliRunner()
    with tempfile.TemporaryDirectory() as td:
        make_fake_device(td)

        # status should show manual and 0%
        res = runner.invoke(cli.main, ['--device-path', td, 'status'])
        assert res.exit_code == 0
        assert 'Fan Mode: manual' in res.output
        assert 'Fan Speed: 0%' in res.output

        # get mode prints just the mode
        res = runner.invoke(cli.main, ['--device-path', td, 'mode'])
        assert res.exit_code == 0
        assert res.output.strip() == 'manual'

        # set mode to auto
        res = runner.invoke(cli.main, ['--device-path', td, 'mode', 'auto'])
        assert res.exit_code == 0
        assert 'Mode set to auto' in res.output

        # setting speed in auto without force should error
        res = runner.invoke(cli.main, ['--device-path', td, 'speed', '50'])
        assert res.exit_code != 0
        assert 'auto mode' in res.output

        # force manual and set speed
        res = runner.invoke(
            cli.main, ['--device-path', td, 'speed', '50', '--force-manual']
        )
        assert res.exit_code == 0
        assert 'Speed set to 50%' in res.output

"""Console interface for odroid_fan_controller."""
import sys
import click

from .odroid_fan_controller import (
    status as api_status,
    get_fan_mode,
    set_fan_mode,
    get_fan_speed,
    set_fan_speed,
)


class DevicePathOption(click.Option):
    pass


@click.group()
@click.option(
    '--device-path',
    envvar='ODROID_FAN_DEVICE_PATH',
    metavar='PATH',
    default=None,
    help='Override the ODROID fan device directory (for testing).',
)
@click.pass_context
def main(ctx, device_path):
    """Manage ODROID XU3/XU4 fan mode and speed."""
    ctx.ensure_object(dict)
    ctx.obj['device_path'] = device_path


@main.command()
@click.pass_context
def status(ctx):
    """Show current fan mode and speed."""
    info = api_status(device_path=ctx.obj.get('device_path'))
    click.echo(f"Fan Mode: {info['mode']}")
    click.echo(f"Fan Speed: {int(info['speed'])}%")


@main.command()
@click.argument('mode', required=False, type=click.Choice(['auto', 'manual']))
@click.pass_context
def mode(ctx, mode):
    """Get or set fan mode (auto/manual)."""
    base = ctx.obj.get('device_path')
    if mode is None:
        click.echo(get_fan_mode(device_path=base))
        return
    result = set_fan_mode(mode, device_path=base)
    click.echo(f"Mode set to {result}")


@main.command()
@click.argument('percent', required=False, type=float)
@click.option('--force-manual', is_flag=True, help='Switch to manual before setting speed.')
@click.pass_context
def speed(ctx, percent, force_manual):
    """Get or set fan speed percentage (25-100)."""
    base = ctx.obj.get('device_path')
    if percent is None:
        click.echo(f"{int(get_fan_speed(device_path=base))}%")
        return
    try:
        value = set_fan_speed(percent, device_path=base, allow_auto_switch=force_manual)
    except (ValueError, RuntimeError) as exc:
        raise click.ClickException(str(exc))
    click.echo(f"Speed set to {int(value)}%")


if __name__ == "__main__":
    sys.exit(main())  # pragma: no cover

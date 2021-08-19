from types import resolve_bases
import click
import subprocess


class AliasedGroup(click.Group):
    """Class to add aliases to the commands"""

    def get_command(self, ctx, cmd_name):
        try:
            cmd_name = ALIASES[cmd_name].name
        except KeyError:
            pass
        return super().get_command(ctx, cmd_name)


def run_subprocess(command):
    """Run commands as a subprocess using subprocess

    Args:
        command: list

    Returns:
        result: subprocess result object
    """
    result = subprocess.run(command, capture_output=True, text=True)
    return result


@click.group(cls=AliasedGroup, invoke_without_command=True)
@click.option("--version", "-v", required=False, is_flag=True, help="Version details")
def easy_edit_main(version):

    click.secho(
        r"""
                                     ___ __
  ___  ____ ________  __   ___  ____/ (_) /_____  _____
 / _ \/ __ `/ ___/ / / /  / _ \/ __  / / __/ __ \/ ___/
/  __/ /_/ (__  ) /_/ /  /  __/ /_/ / / /_/ /_/ / /
\___/\__,_/____/\__, /   \___/\__,_/_/\__/\____/_/
               /____/

    """,
        fg="green",
        bold=True,
    )
    if version:
        click.secho("Version 0.1.0")
    else:
        click.secho(
            r"""
Usage: easy_edit.py [OPTIONS] COMMAND [ARGS]...

Options:
  -v, --version  Version details  [required]
  --help         Show this message and exit.

Commands:
  play  Play your videos with easy editor
        """
        )


@easy_edit_main.command(name="play", help="Play your videos with easy editor")
@click.option(
    "--input",
    "-i",
    required=True,
    is_flag=True,
    help="Pass your input video file to play",
)
@click.argument("input_file", nargs=1, required=True)
def play(input, input_file):
    """Play your videos with easy editor

    Usage: easy_edit.py play [OPTIONS] INPUT_FILE

    Options:
    -i, --input  Pass your input video file to play  [required]
    --help       Show this message and exit.
    """
    if input:
        command = ["ffplay", "-i", input_file]
        result = run_subprocess(command)
        if result.stderr:
            error_msg = f"Error while playing video {input_file}"
            click.secho(error_msg, fg="red", bold=True)


# list of alias commands
ALIASES = {"view": play}

if __name__ == "__main__":
    easy_edit_main()

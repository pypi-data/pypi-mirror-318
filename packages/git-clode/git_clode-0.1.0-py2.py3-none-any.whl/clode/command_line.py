import re
import subprocess


class CommandException(Exception):
    def __init__(self, returncode: int, command_args: list[str], stderr: str | None):
        self.returncode = returncode
        self.command_args = command_args
        self.stderr = stderr


def run_command(*args: str | None) -> str | None:
    """Run a console command and return stdout"""
    filtered_args: list[str] = [arg for arg in args if arg is not None]
    result = subprocess.run(filtered_args, shell=True)
    if result.returncode != 0:
        raise CommandException(
            result.returncode,
            filtered_args,
            result.stderr.decode() if result.stderr is not None else None,  # type: ignore
        )
    if result.stdout is not None:  # type: ignore
        return result.stdout.decode()


def get_clone_output(url: str) -> str:
    m = re.search(r"(?<=\/)[^\/]+?(?=(\.git)?$)", url)
    if m is None:
        raise Exception(f"Invalid git repository url: {url}")
    return m.group(0)


def clone(url: str, path: str):
    """Clone a git repository from `url` into `path`"""
    run_command("git", "clone", url, path)


def code(path: str):
    """Open a directory in VSCode"""
    run_command("code", path)

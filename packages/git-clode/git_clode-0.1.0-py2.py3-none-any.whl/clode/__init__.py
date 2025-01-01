import argparse
from .clode import clode, ShouldOpen
import colorama

colorama.init()


def parse_arguments() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        prog="clode",
        description="CLI tool to open git repositories quickly",
    )
    parser.add_argument(
        "repository", type=str, help="url or name of repository to clone"
    )
    parser.add_argument(
        "directory",
        type=str,
        nargs="?",
        help="the name of a new directory to clone into",
    )

    # Flags
    should_open_group = parser.add_mutually_exclusive_group()
    should_open_group.add_argument(
        "-n",
        "--never-open",
        action="store_true",
        help="don't open after cloning",
    )
    should_open_group.add_argument(
        "-a", "--always-open", action="store_true", help="open even if already cloned"
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    should_open = (
        ShouldOpen.always
        if args.always_open
        else (ShouldOpen.never if args.never_open else ShouldOpen.cloned)
    )
    clode(args.repository, args.directory, should_open=should_open)


if __name__ == "__main__":
    main()

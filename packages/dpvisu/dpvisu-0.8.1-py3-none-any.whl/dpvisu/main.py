#!/usr/bin/env python

# Requires GraphWiz to be installed and added to the system PATH:
# https://graphviz.org/download/

import argparse
import logging
import os
import shlex
import sys
from pathlib import Path

from .datapack_visualizer import generate

# Debug logging toggle
logging.basicConfig(format="", level=logging.DEBUG)


def parse_cli():
    parser = argparse.ArgumentParser(
        description="Generates a call given one or more datapacks."
    )
    parser.add_argument(
        "input",
        metavar="datapack-paths",
        type=Path,
        nargs="*",
        help='Path to a specific datapack or a ".../datapacks/" folder.',
        default=None,
    )
    parser.add_argument(
        "--output",
        "-o",
        metavar="output_file",
        type=str,
        nargs="?",
        help='Output file. Defaults to "datapack" if unspecified.',
        default="datapack",
    )
    parser.add_argument(
        "--format",
        "-f",
        metavar="format",
        type=str,
        help='Output format (svg/png/pdf/...). "svg" compiles fastest. To generate multiple different formats at once, comma-separate them like `svg,pdf,...`.',
        default="svg",
    )
    is_posix = os.name == "posix"
    if len(sys.argv) > 1:
        # Argparse requires comma separated arguments, but to deal with paths including spaces, it has to run through shlex first
        args = parser.parse_args(shlex.split(" ".join(sys.argv[1:]), posix=is_posix))
    else:
        # Argparse requires comma separated arguments, but to deal with paths including spaces, it has to run through shlex first
        args = parser.parse_args(
            shlex.split(
                input("Enter the root folder(s) of your datapack(s): "), posix=is_posix
            )
        )
    return args


def run():
    args = parse_cli()
    generate(args.input, format=args.format, output_file=args.output)


if __name__ == "__main__":
    run()

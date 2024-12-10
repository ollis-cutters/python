#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# vim: set autoindent smartindent softtabstop=4 tabstop=4 shiftwidth=4 expandtab:
from __future__ import print_function, with_statement, unicode_literals, division, absolute_import

__author__ = "{{ cookiecutter.full_name }}"
__copyright__ = "{% now 'utc', '%Y' %} {{ cookiecutter.full_name }} ({{ cookiecutter.domain }}), under the terms of the UNLICENSE"
__version__ = "{{cookiecutter.version}}"
__compatible__ = ((3, 7), (3, 8), (3, 9), (3, 10), (3, 11),)  # fmt: skip
__doc__ = """
===============================
 {{cookiecutter.project_name}}
===============================

{{cookiecutter.project_short_description}}
"""
import argparse

# import os
# import re
import sys

# from contextlib import suppress
# from copy import deepcopy
from functools import partial  # also cache
from pathlib import Path

# from pprint import pformat, pprint
# from typing import Optional

eprint = partial(print, file=sys.stderr)

# Checking for compatibility with Python version
if sys.version_info[:2] not in __compatible__:
    sys.exit(f"This script is only compatible with the following Python versions: {', '.join([f'{z[0]}.{z[1]}' for z in __compatible__])}")  # pragma: no cover

CONFIG_DEFAULTS = """
#[foobar]
#baz = %(thisdir)s/bla.txt
"""


def parse_options() -> argparse.Namespace:
    """\
        Initializes the ArgumentParser and ConfigParser and performs the parsing
    """
    from argparse import ArgumentParser
    from configparser import ConfigParser
    from textwrap import dedent

    cfgname = Path(__file__).absolute().with_suffix(".ini")
    cfg = ConfigParser(defaults={"thisdir": cfgname.parent}, delimiters=("=",))
    cfg.read_string(dedent(CONFIG_DEFAULTS), "<DEFAULTS>")
    parser = ArgumentParser(description="{{cookiecutter.project_short_description}}", add_help=False)
    # Only add the configuration file argument for starters
    parser.add_argument("-c", "--config", "--ini", action="store", default=cfgname, metavar="CFG", type=Path, help=f"The config file; defaults to {cfgname}")
    partial_args = parser.parse_known_args()[0]
    cfg.read(partial_args.config)

    # Remaining command line options
    parser.add_argument("-h", "--help", action="help", help="Show this help message and exit")
    parser.add_argument("--nologo", action="store_const", dest="nologo", const=True, help="Don't show info about this script.")
    parser.add_argument("-v", "--verbose", action="count", default=0, help="Turn up verbosity to see more details of what is going on.")
    return cfg, parser.parse_args()


def main() -> int:
    """\
        Very simply the main entry point to this script
    """
    return 0


if __name__ == "__main__":
    global args
    global cfg
    cfg, args = parse_options()
    try:
        sys.exit(main())
    except SystemExit:
        pass
    except ImportError:
        raise  # re-raise
    except RuntimeError:
        raise  # re-raise
    except Exception:
        eprint(__doc__)
        raise  # re-raise

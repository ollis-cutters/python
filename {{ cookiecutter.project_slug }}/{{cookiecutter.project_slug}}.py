#!/usr/bin/env python
# -*- coding: utf-8 -*-
# vim: set autoindent smartindent softtabstop=4 tabstop=4 shiftwidth=4 expandtab:
from __future__ import print_function, with_statement, unicode_literals, division, absolute_import

__author__ = "{{ cookiecutter.full_name }}"
__copyright__ = "{% now 'utc', '%Y' %} {{ cookiecutter.full_name }} ({{ cookiecutter.domain }}), under the terms of the UNLICENSE"
__version__ = "{{cookiecutter.version}}"
__compatible__ = (
    (3, 7),
    (3, 8),
    (3, 9),
    (3, 10),
    (3, 11),
)
__doc__ = """
=========
 PROGRAM
=========
"""
import argparse  # noqa: F401
import os  # noqa: F401
import sys

# Checking for compatibility with Python version
if not sys.version_info[:2] in __compatible__:
    sys.exit(
        "This script is only compatible with the following Python versions: %s."
        % (", ".join(["%d.%d" % (z[0], z[1]) for z in __compatible__]))
    )  # pragma: no cover


def parse_args():
    """ """
    from argparse import ArgumentParser

    parser = ArgumentParser(description="PROGRAM")
    parser.add_argument(
        "--nologo", action="store_const", dest="nologo", const=True, help="Don't show info about this script."
    )
    return parser.parse_args()


def main(**kwargs):
    """ """
    return 0


if __name__ == "__main__":
    args = parse_args()
    try:
        sys.exit(main(**vars(args)))
    except SystemExit:
        pass
    except ImportError:
        raise  # re-raise
    except RuntimeError:
        raise  # re-raise
    except Exception:
        print(__doc__)
        raise  # re-raise

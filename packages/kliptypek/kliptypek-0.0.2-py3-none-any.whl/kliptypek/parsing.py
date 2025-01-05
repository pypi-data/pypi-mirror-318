# coding: utf-8

import argparse
from kliptypek import __version__


def get_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="kliptypek is clipboard typer. Insert text from clipboard using simulated typing. ")

    parser.add_argument("--version", action="version", version=f"V{__version__}", help="Check version. ")

    parser.add_argument("--clip_text", type=str, default=None,
                        help="Define the typed text explicitly, rather than using the clipboard. ")

    parser.add_argument("--delay_before", type=int, default=3000,
                        help="Set a delay in milliseconds before printing.")

    parser.add_argument("--delay_between", type=int, default=50,
                        help="Set a delay in milliseconds between keystrokes. ")

    parser.add_argument("--delay_between_up_down", type=int, default=5,
                        help="Set a delay in milliseconds between key down and key up. ")

    parser.add_argument("--terminal_duplicate", default=False, action="store_true",
                              help="Duplicate text in the terminal. ")

    parser.add_argument("--print_unicode_special", default=False, action="store_true",
                              help="Print special unicode characters with a description of what they will do. "
                                   "And exit. ")

    parser.add_argument("--ignore_unicode_special", default=False, action="store_true",
                              help="Ignore special unicode characters from --print_unicode_special "
                                   "and treat them as regular unicode characters")

    args = parser.parse_args()

    return args

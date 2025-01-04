"""
cli.py: Main entry point for micropytest with REAL-TIME console output.
Imports the core logic from micropytest.core.
"""

import os
import sys
import argparse
import logging
from collections import Counter

try:
    from colorama import init as colorama_init, Fore, Style
    colorama_init(autoreset=True)
except ImportError:
    class _FallbackFore:
        RED = GREEN = YELLOW = MAGENTA = CYAN = ""
    class _FallbackStyle:
        RESET_ALL = ""
    Fore = _FallbackFore()
    Style = _FallbackStyle()

from . import __version__
from .core import (
    create_live_console_handler,
    SimpleLogFormatter,
    run_tests
)

def console_main():
    parser = argparse.ArgumentParser(
        prog="micropytest",
        description="micropytest - 'pytest but smaller, simpler, and smarter'."
    )
    # Add a --version flag for quick version check
    parser.add_argument("--version", action="store_true",
                        help="Show micropytest version and exit.")

    parser.add_argument("path", nargs="?", default=".")
    parser.add_argument("-v", "--verbose", action="store_true", help="More logs.")
    parser.add_argument("-q", "--quiet",   action="store_true", help="Quiet mode.")
    args = parser.parse_args()

    # If --version is requested, just print it and exit
    if args.version:
        print(__version__)
        sys.exit(0)

    if args.verbose and args.quiet:
        parser.error("Cannot use both -v and -q together.")

    # root logger
    root_logger = logging.getLogger()

    # Attach a 'live' console handler
    live_format = SimpleLogFormatter()
    live_handler = create_live_console_handler(formatter=live_format)
    root_logger.addHandler(live_handler)

    # Set the level based on -v/-q
    if args.verbose:
        root_logger.setLevel(logging.DEBUG)
    elif args.quiet:
        # Log level above CRITICAL => effectively no logs
        root_logger.setLevel(logging.CRITICAL + 1)
    else:
        root_logger.setLevel(logging.INFO)

    # Show estimates only if not quiet
    show_estimates = not args.quiet

    logging.info("micropytest version: {}".format(__version__))

    # Call our core runner
    test_results = run_tests(tests_path=args.path, show_estimates=show_estimates)

    if args.quiet:
        # Summarize quietly
        passed = sum(r["status"] == "pass" for r in test_results)
        total = len(test_results)
        log_counter = Counter()
        for outcome in test_results:
            for (lvl, msg) in outcome["logs"]:
                log_counter[lvl] += 1
        warnings_count = log_counter["WARNING"]
        errors_count = log_counter["ERROR"] + log_counter["CRITICAL"]

        if total > 0:
            pct_pass = int((passed / float(total)) * 100)
        else:
            pct_pass = 0

        if pct_pass == 100:
            pct_color = Fore.GREEN
        elif pct_pass > 50:
            pct_color = Fore.YELLOW
        else:
            pct_color = Fore.RED

        ratio_str = "{}{}/{}{}".format(pct_color, passed, total, Style.RESET_ALL)
        pct_str = "{}{}%{}".format(pct_color, pct_pass, Style.RESET_ALL)

        text = "Tests: {} passed ({}) - ".format(pct_str, ratio_str)
        warn_err_text = []
        if warnings_count > 0:
            warn_err_text.append("{}{} warnings{}".format(Fore.YELLOW, warnings_count, Style.RESET_ALL))
        if errors_count > 0:
            warn_err_text.append("{}{} errors{}".format(Fore.RED, errors_count, Style.RESET_ALL))
        if not warn_err_text:
            warn_err_text.append("{}All perfect :){}".format(Fore.GREEN, Style.RESET_ALL))

        text += ", ".join(warn_err_text)
        print(text)
        return

    # Otherwise, the final fancy ASCII summary
    print(r"""
        _____    _______        _
       |  __ \  |__   __|      | |
  _   _| |__) |   _| | ___  ___| |_
 | | | |  ___/ | | | |/ _ \/ __| __|
 | |_| | |   | |_| | |  __/\__ \ |_
 | ._,_|_|    \__, |_|\___||___/\__|
 | |           __/ |
 |_|          |___/           Report
 """)

    for outcome in test_results:
        status = outcome["status"]
        if status == "pass":
            color_status = Fore.GREEN + "PASS"
        else:
            color_status = Fore.RED + "FAIL"

        duration_s = outcome["duration_s"]
        # Replace f-string with .format()
        testkey = "{}::{}".format(
            os.path.basename(outcome["file"]),
            outcome["test"]
        )

        print("{:50s} - {}{} in {:.3f}s".format(testkey, color_status, Style.RESET_ALL, duration_s))

        if args.verbose:
            for (lvl, msg) in outcome["logs"]:
                print("  {}".format(msg))
            if outcome["artifacts"]:
                print("  Artifacts: {}".format(outcome["artifacts"]))
            print()

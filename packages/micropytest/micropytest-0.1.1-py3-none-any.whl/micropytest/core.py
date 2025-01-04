# core.py
"""
core.py - Contains the core logic for micropytest:
 - test discovery
 - run_tests
 - logging context/handlers
 - storing durations in .micropytest.json

Users who want a programmatic approach can just import run_tests(),
and won't need to deal with the CLI or argument parsing.
"""

import logging
import sys
import os
import json
import traceback
import inspect
import time
from datetime import datetime
from collections import Counter

try:
    from pathlib import Path
except ImportError:
    # If Python 3.4 doesn't have pathlib by default in your environment,
    # you may need a backport (e.g. 'pip install pathlib').
    # But Python 3.4 *should* include pathlib in the standard library.
    raise ImportError("pathlib is required but not found. Install it or upgrade your Python version.")

import importlib.util

from . import __version__

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

CONFIG_FILE = ".micropytest.json"


class LiveFlushingStreamHandler(logging.StreamHandler):
    """
    A stream handler that flushes logs immediately, giving real-time console output.
    """
    def emit(self, record):
        super(LiveFlushingStreamHandler, self).emit(record)
        self.flush()


def create_live_console_handler(formatter=None, level=logging.INFO):
    handler = LiveFlushingStreamHandler(stream=sys.stdout)
    if formatter:
        handler.setFormatter(formatter)
    handler.setLevel(level)
    return handler


class TestContext:
    """
    A context object passed to each test if it accepts 'ctx'.
    Allows logging via ctx.debug(), etc. and storing artifacts.
    """
    def __init__(self):
        self.log_records = []
        self.log = logging.getLogger()
        self.artifacts = {}

    def debug(self, msg):
        self.log.debug(msg)

    def warn(self, msg):
        self.log.warning(msg)

    def error(self, msg):
        self.log.error(msg)

    def fatal(self, msg):
        self.log.critical(msg)

    def add_artifact(self, key, value):
        # In Python 3.4, pathlib.Path exists, but let's be careful about f-strings
        from pathlib import Path
        if isinstance(value, (str, Path)):
            path_val = Path(value)
            if path_val.is_file():
                self.debug("Artifact file '{}' exists.".format(value))
            else:
                self.warn("Artifact file '{}' does NOT exist.".format(value))
            self.artifacts[key] = {'type': 'filename', 'value': value}
        else:
            self.artifacts[key] = {'type': 'primitive', 'value': value}


class GlobalContextLogHandler(logging.Handler):
    """
    A handler that captures all logs into a single test's context log_records,
    so we can show them in a final summary or store them.
    """
    def __init__(self, ctx, formatter=None):
        logging.Handler.__init__(self)
        self.ctx = ctx
        if formatter:
            self.setFormatter(formatter)

    def emit(self, record):
        msg = self.format(record)
        self.ctx.log_records.append((record.levelname, msg))


class SimpleLogFormatter(logging.Formatter):
    """
    Format logs with a timestamp and color-coded level, e.g.:
    HH:MM:SS LEVEL|LOGGER| message
    """
    def format(self, record):
        tstamp = datetime.now().strftime("%H:%M:%S")
        level = record.levelname
        origin = record.name
        message = record.getMessage()

        if level in ("ERROR", "CRITICAL"):
            color = Fore.RED
        elif level == "WARNING":
            color = Fore.YELLOW
        elif level == "DEBUG":
            color = Fore.MAGENTA
        elif level == "INFO":
            color = Fore.CYAN
        else:
            color = ""

        return "{}{} {:8s}|{:11s}| {}{}".format(
            color, tstamp, level, origin, message, Style.RESET_ALL
        )


def load_test_module_by_path(file_path):
    """
    Dynamically import a Python file as a module, so we can discover test_* functions.
    """
    spec = importlib.util.spec_from_file_location("micropytest_dynamic", file_path)
    module = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(module)
    return module


def find_test_files(start_dir="."):
    """
    Recursively find all *.py that match test_*.py or *_test.py,
    excluding files in typical virtual environment or site-packages folders,
    using os.walk for Python 3.4 compatibility (rglob is 3.5+).
    """
    test_files = []
    for root, dirs, files in os.walk(start_dir):
        # Exclude certain directories
        if (".venv" in root) or ("venv" in root) or ("site-packages" in root) or ('__pycache__' in root):
            # Skip processing this folder
            continue

        for f in files:
            if f.startswith("test_") or f.endswith("_test.py"):
                test_files.append(os.path.join(root, f))
    return test_files


def load_lastrun(tests_root):
    """
    Load .micropytest.json from the given tests root (tests_root/.micropytest.json) if present.
    Returns a dict with test durations, etc.
    """
    p = Path(tests_root) / CONFIG_FILE
    if p.exists():
        try:
            with p.open("r", encoding="utf-8") as f:
                return json.load(f)
        except Exception:
            pass
    return {}


def store_lastrun(tests_root, test_durations):
    """
    Write out test durations to tests_root/.micropytest.json.
    """
    data = {
        "_comment": "This file is optional: it stores data about the last run of tests for time estimates.",
        "micropytest_version": __version__,
        "test_durations": test_durations
    }
    p = Path(tests_root) / CONFIG_FILE
    try:
        with p.open("w", encoding="utf-8") as f:
            json.dump(data, f, indent=2)
    except Exception:
        pass


def run_tests(tests_path, show_estimates):
    """
    The core function that:
      1) Discovers test_*.py
      2) For each test function test_*,
         - optionally injects a TestContext
         - times the test
         - logs pass/fail
      3) Updates .micropytest.json with durations
      4) Returns a list of test results

    Note: Logging configuration (verbosity, quiet, etc.) can be done by the caller.
    """
    root_logger = logging.getLogger()
    root_logger.setLevel(logging.DEBUG)  # or caller sets this

    formatter = SimpleLogFormatter()

    # Load known durations
    lastrun_data = load_lastrun(tests_path)
    test_durations = lastrun_data.get("test_durations", {})

    # Discover test callables
    test_files = find_test_files(tests_path)
    test_funcs = []
    for f in test_files:
        try:
            mod = load_test_module_by_path(f)
        except Exception:
            root_logger.error(
                "Error importing {}:\n{}".format(f, traceback.format_exc())
            )
            continue

        for attr in dir(mod):
            if attr.startswith("test_"):
                fn = getattr(mod, attr)
                if callable(fn):
                    test_funcs.append((f, attr, fn))

    total_tests = len(test_funcs)
    test_results = []
    passed_count = 0

    # Possibly show total estimate
    if show_estimates and total_tests > 0:
        sum_known = 0.0
        for (fpath, tname, _) in test_funcs:
            key = "{}::{}".format(fpath, tname)
            sum_known += test_durations.get(key, 0.0)
        if sum_known > 0:
            root_logger.info(
                "{}Estimated total time: ~{:.1f}s for {} tests{}".format(
                    Fore.CYAN, sum_known, total_tests, Style.RESET_ALL
                )
            )

    # Run each test
    for idx, (file_path, test_name, test_func) in enumerate(test_funcs, start=1):
        ctx = TestContext()

        # attach a log handler for this test
        test_handler = GlobalContextLogHandler(ctx, formatter=formatter)
        root_logger.addHandler(test_handler)

        key = "{}::{}".format(file_path, test_name)
        known_dur = test_durations.get(key, 0.0)

        if show_estimates:
            root_logger.info(
                "{}STARTING: {} (est ~{:.1f}s){}".format(
                    Fore.CYAN, key, known_dur, Style.RESET_ALL
                )
            )

        sig = inspect.signature(test_func)
        expects_ctx = len(sig.parameters) > 0

        t0 = time.perf_counter()
        outcome = {
            "file": file_path,
            "test": test_name,
            "status": None,
            "logs": ctx.log_records,
            "artifacts": ctx.artifacts,
            "duration_s": 0.0,
        }

        try:
            if expects_ctx:
                test_func(ctx)
            else:
                test_func()

            duration = time.perf_counter() - t0
            outcome["duration_s"] = duration
            passed_count += 1
            outcome["status"] = "pass"
            root_logger.info(
                "{}FINISHED PASS: {} ({:.3f}s){}".format(
                    Fore.GREEN, key, duration, Style.RESET_ALL
                )
            )
        except Exception:
            duration = time.perf_counter() - t0
            outcome["duration_s"] = duration
            outcome["status"] = "fail"
            root_logger.error(
                "{}FINISHED FAIL: {} ({:.3f}s)\n{}{}".format(
                    Fore.RED, key, duration, traceback.format_exc(), Style.RESET_ALL
                )
            )
        finally:
            root_logger.removeHandler(test_handler)

        test_durations[key] = duration
        test_results.append(outcome)

    root_logger.info(
        "{}Tests completed: {}/{} passed.{}".format(
            Fore.CYAN, passed_count, total_tests, Style.RESET_ALL
        )
    )

    # Write updated durations
    store_lastrun(tests_path, test_durations)
    return test_results

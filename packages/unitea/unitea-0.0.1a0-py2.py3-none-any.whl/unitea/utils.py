import importlib
import os
import re
import time
import sys
import logging
import fcntl

FILE_MODIFICATION_WATCH_INTERVAL_SECONDS = 0.1


class GameArgumentError(Exception):
    pass


def monitor_file_for_external_modification(filename, get_internal_modification_time, callback):
    logging.debug(f"File modification started for {filename}")
    try:
        while True:
            time.sleep(FILE_MODIFICATION_WATCH_INTERVAL_SECONDS)
            with open(filename, "r") as file:
                fcntl.flock(file, fcntl.LOCK_EX)
                modification_time = os.stat(filename).st_mtime
                internal_modification_time = get_internal_modification_time()
                fcntl.flock(file, fcntl.LOCK_UN)

                if modification_time != internal_modification_time:
                    logging.debug(
                        f"Detected external file modification ({modification_time} != {internal_modification_time})"
                    )
                    callback()
    except KeyboardInterrupt:  # user pressed Ctrl+C
        pass


def import_optional_module(module_name):
    """
    Try to import a module.

    If all ok, return the imported module.
    In case of import error print an error message (including the 'pip install'
    command required to install the missing module) and exit with error.
    """
    if module_name in globals():
        module = globals()[module_name]
    else:
        module = importlib.import_module(module_name)
        globals()[module_name] = module

    return module


def get_text_after_prompt(text, prompt):
    return re.sub(f".*{re.escape(prompt)}", "", text, flags=re.DOTALL)

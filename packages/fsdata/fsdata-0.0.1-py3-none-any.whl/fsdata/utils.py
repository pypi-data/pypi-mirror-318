"""fsspec data mapper"""

import os
import re


def check_path(path):
    """check and normalize path"""
    if re.match(r"^([a-z]):", path):
        prefix = ""
    else:
        prefix, _, path = path.rpartition(":")

    if prefix == "":
        prefix = "local"

    if path.startswith("~"):
        path = os.path.expanduser(path)

    if not path.startswith(("/", "\\")):
        raise ValueError(f"Path {path!r} is not absolute!")
    
    return prefix + ":" + path


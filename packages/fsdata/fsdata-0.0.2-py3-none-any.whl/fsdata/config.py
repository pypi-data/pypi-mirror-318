"""fsspec data mapper"""

import os

from functools import lru_cache
from configparser import ConfigParser, Interpolation


class ExpandVars(Interpolation):
    """Interpolation to expand environment variables"""

    def before_get(self, parser, section, option, value, defaults):
        return os.path.expandvars(value)


def config_dirs():
    """list of config dirs from environment or defaults"""
    config_dirs = os.getenv("FSDATA_CONFIG_DIRS", None)
    if config_dirs:
        return config_dirs.split(os.pathsep)
    
    config_home = os.getenv("XDG_CONFIG_HOME", "~/.config")
    config_dirs = os.getenv("XDG_CONFIG_DIRS", "/etc/xdg").split(os.pathsep)

    config_dirs = [config_home, *config_dirs]
    config_dirs = [os.path.expanduser(p) for p in config_dirs if len(p)]

    return config_dirs


@lru_cache
def read_config():
    """read configuration files"""
    config = ConfigParser(interpolation=ExpandVars())

    for folder in config_dirs():
        file = os.path.join(folder, "fsdata.ini")      
        if os.path.exists(file):
            config.read(file)

    return config


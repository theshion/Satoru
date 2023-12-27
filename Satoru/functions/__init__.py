import glob
from os.path import basename, dirname, isfile


def __list_all_functions():
    mod_paths = glob.glob(dirname(__file__) + "/*.py")

    all_functions = [
        basename(f)[:-3]
        for f in mod_paths
        if isfile(f) and f.endswith(".py") and not f.endswith("__init__.py")
    ]

    return all_functions


ALL_FUNCTIONS = sorted(__list_all_functions())
__all__ = ALL_FUNCTIONS + ["ALL_FUNCTIONS"]

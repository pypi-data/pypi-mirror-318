import importlib

__all__ = ["getdatapath"]

PATHS = dict()


def calcdatapath(key):
    names = list(key)
    if len(names) == 0:
        return None
    resource = names.pop(-1)
    package = ".".join(names)
    context = importlib.resources.path(package, resource)
    path = context.__enter__()
    ans = str(path)
    return ans


def getdatapath(*names):
    key = tuple(str(x) for x in names)
    if key not in PATHS:
        PATHS[key] = calcdatapath(key)
    return PATHS[key]

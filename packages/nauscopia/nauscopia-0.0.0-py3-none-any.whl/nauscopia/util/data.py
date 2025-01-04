import typing as t


def asbool(obj: t.Any) -> bool:
    # from sqlalchemy.util.langhelpers
    # from paste.deploy.converters
    if isinstance(obj, str):
        obj = obj.strip().lower()
        if obj in ["true", "yes", "on", "y", "t", "1"]:
            return True
        elif obj in ["false", "no", "off", "n", "f", "0"]:
            return False
        else:
            raise ValueError("String is not true/false: %r" % obj)
    return bool(obj)

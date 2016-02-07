# slighty modifed from http://stackoverflow.com/a/4904200/4087357
# from user vrde http://stackoverflow.com/users/597097/vrde

import sys
try:
    from StringIO import StringIO
except ImportError:
    from io import StringIO


def exec_output(code):
    buffer = StringIO()
    sys.stdout = buffer

    try:
        exec(code, globals())
    except Exception as e:
        return "{0}\n{1}\n".format(e.__doc__, e)

    # remember to restore the original stdout!
    sys.stdout = sys.__stdout__

    return buffer.getvalue()

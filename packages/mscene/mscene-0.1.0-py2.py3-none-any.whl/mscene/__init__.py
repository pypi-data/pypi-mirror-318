#!/usr/bin/python3

from IPython import get_ipython

ipy = get_ipython()


def mscene_magic(line):

    line_magic = f"-m mscene {line}"

    ipy.run_line_magic("run", line_magic)


ipy.register_magic_function(mscene_magic, "line", "mscene")

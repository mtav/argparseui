#!/usr/bin/env python3
import argparse
import sys
from PyQt5 import QtWidgets
import argparseui

# EXPERIMENT USING BASIC PARSER     
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--make-argument-true", help="optional boolean argument", action="store_true")
parser.add_argument("-o","--make-other-argument-true", help="optional boolean argument 2", action="store_true",  default=True)
parser.add_argument("-n","--number", help="an optional number", type=int)
parser.add_argument("-r","--restricted-number", help="one of a few possible numbers", type=int, choices=[1,2,3],  default=2)
parser.add_argument("-c", "--counting-argument", help="counting #occurrences", action="count")
parser.add_argument("-d", "--default-value-argument", help="default value argument", type=float, default="3.14")
group = parser.add_mutually_exclusive_group()
group.add_argument("-v", "--verbose", action="store_true")
group.add_argument("-q", "--quiet", action="store_true")
parser.add_argument("posarg", help="positional argument", type=str)

app = QtWidgets.QApplication(sys.argv)
a = argparseui.ArgparseUi(parser)
a.show()
app.exec_()

if a.result() == 1: # Ok pressed
    parsed_args = a.parse_args() # ask argparse to parse the options
    print(parsed_args)            # print the parsed_options

# Do what you like with the arguments...

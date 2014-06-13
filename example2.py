#!/usr/bin/env python3
import argparse
import sys
from PyQt5 import QtWidgets
import argparseui

def do_something(argparseuiinstance):
    options = argparseuiinstance.parse_args()
    print ("Options: ", options)
     
parser = argparse.ArgumentParser()
parser.add_argument("-m", "--make-argument-true", help="optional boolean argument", action="store_true")
parser.add_argument("-o","--make-other-argument-true", help="optional boolean argument 2", action="store_true",  default=True)

app = QtWidgets.QApplication(sys.argv)
a =     argparseui.ArgparseUi(parser,use_save_load_button=True,ok_button_handler=do_something)
a.show()
app.exec_()
if a.result() != 1:
    # Do what you like with the arguments...
    print ("Cancel pressed")

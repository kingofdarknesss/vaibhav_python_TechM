#1. correcting circualr imports

#module_a.py:
import module_b

def func_a():
    return "Function A"

print(module_b.func_b())

# module_b.py:
# we reomove the circular import by removing the import of module a in module b
def func_b():
    return "Function B"

# the problem of circuar dependency is therefore resolved 

# dynamic module loading
import sys
module_name =sys.argv[1]
import importlib
math = importlib.import_module(module_name)
func_name=input("the function name :")
argu=input("enter the argunment: ")
argu_conv=int(argu)
func=getattr(math,func_name)
print (func)
print(func(argu_conv))

#importing and using the calulator module

import calculator
print(calculator.divide(2,3)) #0.6666666
print(calculator.divide(2,0)) # cannot divide by zero


#advanced import startegy
#created a simple module and then imported it in main.py where it runs as a script 
# checking if the function exists with getattr 

#import time for modules
import time
start = time.time()
import math
from sys import *
from os import *
end = time.time()
print(f"Import time: {end - start}") #Import time: 2.005006790161133

#package creation and usage
# I created a mypackage directory with a simple setup file and  basic mat operation
#then I used pip to install that package and used it in test_pack.py file


# mocking a module for testing
from unittest import mock
with mock.patch('math.sqrt', return_value=100):
    print(math.sqrt(25))  # Should print 100

import import_side_effects
msg=import_side_effects.greet("hello") 
print(msg)#This code runs as soon as the module is imported in the program
           #Hello, hello!

#module caching
import sys
import math
print(sys.modules['math'])#[?2004l
#<module 'math' (built-in)>
#[?2004h

import sys
import mypackage
print(sys.modules['mypackage']) #<module 'mypackage' from 'C:\\Python312\\Lib\\site-packages\\mypackage\\__init__.py'>
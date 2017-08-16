#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

x = 1
def local(x):
    print('x is:',x)
    x = 2
    print('x is:',x)
local(x)
print('x is:',x)
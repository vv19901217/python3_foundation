#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

x = 10


def global_x():
    global x  # 读取全局中的x的值
    print('x is:', x)
    x = 20
    print('changed global x to:', x)


print('函数运行之前,全局x的值为:', x)
global_x()
print('函数运行之后,全局x的值为:', x)

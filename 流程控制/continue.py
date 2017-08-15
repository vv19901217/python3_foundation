#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

while True:
    str = input('请输入字符:')
    if str == 'quit':
        print('已退出')
        break
    elif len(str) < 3:
        print('您输入的字符长度小于3!')
        continue
    else:
        print('您输入的是%s' % str)

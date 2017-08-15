#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
# 猜数游戏
number = 30
running = True
while running:
    guess = int(input('请输入您猜的数字：'))
    if (guess == number):
        running = False
        print('您才对了，结果就是%s' % guess)
    elif (guess < number):
        print('%s太小了，请重新猜测' % guess)
    elif (guess > number):
        print('%s太大了,请重新猜测' % guess)

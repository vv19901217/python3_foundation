#!/usr/bin/env python3
# _*_ coding:utf-8 _*_
height = float(input('请输入您的身高(cm):'))/100
weight = float(input('请输入您的体重(kg):'))
def BMI_sf():
    BMI = weight / (height ** 2)
    str = ''
    if BMI<18.5:
        str = '过轻'
    elif BMI<25:
        str = '正常'
    elif BMI <28:
        str = '过重'
    elif BMI <32 :
        str = '肥胖'
    else:
        str = '严重肥胖'
    return [BMI,str]
print('身高是:%scm,体重是:%slg,指数是:%.2f,您属于%s' %(height*100,weight,BMI_sf()[0],BMI_sf()[1]))

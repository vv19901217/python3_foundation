#!/usr/bin/env python3
# _*_ coding:utf-8 _*_

L = [1,2,3,True]

# 获取列表中的元素
print( L[0] )
print( L[len(L)-1] )
print( L[-1] )

# 在尾部追加元素
L.append(2)

# 添加元素
L.insert(1,'str')   #在下标1的位置插入

# 删除元素
L.pop(1)    # 参数i是可选的,无参数即删除最后一个元素



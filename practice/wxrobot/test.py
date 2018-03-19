# -*- coding: utf-8 -*-


num = input('Input the num:')
a = int(num)

def fun(a):
    if a == 1:
        return 'one'

    print('run...here...')
    if a == 2:
        return 'two'
    else:
        return 'three'

print(fun(a))

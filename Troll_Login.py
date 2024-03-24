# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 16:24:50 2024

@author: LAM Quincy
"""

print('   name   : IllIllIl ',
      '\n password : wasdert')
t=1
while True:
    a=input('User name : ')
    b=input(' Password : ')
    if t<=2:
        print('\n- user name incorrect or password incorrect -\n')
    elif t>2:
        if a=='IllIllIl'and b== 'wasdert':
            print('\n- Correct -')
            break
        else:
            print('\n- Please input correctly -\n')
    t=t+1
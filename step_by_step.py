# -*- coding: utf-8 -*-
"""
Created on Fri Mar 22 15:57:22 2024

@author: LAM Quincy
"""

import random
import time
max=9
min=1
table=['_1_________',
       '__1________',
       '___1_______',
       '____1______',
       '_____1_____',
       '______1____',
       '_______1___',
       '________1__',
       '_________1_']
t=1
while True:
    print('-',t,'time -\n')
    if t>=10:
        print('You Stupid\n')
    elif t>=5:
        print('Quick! Trash\n')
    x=input('Roll? ')
    if x=='x':
        print('\n\n- You Trash -\n')
        break
    else:
        i=0
        a=random.randint(min, max)
        print('\n',a,'steps')
        while i<a:
            print('\r',table[i],end='')
            i=i+1
            time.sleep(0.5)
        if a==9:
            print('\n\n- You win! -')
            break
        else:
            print('\n\n- You Trash -\n')
        t=t+1
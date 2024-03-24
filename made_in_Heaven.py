# -*- coding: utf-8 -*-
"""
Created on Thu Mar  7 22:46:38 2024

@author: LAM Quincy
"""
import time
import os
a=['_*_________','__*________','___*_______','____*______','_____*_____','______*____','_______*___','________*__','_________*_']
while True:
    print('=======================','\n Type x to exit','\n Type p to play')
    print('=======================')
    x=input('input: ')
    print('-----------------------')
    if x == 'x':
        print('Exit','\nThanks for using')
        print('=======================')
        time.sleep(2)
        os.system("cls")
        break
    if x == 'p':
        t=int(10)
        delay=1
        print("\r    你 相信引力嗎    ",end="")
        time.sleep(2)
        print("\r     時間加速吧      ",end="")
        time.sleep(2)
        print("\r  Made in Heaven   ",end="")
        print('\n-----------------------')
        for i in range(t):
            for char in a:
                print(f'\r{char}        ',end='')
                time.sleep(delay)
                delay *= 0.96
        print('\r___________')
        time.sleep(1)
        print('\n我以神的諭令令你退下！')
        time.sleep(2)
        print('    覺悟者恆幸福    ')
        print('\n=======================')
        time.sleep(3)
        os.system("cls")
        break
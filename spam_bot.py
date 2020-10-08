# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 22:47:21 2020

@author: aryar
"""

import pyautogui, time
time.sleep(5)
f = open("https://github.com/aryaraj132/Spam-Bot/blob/master/bee_script.txt",'r')

for word in f:
    pyautogui.typewrite(word)
    pyautogui.press("enter")
    

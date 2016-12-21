# -*- coding: utf-8 -*-
"""
Created on Sun Dec 18 03:34:27 2016

@author: footb
"""

import win32api,win32con,win32clipboard
import time
import Tkinter as tk

def get_cords():
    for i in range(20):
        x,y = win32api.GetCursorPos()
        print x,y
        time.sleep(0.5)

def leftClick():
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click."  

def mousePos(cord):
    win32api.SetCursorPos(cord)

fo = open("donkdata.txt", "a")

for i in range(177):
    mousePos((1060, 1415))
    leftClick()
    time.sleep(0.1)
    mousePos((1070, 1168))
    leftClick()
    #ctrl-a
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(0x41, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(win32con.VK_CONTROL, 0,win32con.KEYEVENTF_KEYUP, 0)
    
    #ctrl-c
    win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(0x43, 0, 0, 0)
    time.sleep(0.1)
    win32api.keybd_event(0x43, 0, win32con.KEYEVENTF_KEYUP, 0)
    time.sleep(0.1)
    win32api.keybd_event(win32con.VK_CONTROL, 0,win32con.KEYEVENTF_KEYUP, 0)
    
    time.sleep(0.1)
    root = tk.Tk()
    # keep the window from showing
    root.withdraw()
    
    # read the clipboard
    c = root.clipboard_get()
    fo.write(c)
    fo.write("\n")
    print c

fo.close()
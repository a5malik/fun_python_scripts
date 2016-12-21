# -*- coding: utf-8 -*-
"""
Created on Tue Dec 20 16:07:30 2016

@author: footb

easy command line actions for Bluff Avenue client.
"""

import win32api,time,win32con
import win32gui

def callback(hwnd, extra):
    print "%s" % win32gui.GetWindowText(hwnd)
    


def typethis(sentence=None,shift=False,control=False,delay=0.05,random_delay=0.05):
    for letter in sentence:
        c=letter
        punctflag = True
        if (letter>='A' and letter<='Z') or shift:
            win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
            punctflag = False
        if letter>='a' and letter<='z':
            c=letter.upper()
            punctflag = False
        if ((letter>='0' and letter<='9') or (letter==' ')):
            punctflag=False
        if control:
            win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)

        if not punctflag: # Do this for real letters on the keyboard
            if isinstance(letter,(int)):
                ordletter=letter
            else:
                ordletter=ord(c)

            win32api.keybd_event(ordletter, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0) 
            time.sleep(delay)
            win32api.keybd_event(ordletter, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                        win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(delay)

            if control:
                win32api.keybd_event(win32con.VK_CONTROL, 0, win32con.KEYEVENTF_KEYUP, 0)
            if (letter>='A' and letter<='Z') or shift:
                win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
        # This must be some punctuation - try to deal with it. 
        # win32con doesn't include OEM
        else: 
            if letter=='.':
                win32api.keybd_event(190, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                time.sleep(delay)
                win32api.keybd_event(190, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)
            elif letter==',':
                win32api.keybd_event(188, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                time.sleep(delay)
                win32api.keybd_event(188, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)
            elif letter=='-':
                win32api.keybd_event(189, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                time.sleep(delay)
                win32api.keybd_event(189, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)
            elif letter=='?':
                win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                time.sleep(delay)
                win32api.keybd_event(191, 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                time.sleep(delay)
                win32api.keybd_event(191, 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)
                win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)
            elif letter=='!':
                win32api.keybd_event(win32con.VK_SHIFT, 0, 0, 0)
                time.sleep(delay)
                win32api.keybd_event(ord('1'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 0, 0)
                time.sleep(delay)
                win32api.keybd_event(ord('1'), 0, win32con.KEYEVENTF_EXTENDEDKEY | 
                win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)
                win32api.keybd_event(win32con.VK_SHIFT, 0, win32con.KEYEVENTF_KEYUP, 0)
                time.sleep(delay)

                
                
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

def click(cord):
    win32api.SetCursorPos(cord)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTDOWN,0,0)
    time.sleep(.1)
    win32api.mouse_event(win32con.MOUSEEVENTF_LEFTUP,0,0)
    print "Click." 
    

def main():
    win32gui.EnumWindows(callback, None)
    time.sleep(2)
    wname = raw_input('Copy/Paste exact window name from above list here: (it will be of the form (table name)- Bluff Avenue - Google Chrome:')
    s = ""
    while(True):
        hwnd = win32gui.FindWindow(None, wname)
        win32gui.BringWindowToTop(hwnd)
        #win32gui.SetForegroundWindow(hwnd)
        
        rect = win32gui.GetWindowRect(hwnd)
        x = rect[0]
        y = rect[1]
        w = rect[2] - x
        h = rect[3] - y
        
        start_y_ratio = 619.0/785.0
        height_box_ratio = 21.0/785.0
        start_x_ratio = 347.0/737.0
        x_box = int(x+start_x_ratio*w+6)
        y_fold = y+(start_y_ratio+height_box_ratio/2)*h
        y_check = int(y_fold+height_box_ratio*h)
        y_raise = int(y_fold+2*height_box_ratio*h)
        y_amount = int(y_fold+3*height_box_ratio*h+10)
        y_fold=int(y_fold)
        time.sleep(0.4)
        s = raw_input('Enter action(F/C/R amt/Quit)): ')
        su = s[0].upper()
        if su == 'F':
            click((x_box, y_fold))
        elif su == 'C':
            click((x_box, y_check))
        elif su == 'R':
            amt = s[2:]
            #bet/raise
            click((x_box, y_amount))
            
            #ctrl-a
            win32api.keybd_event(win32con.VK_CONTROL, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(0x41, 0, 0, 0)
            time.sleep(0.1)
            win32api.keybd_event(0x41, 0, win32con.KEYEVENTF_KEYUP, 0)
            time.sleep(0.1)
            win32api.keybd_event(win32con.VK_CONTROL, 0,win32con.KEYEVENTF_KEYUP, 0)
            
            win32api.keybd_event(win32con.VK_BACK, 0, 0, 0)
            time.sleep(0.8)
            win32api.keybd_event(win32con.VK_BACK, 0, win32con.KEYEVENTF_KEYUP, 0)
            
            typethis(amt)
            time.sleep(0.2)
            click((x_box, y_raise))
        elif su == 'Q':
            break
        else:
            continue
       
        

if __name__ == '__main__':
    main()

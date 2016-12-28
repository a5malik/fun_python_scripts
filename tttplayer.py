# -*- coding: utf-8 -*-
"""
Created on Mon Dec 26 16:03:45 2016

@author: footb

Uses minimax with a/b pruning to play Tic Tac Toe on https://playtictactoe.org/
Uses snapshots to recognize x's and o's
"""



import win32api,time,win32con
import win32gui
#import pyscreenshot as ImageGrab
from PIL import ImageGrab
from PIL import ImageOps
import time
from numpy import *
import os
import random
from selenium import webdriver

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

def screenGrabW():
    time.sleep(4)
    im = ImageGrab.grab()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
    
def screenGrab(box):
    im = ImageGrab.grab(box)
    #im.show()
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')


class Shapes:
    empty, cross, circle = range(3)

class Player:
    me, ai = range(2)

shapes = [Shapes.cross, Shapes.circle]
class Board:    
    def __init__(self, state):
        self.state = state
    
    def next_states(self, shape):
        l = []
        for i in range(9):
            if self.state[i] == Shapes.empty:
                r = list(self.state)
                r[i] = shape
                l.append((Board(r), i))
        return l
    def process(self, a, b, c, shape):
        if self.state[a] == shape and self.state[b] == shape and self.state[c] == shape :
            return True
        else:
            return False
        
    def evaluate(self, player_shape, ai_shape):
        for i in range(3):
            if self.process(3*i, 3*i+1, 3*i+2, player_shape):
                return 1
            if self.process(i, i+3, i+6, player_shape):
                return 1
            if self.process(3*i, 3*i+1, 3*i+2, ai_shape):
                return -1
            if self.process(i, i+3, i+6, ai_shape):
                return -1
        
        if self.process(0, 4, 8, player_shape):
            return 1
        if self.process(2, 4, 6, player_shape):
            return 1
        
        if self.process(0, 4, 8, ai_shape):
            return -1
        if self.process(2, 4, 6, ai_shape):
            return -1
        
        return 0
        
            
    def over(self):
        if Shapes.empty in self.state:
            return False
        else:
            return True
            
    def pnt(self):
        print "board:"
        print self.state[:3]
        print self.state[3:6]
        print self.state[6:9]
        


def minimax(board, player, maxDepth, currentDepth, alpha, beta):
    if board.over() or currentDepth == maxDepth:
        r = board.evaluate(shapes[Player.me], shapes[Player.ai])
        return r, None, currentDepth
    
    res = board.evaluate(shapes[Player.me], shapes[Player.ai])
    
    if res == -1 or res == 1:
        return res, None, currentDepth
    
    bestMove = None
    if player == Player.me: bestScore = -1
    else: bestScore = 1
    bestDepth = 10
    for board_i,i in board.next_states(shapes[player]):
        cur_score, cur_move, cur_depth = minimax(board_i, (player+1)%2, maxDepth, currentDepth+1, alpha, beta)
        alpha = max(cur_score, alpha)
        beta = min(cur_score, beta)
        if player == Player.me:
            if cur_score > bestScore:
                bestScore = cur_score
                bestMove = i
                bestDepth = cur_depth
                #if cur_score >= beta:
                #   return bestScore, bestMove, bestDepth
            elif cur_score == bestScore and bestMove is not None and cur_depth<bestDepth:
                bestMove = i
                bestDepth = cur_depth
        else:
            if cur_score < bestScore:
                bestScore = cur_score
                bestMove = i
                #if cur_score <= alpha:
                #    return bestScore,bestMove, bestDepth
            elif cur_score == bestScore and bestMove is not None and cur_depth<bestDepth:
                bestMove = i
                bestDepth = cur_depth
                
    #print str(player) + " selecting " + str(bestMove) + " with score " + str(bestScore)
    return bestScore,bestMove, bestDepth

#remember to change this...    
browser = webdriver.Chrome("C:\\Users\\footb\\Downloads\\chromedriver_win32\\chromedriver.exe")
browser.get("https://playtictactoe.org/")
time.sleep(1)
toplist, winlist = [], []
def enum_cb(hwnd, results):
    winlist.append((hwnd, win32gui.GetWindowText(hwnd)))
win32gui.EnumWindows(enum_cb, toplist)

ttt_windows = [(hwnd, title) for hwnd, title in winlist if 'toe' in title.lower()]
# just grab the hwnd for first window matching firefox
hwnd = ttt_windows[0][0]

win32gui.BringWindowToTop(hwnd)

bbox = win32gui.GetWindowRect(hwnd)

#gets the TL and BR coordinates of the center box

x1 = 0
y1 = 0

print "Hurry! Settle cursor on Top Left coordinate of center box"
for i in range(15):
    x1,y1 = win32api.GetCursorPos()
    print x1,y1
    time.sleep(0.5)
    
print "Top Left coordinates are: ", x1, y1
c = raw_input("Enter c to continue: ")
x2 = 0
y2 = 0


    
print "Hurry! Settle cursor on Bottom Right coordinate of center box"
for i in range(15):
    x2,y2 = win32api.GetCursorPos()
    print x2,y2
    time.sleep(0.5)

print "Botom Right coordinates are: ", x2, y2
print "Now, you can make whatever moves(if you want)"
print "It will start from wherever you leave it (even scratch)"
c = raw_input("Press c when you are ready, and sit back! (dont use the mouse!)")
print "Now, it will play for you : )"

#x1 = 434
#y1 = 769
#x2 = 637
#y2 = 967
img = ImageOps.grayscale(ImageGrab.grab((x1,y1,x2,y2)))
print img.getcolors()
#img.show()

CELLW = abs(x2-x1)
CELLH = abs(y2-y1)
STARTX = x1-CELLW
STARTY = y1-CELLH


sums= []

for y in range(3):
    for x in range(3):
        box = (STARTX+CELLW*x+10, STARTY+CELLH*y+10, STARTX+CELLW*x+CELLW-10, STARTY+CELLH*y+CELLH-10)
        im = ImageOps.grayscale(ImageGrab.grab(box))
        a = array(im.getcolors())
        a = a.sum()
        sums.append(a/1000)
        #screenGrab(box)
        time.sleep(0.5)

print sums
shapenum = list(set(sums))
shapenum.sort()
state = [shapenum.index(i) for i in sums]
my = [0,0,0,1,1,1,2,2,2]
mx = [0,1,2,0,1,2,0,1,2]
bp = ["draw", "win", "loss"]

#state = [Shapes.empty]*9
board = Board(state)
board.pnt()
player = Player.me

while(True):
    bestScore, bestMove, bestDepth = minimax(board, player, 10, 0, -1, 1)
    if bestMove == None:
        bestScore, bestMove, bestDepth = minimax(board, player, 2, 0, -1, 1)
    if bestMove == None:
        bestScore, bestMove, bestDepth = minimax(board, player, 1, 0, -1, 1)
    if bestMove == None:
        break
    #Click at best move
    print "Will click at spot ", bestMove
    print "Best Option is: (assuming optimal play) " + bp[bestScore]
    click((STARTX+CELLW*mx[bestMove]+CELLW/2, STARTY+CELLH*my[bestMove]+CELLH/2))
    mousePos((0,0))
    #Get Current State
    sums= []
    time.sleep(1)
    for y in range(3):
        for x in range(3):
            box = (STARTX+CELLW*x+10, STARTY+CELLH*y+10, STARTX+CELLW*x+CELLW-10, STARTY+CELLH*y+CELLH-10)
            im = ImageOps.grayscale(ImageGrab.grab(box))
            a = array(im.getcolors())
            a = a.sum()
            sums.append(a/1000)
            #screenGrab(box)
            time.sleep(0.5)
    print sums
    shapenum = list(set(sums))
    if len(shapenum) == 2: 
        break
    shapenum.sort()
    state = [shapenum.index(i) for i in sums]
    board = Board(state)
    board.pnt()

#pip install keyboard
import keyboard
import pyHook
import datetime ,time ,os
from PIL import ImageGrab
import cv2
import pythoncom
import numpy as np

coordinate = [1,1,1,1]
path = "G:/python_job/screenshot/"
firstpress=1

def on_mouse_event(event):
	if event.MessageName == "mouse left down":
		coordinate[0:2] = event.Position
	elif event.MessageName == "mouse left up":
		coordinate[2:4] == event.Position
		win32api.PostQuitMessage()#退出监听循环
		pic = ImageGrab.grab(coordinate)
		timestamp = datetime.datetime.now().strftime('%Y-%m-%d-%H-%M-%S') # 现在的时间
		pic.save(path+str(timestamp)+".png")
	

def cut():
    global img
    screen_cut()
    img = cv2.imread('screen.jpg')
    cv2.namedWindow('image')
    cv2.setMouseCallback('image', on_mouse)
    cv2.imshow('image', img)
    cv2.waitKey(0)
    os.remove('screen.jpg')
def screen_cut():
    beg = time.time()
    debug = False
    # img = ImageGrab.grab(bbox=(250, 161, 1141, 610))
    image = ImageGrab.grab()
    image.save("screen.jpg")
    # PIL image to OpenCV image
def on_mouse(event, x, y, flags, param):
    global img, point1, point2
    img2 = img.copy()
    if event == cv2.EVENT_LBUTTONDOWN:         #左键点击
        point1 = (x,y)
        cv2.circle(img2, point1, 10, (0,255,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_MOUSEMOVE and (flags & cv2.EVENT_FLAG_LBUTTON):               #按住左键拖曳
        cv2.rectangle(img2, point1, (x,y), (255,0,0), 5)
        cv2.imshow('image', img2)
    elif event == cv2.EVENT_LBUTTONUP:         #左键释放
        print("release button")
        point2 = (x,y)
        cv2.rectangle(img2, point1, point2, (0,0,255), 5) 
        cv2.imshow('image', img2)
        min_x = min(point1[0],point2[0])     
        min_y = min(point1[1],point2[1])
        width = abs(point1[0] - point2[0])
        height = abs(point1[1] -point2[1])
        cut_img = img[min_y:min_y+height, min_x:min_x+width]
        timestamp = datetime.datetime.now().strftime('%Y%m%d-%H%M%S')
        cv2.imwrite(path + str(timestamp) + "_capture.png", cut_img)




keyboard.add_hotkey('F8',cut) #add pageup hotkey
keyboard.wait('F9')


#=================================================
#字母和数字键     数字小键盘的键       功能键         其它键 
#      键   键码      键   键码          键   键码       键      键码 
#     A   65          0   96            F1   112       Backspace    8 
#     B   66          1   97            F2   113       Tab       9 
#     C   67          2   98            F3   114       Clear      12 
#    D   68          3   99            F4   115       Enter      13 
#    E   69          4   100           F5   116      Shift      16 
#    F   70          5   101           F6   117      Control     17 
#    G   71         6   102           F7   118      Alt       18 
#    H   72         7   103           F8   119      Caps Lock    20 
#    I    73          8   104          F9   120      Esc       27 
#   J    74          9   105          F10  121     Spacebar    32 
#   K   75         *   106           F11  122      Page Up     33 
#   L   76         +   107           F12  123      Page Down    34 
#   M   77        Enter 108                          End       35 
#   N   78         -   109                              Home      36 
#    O   79         .   110                              Left Arrow   37 
#    P   80         /   111                              Up Arrow    38 
#    Q   81                                                Right Arrow   39 
#    R   82                                                Down Arrow    40 
#    S   83                                                Insert      45 
#    T   84                                                Delete      46 
#    U   85                                                Help       47 
#   V   86                                                Num Lock     144   
#   W  87          
#    X   88      
#    Y   89      
#     Z   90      
#     0   48      
#     1   49      
#     2   50       
#     3   51       
#     4   52       
#     5   53       
#     6   54       
#     7   55       
#     8   56       
#     9   57









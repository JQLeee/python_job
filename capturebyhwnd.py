import time
import win32gui, win32ui, win32con, win32api
import win32clipboard, cv2
import pyautogui
from PIL import Image
from PIL import ImageGrab
from ctypes import *
import ctypes

hwnd_title = {}
def get_all_hwnd(hwnd,mouse):
    if(win32gui.IsWindow(hwnd)) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
#sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf8')
def gethwndbyName(name):
	win32gui.EnumWindows(get_all_hwnd, 0)
	hwnd = 0
	#f=open("G:/python_job/LOG.txt","w",encoding="utf-8")
	for h,t in hwnd_title.items():
		if t:
			print(h,":   ",t)
			#f.write(str(h)+":   "+t+"\n")
			if t == name:
				hwnd=h
	#f.close()
	return hwnd
			    
#把窗口调到前台再进行截图，否则可能会黑屏
#win32gui.SetForegroundWindow(hwnd)
#win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)
#time.sleep(1)
def window_capture(filename,hwnd): #优点是速度快，缺点是有些wpf框架开发的程序会显示黑屏
    #hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    #hwnd = win32gui.FindWindow(0,"Odin3 v3.14")
    #hwnd = win32gui.GetForegroundWindow()
    #获取句柄窗口的大小信息
    left,top,right,bot = win32gui.GetWindowRect(hwnd)
    w = right-left
    h = bot-top
    # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
    hwndDC = win32gui.GetWindowDC(hwnd)
    # 根据窗口的DC获取mfcDC
    mfcDC = win32ui.CreateDCFromHandle(hwndDC)
    # mfcDC创建可兼容的DC
    saveDC = mfcDC.CreateCompatibleDC()
    # 创建bigmap准备保存图片
    saveBitMap = win32ui.CreateBitmap()
    # print w,h　　　#图片大小
    # 为bitmap开辟空间
    saveBitMap.CreateCompatibleBitmap(mfcDC, w, h)
    # 高度saveDC，将截图保存到saveBitmap中
    saveDC.SelectObject(saveBitMap)
    # 截取从左上角（0，0）长宽为（w，h）的图片
    saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY)
	#方法一
    saveBitMap.SaveBitmapFile(saveDC, filename)

def pil_capture(filename,hwnd):#缺点是速度慢，但是保证是屏幕截图，所有窗口都可以截图，只要你能调到前面来
	#win32gui.ShowWindow(hwnd,win32con.SW_SHOW)#不能最小化窗口，否则会失效
	win32gui.SetForegroundWindow(hwnd)
	win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_RESTORE, 0)#SC_MAXIMIZE 最大化
	#win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE, 0)
	time.sleep(0.3)
	left,top,right,bot = win32gui.GetWindowRect(hwnd)
	d = 8
	coordinate = (left+d,top+d,right-d,bot-d)
	pic = ImageGrab.grab(coordinate)
	pic.save(filename)

def pil_capture_by_coordinate(filename,hwnd,x,y,w):
	coordinate = (x,y,x+w,y+w)
	pic = ImageGrab.grab(coordinate)
	pic.save(filename)
	
def showImage(path,win_title):
	cv2.namedWindow(win_title)
	imagex = cv2.imread(path)
	cv2.imshow(win_title,imagex)
	cv2.waitKey(0)
	cv2.destroyAllWindows

def debug():
	savefilename = "G:/python_job/background.png"
	hwnd = gethwndbyName("微信")
	pil_capture(savefilename,hwnd)
	showImage(savefilename,"capturePic")

if __name__ == "__main__":
	debug()

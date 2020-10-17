import cv2 ,win32gui ,pyautogui ,win32api ,win32con ,time
import capturebyhwnd 
from pymouse import PyMouse

path="G:/python_job/screenshot/"
d=8

global gx,gy

def find_pic_in_template(target,hwnd):
	global gx ,gy
	capturebyhwnd.pil_capture(path+"template.png",hwnd)
	temp=cv2.imread(path + "template.png")
	tar=cv2.imread(path + target + ".png")
	tar_h,tar_w = tar.shape[:2]  #返回目标图片的高和宽
	#执行模板匹配，采用匹配方式cv2.TM_SQDIFF_NORMED
	result = cv2.matchTemplate(tar,temp,cv2.TM_SQDIFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	#如果匹配度小于90%,就认为没有找到
	if min_val >0.1:
		return None
	
	print(str(min_val))
	#计算要点击的坐标
	gx=min_loc[0] + tar_w//3
	gy=min_loc[1] + tar_h//3
	
	return gx,gy
	
def mouse_click_abs(hwnd,x,y):
	left,top,right,bot = win32gui.GetWindowRect(hwnd)
	nx = x + left + d
	ny = y + top + d
	for i in range(2):
		#pyautogui.click(nx,ny)
		#pa_click(nx,ny)
		pymouse_click(nx,ny)
		#win32_click(hwnd,x,y) #不用作坐标变换
		print("click at " + str(nx) + "," + str(ny))

def pa_click(x,y):
	pyautogui.click(x,y)

def pymouse_click(x,y):
	m=PyMouse()
	m.click(x,y)

def win32_click(hwnd,x,y): #这个不用作坐标变换，因为已经绑定了hwnd,已经是相对坐标
	long_position = win32api.MAKELONG(x,y)
	win32api.SendMessage(hwnd, win32con.WM_LBUTTONDOWN, win32con.MK_LBUTTON, long_position)#模拟鼠标按下
	time.sleep(0.03)
	win32api.SendMessage(hwnd, win32con.WM_LBUTTONUP, win32con.MK_LBUTTON, long_position)#模拟鼠标弹起
	
def click(hwnd):
	mouse_click_abs(hwnd,gx,gy)
	
def debug():
	windowname = "雷电模拟器（天命）"
	hwnd = capturebyhwnd.gethwndbyName(windowname)
	click_in_template("feitian",hwnd)
	
if __name__ == "__main__":
	debug()	
	
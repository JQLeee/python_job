import cv2 ,win32gui ,pyautogui
import capturebyhwnd 

path="G:/python_job/screenshot/"
d=8

def find_pic_in_template(target, template):
	temp=cv2.imread(path + template +".png")
	tar=cv2.imread(path + target + ".png")
	tar_h,tar_w = tar.shape[:2]  #返回目标图片的高和宽
	#执行模板匹配，采用匹配方式cv2.TM_SQDIFF_NORMED
	result = cv2.matchTemplate(tar,temp,cv2.TM_SQDIFF_NORMED)
	min_val, max_val, min_loc, max_loc = cv2.minMaxLoc(result)
	#如果匹配度小于99%,就认为没有找到
	#if min_val >0.01:
		#return None
	
	print(str(min_val))
	#计算要点击的坐标
	x=min_loc[0] + tar_w//3
	y=min_loc[1] + tar_h//3
	return x,y
	
def mouse_click_abs(hwnd,x,y):
	left,top,right,bot = win32gui.GetWindowRect(hwnd)
	nx = x + left + d
	ny = y + top + d
	for i in range(10):
		pyautogui.click(nx,ny)
		print("click at " + str(nx) + "," + str(ny))
	
def debug():
	hwnd = capturebyhwnd.gethwndbyName("安静的奇女子")
	capturebyhwnd.pil_capture(path+"template.png",hwnd)
	#capturebyhwnd().pil_capture_by_coordinate(path+"target.png",400,400,20)
	x,y= find_pic_in_template("a","template")
	mouse_click_abs(hwnd,x,y)
	#x,y  = find_pic_in_template("b","template")
	#mouse_click_abs(hwnd,x,y)
	#x,y  = find_pic_in_template("c","template")
	#mouse_click_abs(hwnd,x,y)
	#x,y  = find_pic_in_template("d","template")
	#mouse_click_abs(hwnd,x,y)
	
if __name__ == "__main__":
	debug()	
	
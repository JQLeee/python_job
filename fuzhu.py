import findPic as fp
import capturebyhwnd ,time


dir = "G:/python_job/screenshot/"

cx=0
cy=0

def main():
	winname = "用WinIO模拟键盘, 游戏只认第一次. 且WinIO模拟不了USB鼠标.-CSDN论坛 - 115电脑版"
	hwnd = capturebyhwnd.gethwndbyName(winname)
	if isIconExist("fatie",hwnd):
		click_in(hwnd)

	
def isIconExist(icon_name,h):
	global cx ,cy
	pos = fp.find_pic_in_template(icon_name,h)
	if pos is None:
		cx=0
		cy=0
		print(icon_name + " not found")
		return None
	cx=pos[0]
	cy=pos[1]
	return pos

def click_in(h):
	fp.click(h,cx,cy)
	
	
if __name__ == "__main__":
	main()

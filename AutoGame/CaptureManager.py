import win32gui, win32ui, win32con, win32api #pip install pywin32
import time
import cv2 #pip install opencv-python
from PIL import ImageGrab #pip install pillow

class CaptureManager:
    def __init__(self, path):
        self.save_path = path
        print("CaptureManager to do")

    def win32_capture(self,hwnd,filename):#优点是速度快，甚至可以后台截屏，缺点是有些wpf框架开发的程序会显示黑屏
        # 获取句柄窗口的大小信息
        left,top,right,bot = win32gui.GetWindowRect(hwnd)
        w = right - left
        h = bot - top
        hwndDC = win32gui.GetWindowDC(hwnd) # 根据窗口句柄获取窗口的设备上下文DC（Divice Context）
        mfcDC = win32ui.CreateDCFromHandle(hwndDC) # 根据窗口的DC获取mfcDC
        saveDC = mfcDC.CreateCompatibleDC() # mfcDC创建可兼容的DC
        saveBitMap = win32ui.CreateBitmap() # 创建bigmap准备保存图片
        saveBitMap.CreateCompatibleBitmap(mfcDC, w, h) # 为bitmap开辟空间, w,h 的大小
        saveDC.SelectObject(saveBitMap)  # 高度saveDC，将截图保存到saveBitmap中
        saveDC.BitBlt((0, 0), (w, h), mfcDC, (0, 0), win32con.SRCCOPY) # 截取从左上角（0，0）长宽为（w，h）的图片
        saveBitMap.SaveBitmapFile(saveDC, self.save_path+filename)#保存截取到的图片

    def pil_capture(self,hwnd,filename):#缺点是速度比win32慢，且需要把窗口调到前面来，不能最小化，但因为是全屏截图，不会出现win32的黑屏问题
        win32gui.SetForegroundWindow(hwnd)
        win32gui.SendMessage(hwnd , win32con.WM_SYSCOMMAND, win32con.SC_RESTORE,0)#恢复窗口
        # win32gui.SendMessage(hwnd, win32con.WM_SYSCOMMAND, win32con.SC_MAXIMIZE, 0) # 最大化窗口，看需要注释选择
        time.sleep(0.3)
        left,top,right,bot = win32gui.GetWindowRect(hwnd)
        d = 8 #不知道为什么有时候截图的边变会有多的，根据实际情况加了个offset自己调整
        coordinate = (left + d, top + d, right - d, bot - d)
        pic = ImageGrab.grab(coordinate)
        pic.save(self.save_path+filename)

    def pil_capture_by_coordinate(self,filename,hwnd,x,y,w):
        coordinate = (x, y, x + w, y + w)
        pic = ImageGrab.grab(coordinate)
        pic.save(self.save_path+filename)

    def selenium_capture(self):
        print("not finish yet")

    def showImage(self,path , win_title):
        cv2.namedWindow(win_title)
        imgx = cv2.imread(path)
        cv2.imshow(win_title,imgx)
        cv2.waitKey(0)
        cv2.destroyAllWindows()






import time
import win32gui, win32ui, win32con, win32api
import win32clipboard, cv2
import pyautogui

savefilename = "G:/python_job/background.png"

hwnd_title = {}
hwnd = 0
def get_all_hwnd(hwnd,mouse):
    if(win32gui.IsWindow(hwnd)) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd):
        hwnd_title.update({hwnd: win32gui.GetWindowText(hwnd)})
        
win32gui.EnumWindows(get_all_hwnd, 0)
for h,t in hwnd_title.items():
    if t:
        print(h,"----",t)
        if t == '即时通讯':
            hwnd = h
print("target hwnd is " + str(hwnd))
def window_capture(filename,hwnd):
    #hwnd = 0  # 窗口的编号，0号表示当前活跃窗口
    #hwnd = win32gui.FindWindow(0,"Odin3 v3.14")
    #hwnd = win32gui.GetForegroundWindow()
    #获取句柄窗口的大小信息
    left,top,right,bot = win32gui.GetWindowRect(hwnd)
    w = right-left
    h = bot-top
    w = w+500
    h = h+500
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
    saveBitMap.SaveBitmapFile(saveDC, filename)

window_capture(savefilename,hwnd)
cv2.namedWindow("capturePic")
imagex = cv2.imread(savefilename)
cv2.imshow("capturePic",imagex)
cv2.waitKey(0)
cv2.destroyAllWindows()
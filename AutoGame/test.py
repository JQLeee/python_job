from HwndManager import *
from CaptureManager import *

testHwnd= HwndManager()
hwnd = testHwnd.get_hwnd_by_name("盛夏的烈阳")
cm = CaptureManager('G:/python_job/AutoGame/')
cm.win32_capture(hwnd,"msp_win32.png")
#cm.pil_capture(hwnd,"msp_pil.png")
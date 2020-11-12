from HwndManager import *
from CaptureManager import *

testHwnd= HwndManager()
hwnd = testHwnd.get_hwnd_by_name("MSP TG")
cm = CaptureManager('D:/1/python_test/AutoGame/')
cm.win32_capture(hwnd,"msp_win32.png")
cm.pil_capture(hwnd,"msp_pil.png")
#from win32gui import *
import os
import win32gui

class HwndManager:
    def __init__(self):
        self.hwnd_titles = {}
        self.log_save_path = 'log.txt'
    def add_hwnd_in_list(self,hwnd,mouse):
        if(win32gui.IsWindow(hwnd) and win32gui.IsWindowEnabled(hwnd) and win32gui.IsWindowVisible(hwnd)):
            self.hwnd_titles.update({hwnd: win32gui.GetWindowText(hwnd)})

    def find_all_hwnd(self):
        win32gui.EnumWindows(self.add_hwnd_in_list, 0)
        return self.hwnd_titles

    def get_hwnd_by_name(self,name):
        self.find_all_hwnd()
        hwnd = 0
        for h,t in self.hwnd_titles.items():
            if t:
                print(h, " : ", t)
                with open(self.log_save_path,'w',encoding='utf-8') as f:
                    f.write(str(h) + " : " + t )
                if t == name:
                    hwnd =h
        f.close()
        return hwnd

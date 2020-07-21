#!usr/bin/env python

import ctypes

class POINT(ctypes.Structure):
    _fields_ = [("x", ctypes.c_ulong), ("y", ctypes.c_ulong)]
# get mouse cursor location    
point = POINT()
ctypes.windll.user32.GetCursorPos(ctypes.pointer(point))
print(point.x, point.y)

# Right click down and up on mouse button to open options (see: right click)
# currently takes current mouse position
ctypes.windll.user32.SetCursorPos(point.x,point.y)
ctypes.windll.user32.mouse_event(14,0,0,0,0)
ctypes.windll.user32.mouse_event(16,0,0,0,0)

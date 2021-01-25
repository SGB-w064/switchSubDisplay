import ctypes
import subprocess as sp

user32 = ctypes.windll.user32

singleScreenSize = user32.GetSystemMetrics(0), user32.GetSystemMetrics(1)
allScreenSize = user32.GetSystemMetrics(78), user32.GetSystemMetrics(79)

if singleScreenSize == allScreenSize:
    cmd = ["powershell", "&", "DisplaySwitch.exe", "/extend"]
else:
    cmd = ["powershell", "&", "DisplaySwitch.exe", "/internal"]

sp.run(cmd)


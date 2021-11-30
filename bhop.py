from win32gui import GetWindowText, GetForegroundWindow
import time
import keyboard
import pymem

fj = (0x526B5A0)
lp = (0xDA746C)
f = (0x104)



pm = pymem.Pymem("csgo.exe")
client = pymem.process.module_from_name(pm.process_handle, "client_panorama.dll").lpBaseOfDll

while True:
    if not GetWindowText(GetForegroundWindow()) == "Counter-Strike: Global Offensive":
        continue

    if keyboard.is_pressed("space"):
        forceJump = client + fj
        player = pm.read_int(client + lp)
        if player:
            on_ground = pm.read_int(player + f)
            if on_ground and on_ground == 257:
                pm.write_int(forceJump, 5)
                time.sleep(0.08)
                pm.write_int(forceJump, 4)

    time.sleep(0.002)


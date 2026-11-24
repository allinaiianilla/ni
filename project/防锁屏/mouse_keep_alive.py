
"""
文件路径：mouse_keep_alive.py
功能：定时微动鼠标
"""

import time
import pyautogui

# 每隔 3 分钟执行一次
INTERVAL = 5

print("鼠标自动微动程序已启动，按 Ctrl+C 退出")

try:
    while True:
        x, y = pyautogui.position()

        # 移动 2 个像素，再恢复原位置
        pyautogui.moveTo(x + 2, y, duration=0.2)
        # pyautogui.moveTo(x, y, duration=0.2)

        print("鼠标已微动")
        time.sleep(INTERVAL)

except KeyboardInterrupt:
    print("程序已退出")

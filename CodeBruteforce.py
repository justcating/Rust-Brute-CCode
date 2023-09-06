import pyautogui as pag
import time as t

fileName = input("File Name > ")

print("Start in 5 seconds...")
t.sleep(5)

with open(fileName, "r") as file:
	for line in file:
		print(line)
		pag.click()
		pag.write(line, interval=.01)
		t.sleep(0.022)
		pag.press("enter")
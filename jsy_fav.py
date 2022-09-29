import pywinmacro as p
from selenium import webdriver
import time

driver=webdriver.Chrome(executable_path="c:/chromedriver.exe")
driver.get("http://122.37.216.171:12345/jsy_fav/index.html")
# # driver.get("https://google.com")

time.sleep(2)
p.key_press_once("enter")
time.sleep(1)
p.typing("jsy")
p.key_press_once("tab")
time.sleep(1)
p.typing("jsy1030")
time.sleep(1)
p.key_press_once("enter")
time.sleep(1)
p.key_on("window")
p.key_on("up_arrow")
p.key_off("window")
p.key_off("up_arrow")

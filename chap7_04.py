import pywinmacro as pw
import time
from selenium import webdriver

# driver=webdriver.Chrome(executable_path="chromedriver.exe")
# driver.get("https:google.com")
# print(pw.get_mouse_position())
for i in range(5):
  pw.click((1209,301))
  time.sleep(1)
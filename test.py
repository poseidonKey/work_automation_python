from selenium import webdriver
from selenium.webdriver.chrome.options import Options
import pywinmacro as pw
import time
import pyperclip as pc
options = Options()
# 옵션에 해상도를 입력합니다.
options.add_argument("--window-size=1600,900")
driver = webdriver.Chrome(executable_path="chromedriver.exe", options=options)
driver.get('https://www.google.com/search?q=구찌&tbm=nws')
pw.ctrl_a()
pw.ctrl_c()
txt=pc.paste()
print(txt)
time.sleep(10)
driver.quit()

import pywinmacro as pw
import time
from selenium import webdriver
from selenium.webdriver.common.by import By

driver=webdriver.Chrome(executable_path="chromedriver.exe")
driver.get('https://twitter.com/i/flow/login')
time.sleep(5)
# input_tags=driver.find_elements(By.TAG_NAME,'input')
# print(len(input_tags))
# id_field=input_tags[0]
# ps_field=input_tags[1]
# id_field.send_keys("test")
# ps_field.send_keys("test")

# el=driver.find_element(By.XPATH,'//*[@id="mount_0_0_w2"]/div/div/div/div[1]/div/div/div/div[1]/section/main/article/div/div/div/div[1]/div[1]/a/div[1]/div[2]')
# el.click()

ele=driver.find_element(By.NAME,"text")
ele.send_keys('test')
ele.screenshot(filename='test.png')
time.sleep(5)
driver.quit()
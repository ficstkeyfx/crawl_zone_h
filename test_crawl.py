from selenium import webdriver
from PIL import Image
# from Screenshot import Screenshot_clipping
# driver = webdriver.Chrome(executable_path = 'C://chromedriver.exe')
# url = "https://www.google.com/"
# driver.get(url)
# driver.save_screenshot('test.png')

driver = webdriver.Chrome(executable_path='C://chromedriver.exe')
driver.get('https://siputterbang.shop')
el = driver.find_element_by_tag_name('body')
print(el.text)
driver.close()
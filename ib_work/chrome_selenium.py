# from selenium import webdriver # 从selenium导入webdriver

# driver = webdriver.Chrome()  # Optional argument, if not specified will search path.
# driver.get('http://hd.chinatax.gov.cn/nszx/InitMajor.html') # 获取百度页面
# inputElement = driver.find_element_by_id('queryvalue') #获取输入框
# # searchButton = driver.find_element_by_id('su') #获取搜索按钮

# inputElement.send_keys("江海证券有限公司") #输入框输入"Python"
# # searchButton.click() #搜索


# links = driver.find_element_by_xpath("(//td[@class='sv_hei14boldwhite'])[1]")
# links.click()
# driver.get_screenshot_as_file("test.png")


import requests

# r = requests.get("http://neris.csrc.gov.cn/shixinchaxun/login/ycode.do?d=Tue%20Feb%2025%202020%2017:39:00%20GMT+0800%20(%E4%B8%AD%E5%9B%BD%E6%A0%87%E5%87%86%E6%97%B6%E9%97%B4)")
# with open('code.png', 'wb') as file:
#     for data in r.iter_content(128):
#         file.write(data)
# # print(r.text)
# print (r.status_code)

r = requests.get('http://eid.csrc.gov.cn/ipo/infoBlock.action?block=1')
print(r.text)
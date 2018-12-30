from selenium import webdriver
from selenium.webdriver.common.keys import Keys

driver=webdriver.Chrome(executable_path="/home/efat/Documents/DevOps/Selenium/chromedriver")
#driver=webdriver.Firefox(executable_path="/home/efat/Documents/DevOps/Selenium/geckodriver")

driver.get('https://eu-innovi-staging.agentvi.com')
driver.find_element_by_name("email").send_keys("admin@agentvi.com")
driver.find_element_by_name("password").send_keys("12345678")
driver.find_element_by_class_name("btn-lg").click()
driver.find_element_by_id("devices").click()
#driver.find_element_by_xpath("/html[@class='k-webkit k-webkit68']/body/div/div[@class='container container-content']/div[@class='rightArea']/div[@class='navbar-tabs']/div/ul[@class='nav nav-tabs']/li[@id='devices']/a").click()
#444444
print(driver.current_url)
# print(driver.title)
# print(driver.page_source)

#driver.find_element_by_id("cameraDashboard").click()

#efrat
# driver.refresh()
#


# driver.quit()
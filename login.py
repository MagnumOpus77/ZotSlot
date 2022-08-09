from selenium import webdriver
from selenium.webdriver.common.by import By


username = "wilhelaw"
password = "PotatoRebel890!"

url = "https://login.uci.edu/ucinetid/webauth?return_url=https://webreg2.reg.uci.edu:443/cgi-bin/wramia?page=login?call=0012&info_text=Reg+Office+Home+Page&info_url=https://www.reg.uci.edu/"

driver = webdriver.Chrome("/Users/will/Documents/chromedriver")

driver.get(url)


driver.find_element(By.ID, "ucinetid").send_keys(username)
driver.find_element(By.ID, "password").send_keys(password)
driver.find_element(By.NAME, "login_button").click()

print(driver.find_element(By.XPATH, "/html/body").text)
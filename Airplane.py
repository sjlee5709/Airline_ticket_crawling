from selenium import webdriver
browser = webdriver.Chrome()
browser.maximize_window()

url = "https://beta-flight.naver.com/"
browser.get(url)

browser.find_element_by_link_text("가는날 선택").click()

browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[0].click()

browser.find_elements_by_link_text("27")[1].click()
browser.find_elements_by_link_text("28")[1].click()

browser.find_elements_by_link_text("27")[0].click()
browser.find_elements_by_link_text("28")[1].click()

browser.find_element_by_xpath("//*[@id='recommendationList']/ul/li[1]").click()

browser.find_element_by_link_text("항공권 검색").click()
elem = webdriverwait(browser,10)/until(EC.presence_of_element_located((By.XPATH,"//*[@id='conten']/div[2]/div/div[4]/ul/li[1]")))
elem=browser.find_element_by_xpath("//*[@id='conten']/div[2]/div/div[4]/ul/li[1]")
print(elem.text)


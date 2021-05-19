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

print("hello")
print("hello")

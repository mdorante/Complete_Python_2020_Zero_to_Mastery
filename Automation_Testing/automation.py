from selenium import webdriver

# A basic introduction to automation testing with Selenium
# This automation script opens a browser, goes to a Selenium test page and inputs text to some fields and clicks on buttons

chrome_browser = webdriver.Chrome('./chromedriver')

chrome_browser.maximize_window()
chrome_browser.get(
    'https://www.seleniumeasy.com/test/basic-first-form-demo.html')


assert 'Show Message' in chrome_browser.page_source
enter_message = chrome_browser.find_element_by_id('user-message')
enter_message.clear()
enter_message.send_keys('This is cool')

button = chrome_browser.find_element_by_class_name('btn-default')
button.click()

assert 'Get Total'in chrome_browser.page_source
enter_a = chrome_browser.find_element_by_id('sum1')
enter_a.clear()
enter_a.send_keys('5')

enter_b = chrome_browser.find_element_by_id('sum2')
enter_b.clear()
enter_b.send_keys('3')

total_button = chrome_browser.find_element_by_css_selector(
    '#gettotal > .btn')
total_button.click()

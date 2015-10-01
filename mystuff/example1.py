from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.remote.webdriver import WebDriver

import time

def test_google(browser):
	browser.get("http://www.google.com")
	assert "Google" in browser.title
	search_box = browser.find_element_by_name("q")
	search_box.send_keys("toasters")
	search_box.send_keys(Keys.RETURN)
	
	browser.implicitly_wait(10)
	
	results = browser.find_element_by_id("ires")
	targets = results.find_elements_by_tag_name("a")
	link = None
	for target in targets:
		# print(target.get_attribute("href"))
		if target.get_attribute("href").startswith('http://www.amazon.com'):
			link = target.get_attribute("href")
	assert link != None
	# results = results.find_element_by_partial_link_text("amazon.com")
	
	#go to amazon
	browser.get(link)
	browser.implicitly_wait(5)
	assert "Amazon" in browser.title
	
	assert "Toaster" in browser.page_source
	
	assert "Oster" in browser.page_source
	
	items = browser.find_elements_by_class_name("celwidget")
	
	# print(items)
	n = 0 
	position = 0
	
	for item in items:
		if n == 0 :
			n = n + 1
		if "Oster" in item.text:
			oster_item = item
			position = n
			break
	assert oster_item != None
	assert position < 4
	
	text = oster_item.text
	print(text)
	lowest = 10000000.00
	for line in text.split("\n"):
		if line.startswith("$"):
			line = line.replace("$","")
			if " " in line:
				line = line.split(" ")[0]
			value = float(line)
			if lowest > value:
				lowest = value	
			print("Price = ", value)
			
	print("lowest value = ", lowest)
	
	assert lowest < 40.00
	print("PASS")
	
	search_box = browser.find_element_by_id("twotabsearchtextbox")
	search_box.send_keys("4-slice")
	search_box.send_keys(Keys.RETURN)
	
	assert "Oster" in browser.page_source
	
	items = browser.find_elements_by_class_name("celwidget")
	
	# print(items)
	n = 0 
	position = 0
	
	for item in items:
		if n == 0 :
			n = n + 1
		if "Oster" in item.text:
			oster_item = item
			position = n
			break
	assert oster_item != None
	assert position <= 2
	print ("PASS")
	
	stars_items = oster_item.find_elements_by_class_name("a-icon-star")
	for stars_item in stars_items:
		print(stars_item.text)
	
	print("PASS ALL")
	
	# spans = oster_item.find_elements_by_tag_name("span")
	# for span in spans:
	# 	print(span.text)
	
		# print (item.text)
	
options = webdriver.ChromeOptions()
options.add_experimental_option("excludeSwitches", ["ignore-certificate-errors","test-type"])
options.add_argument("--start-maximized")
options.add_argument("--disable-application-cache")
browser = webdriver.Chrome(chrome_options=options)

test_google(browser)
time.sleep(300)
browser.close()
	
	

# Browser = {
# 	"Chrome": 1,
# 	"Firefox": 2
# }

# driver = Browser["Chrome"]
# # driver = webdriver.Firefox()
# driver.get("http://www.python.org")
# assert "Python" in driver.title
# elem = driver.find_element_by_name("q")
# elem.send_keys("pycon")
# elem.send_keys(Keys.RETURN)
# assert "No results found." not in driver.page_source
# driver.close()
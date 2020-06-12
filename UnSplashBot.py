from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from time import sleep, strftime
from random import randint
import pandas as pd
import sys
import os

path = os.path.join("<directory path>", sys.argv[1])
try: 
    os.makedirs(path) 
    print("Directory '%s' created successfully" % directory) 
except: 
    print("Adding to directory")

path = '/Users/siddharth/Downloads/'+sys.argv[1]
chrome_options = webdriver.ChromeOptions()
prefs = {'download.default_directory' : path}
chrome_options.add_experimental_option('prefs', prefs)
chromedriver_path = '/Users/siddharth/Downloads/chromedriver' # Enter there to your own chromedriver path!
webdriver = webdriver.Chrome(executable_path=chromedriver_path,chrome_options=chrome_options)
sleep(2)
webdriver.get('https://unsplash.com')
sleep(3)

hashtag_list = [sys.argv[1]]

downloads = 0;
tag = -1
total = int(sys.argv[2])
for hashtag in hashtag_list:
	tag += 1
	webdriver.get('https://unsplash.com/s/photos/'+ hashtag_list[tag])
	sleep(5)
	first_thumbnail = webdriver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div[3]/div/div[1]/div/div/div[1]/div[1]/figure/div/div[1]/div/a')
	first_thumbnail.click()
	sleep(randint(1,2)) 
	try:
		for x in range(0,total):
			download = webdriver.find_element_by_xpath('/html/body/div[2]/div/div/div[4]/div/div/div[1]/div[1]/header/div[2]/div[3]/div/a/span').click()
			downloads+=1
			webdriver.find_element_by_css_selector('body > div.ReactModalPortal > div > div > div._3OTjU._3JvN7 > a').click()
			sleep(9)

	except Exception as e:
		print(e)
		continue

print('Downloads {}'.format(downloads))
sleep(25)
webdriver.close()

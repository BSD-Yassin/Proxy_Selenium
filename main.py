from selenium import webdriver
from selenium.webdriver.firefox.options import Options as FirefoxOptions
from selenium.webdriver.common.by import By
import time 
import random
import requests

# main url
url = ''

# returns a list of proxies from proxyscrape
proxies_api = 'https://api.proxyscrape.com/v2/?request=displayproxies&protocol=http&timeout=10000&country=all&ssl=all&anonymity=all'

# get the content and decodes the proxies from byte to string
proxies_bytes = requests.get(proxies_api).content
proxies = proxies_bytes.decode()

# splits the ips by line and puts them in a list
proxies_list = list(proxies.split())

""" Loop to : set a certain timer, generate a Firefox browser headlessly, use a proxy picked randomly """
while True: 

    proxy = random.choice(proxies_list)
    print("The set proxy for this run is %s" % proxy)
    
    # randomize between 1 min and 30 min
    duration = random.randrange(1,10) 
    min = round(duration/60)

    print("The set timer for this run is in %s seconds, meaning approx. %s minute " % (duration, min))
    timer = time.sleep(duration)

    ## sets up the driver with the proper options
    options = FirefoxOptions() 
    options.add_argument('--headless')
    options.add_argument('--proxy-server=%s' % proxy)
    driver = webdriver.Firefox(executable_path='geckodriver', options=options)
    
    print('Running the request:')
    driver.get(url)

    url_selector = '' 
    target_url = driver.find_element(By.CSS_SELECTOR,url_selector)
    
    #clicks on the targetted url
    target_url.click()

    # waiting for the page to load just in case
    time.sleep(5)
    driver.delete_all_cookies    
    
    # closing the browser
    driver.close()

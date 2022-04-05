from colorama import init, Fore
from csv import reader
import pandas as pd
from fake_useragent import UserAgent
from selenium.webdriver.common.by import By
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time, random
import threading
import json
from random import randint
from selenium.webdriver.common.action_chains import ActionChains
import requests
import requests.auth
from seleniumwire import webdriver
import warnings
from time import sleep
from liaison import *
warnings.filterwarnings('ignore')




def tres_bien_shop():
                #return the current Thread object which corresponds to the caller's thread of control
                t = threading.current_thread()

        

                fileObject = open("webscraping.json", "r")
                jsonContent = fileObject.read()
                List = json.loads(jsonContent)

                #choose a proxy in the text file if the user want a proxy
                if List["proxyless"] == "no":

                    choicefile = open('proxy.txt', 'r')
                    lineliste = []
                    for line in choicefile:
                        lineliste.append(line)
                    choice = random.choice(lineliste)
                else:
                    choice = ""
                    
                    
                #creat a new fingerprint for the chromewebdriver to be undetected with several tasks    
                
                #Rotating the useragent
                
                ua = UserAgent()
                user_agent = ua.chrome

                #allows the chromdriver to look like a lambda and non-automatic internet browser
                options = webdriver.ChromeOptions()

                
                #showing or not the interface of the chromedriver
                #Note: if your chromedriver is in headless mode, your task will be faster and you have less chance to be detected as a robot
                if List["headless"] == "no":
                    pass
                else:
                    options.add_argument('headless')


                options.add_argument(f'--disable-dev-shm-usage')
                options.add_argument("--start-maximized")
                options.add_argument(f'--disable-gpu')
                options.add_argument("--ignore-certificate-errors")
                options.add_argument('--ignore-ssl-errors')
                options.add_argument("--disable-infobars")
                options.add_argument("--disable-extensions")
                options.add_argument('--no-first-run --no-service-autorun --password-store=basic')
                options.add_argument("--lang=en-US")
                options.add_argument(f'--user-agent={user_agent}')
                options.add_experimental_option("useAutomationExtension", False)
                options.add_experimental_option("excludeSwitches", ["enable-automation"])

                
                #creat a new fingerprint for the chromewebdriver to be undetected with several tasks and to look like a humain user
                headers = {
                    'pragma': 'no-cache',
                    'cache-control': 'no-cache',
                    "accept": "text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3",
                    "accept-encoding": "gzip, deflate, br",
                    "accept-language": "en-US,en;q=0.9",
                    "DNT": "1",
                    "referer": "http://www.google.com/",
                    "origin": "http://www.google.com/",
                    'sec-ch-ua-mobile': '?0',
                    'sec-fetch-site': 'same-origin',
                    'sec-fetch-mode': 'navigate',
                    'sec-fetch-user': '?1',
                    'sec-fetch-dest': 'document',
                    'Upgrade-Insecure-Requests': '1',
                    'sec-ch-ua': '" Not A;Brand";v="99", '
                                 '"Chromium";v="96", "Google '
                                 'Chrome";v="96"',
                    'connection': 'keep-alive'

                }

                #enter the path of your csv file
                with open(".csv", 'r') as csv_file:
                    csv_reader = reader(csv_file)
                    list_of_rows = list(csv_reader)
                    # (list_of_rows)

                    r="yes"
                    list1 = [3, 4, 5]
                    z = [2, 3, 4, 5, 6]
                    y = [2, 3, 4, 5, 6]


                   
                    try:

                        row_number = s

                        #open the chromedriver navigator
                        driver = webdriver.Chrome(options=options)
                        
                        #search the url in the navigator
                        url = List['url']

                        driver.get(url)

                        #Change the property value of the navigator for webdriver to undefined
                        script = '''
                                                                                            Object.defineProperty(navigator, 'webdriver', {
                                                                                                get: () => undefined
                                                                                            })
                                                                                            '''
                        driver.execute_script(script)

                        try:
                            #send all the information about the fingerprint of the user in a request session
                            #Note:proxy must have this format: username:password@ip:port
                            
                            s = requests.Session()
                            header = s.get(url, headers=headers,proxies={'http': f'http://' + choice, 'https': f'http://' + choice}, verify=False)
                        except:
                            ("header doesn't work")


                        #wait 15 until the new page is loaded
                        driver.set_page_load_timeout(15)


                        print(Fore.GREEN + str(s1) + "    " + "start task[" + str(row_number) + "]")
                    except:
                        print(Fore.RED + "can't find url")
                        r = "no"


                if r == "no":
                    pass
                else:
                    try:
                        a = random.choice(list1)
                        zs = random.choice(z)
                        ys = random.choice(z)

                        #Wait that the element is clickable during 15 if the time is up the chromedriver will show a error
                       
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '/html/body/div[3]/header/div/div/div/a[1]/span')))

                        #search the fullxpath of the element and click on it but not in the center of the element to bypass bot protection
                        
                        search_xpath = driver.find_element(By.XPATH, '/html/body/div[3]/header/div/div/div/a[1]/span')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(search_xpath, ys, zs)
                        action.click()
                        action.perform()

                        #Do nothing during "a" secondes
                        #Note: we use a random number of secondes to look more like a humain
                        
                        sleep(a)
                        
                    except:
                        print(Fore.RED + "can't find enter button")
                        r = "no"

                if r == "no":
                    pass
                else:

                    a = random.choice(list1)


                    try:
                        
                        #Wait that the element is clickable during 15 if the time is up the chromedriver will show a error
                        
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="search"]')))

                        #search the xpath of the element and send a value to the element
                        
                        sneakers_element = driver.find_element(By.XPATH, '//*[@id="search"]').send_keys(sneaker_reference)
                        sneakers_element.send_keys(List['sneakers reference'])

                        sleep(a+3)

                    except:
                        print(Fore.RED + "can't find sneakers")
                        r="no"

                if r == "no":
                    pass
                else:



                    try:
                        a = random.choice(list1)
                        zs = random.choice(z)
                        ys = random.choice(z)

                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="cookie-allow"]')))

                        cookie_xpath = driver.find_element(By.XPATH, '//*[@id="cookie-allow"]')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(cookie_xpath, ys, zs)
                        action.click()
                        action.perform()

                        sleep(a+4)
                    except:
                        print(Fore.RED + "can't find popup")
                        r = "no"

                if r == "no":
                    pass
                else:
                    try:
                        zs = random.choice(z)
                        ys = random.choice(y)
                        a = random.choice(list1)

                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="kuLandingProductsListUl"]/li/div[2]/div[1]/a')))


                        search_xpath = driver.find_element(By.XPATH,
                                                           '//*[@id="kuLandingProductsListUl"]/li/div[2]/div[1]/a')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(search_xpath, ys, zs)
                        action.click(on_element=search_xpath)
                        action.perform()

                        sleep(a)
                    except:
                        print(Fore.RED + "can't find enter button 3")
                        r = "no"

                if r == "no":
                    pass
                else:


                    if List['fake/real fullname'] == "fake":

                        col_number = 5
                        value1 = list_of_rows[row_number - 1][col_number - 1]
                        col_number = 7
                        value2 = list_of_rows[row_number - 1][col_number - 1]

                    else:
                        col_number = 4
                        value1 = list_of_rows[row_number - 1][col_number - 1]
                        col_number = 6
                        value2 = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:


                        fullname_element = driver.find_element(By.XPATH, '//*[@id="fullname"]')
                        fullname_element.send_keys(value1+" "+value2)
                        sleep(a)
                        
                        #scroll to the element
                        driver.execute_script("arguments[0].scrollIntoView();", fullname_element)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find fullname")
                        r = "no"

                if r == "no":
                    pass
                else:

                    if List["paypal_email"] == "paypal":

                        col_number = 2
                        value = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 1
                        value = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:

                        email_element = driver.find_element(By.XPATH, '//*[@id="raffle-email"]')
                        email_element.send_keys(value)

                        sleep(a)

                    except:
                        print(Fore.RED + "can't find email")
                        r = "no"

                if r == "no":
                    pass
                else:


                    if List['fake/real address'] == "fake":

                        col_number = 17
                        value1 = list_of_rows[row_number - 1][col_number - 1]
                        col_number = 16
                        value2 = list_of_rows[row_number - 1][col_number - 1]

                    else:
                        col_number = 11
                        value2 = list_of_rows[row_number - 1][col_number - 1]
                        col_number = 12
                        value1 = list_of_rows[row_number - 1][col_number - 1]



                    if List['jig before address'] == "yes":

                        col_number = 32
                        value3 = list_of_rows[row_number - 1][col_number - 1]


                    else:

                        value3 = ""



                    if List['jig with street type'] == "yes":

                        col_number = 33
                        value4 = list_of_rows[row_number - 1][col_number - 1]


                    else:

                        value4 = ""

                    a = random.choice(list1)

                    try:

                        street_element = driver.find_element(By.XPATH, '//*[@id="address"]')
                        street_element.send_keys(value3 + "  " + value1 + "  " + value4 + "  " + value2)

                        sleep(a)

                    except:
                        print(Fore.RED + "can't find street")
                        r = "no"

                if r == "no":
                    pass
                else:


                    if List['fake/real address'] == "fake":

                        col_number = 18
                        value = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 13
                        value = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:

                        zipcode_element = driver.find_element(By.XPATH, '//*[@id="zipcode"]')
                        zipcode_element.send_keys(value)

                        sleep(a)

                    except:
                        print(Fore.RED + "can't find zipcode")
                        r = "no"

                if r == "no":
                    pass
                else:


                    if List['fake/real address'] == "fake":

                        col_number = 20
                        value = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 15
                        value = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:

                        city_element = driver.find_element(By.XPATH, '//*[@id="city"]')
                        city_element.send_keys(value)
                        sleep(a)
                        driver.execute_script("arguments[0].scrollIntoView();", city_element)

                        sleep(a)

                    except:
                        print(Fore.RED + "can't find city")
                        r = "no"

                if r == "no":
                    pass
                else:

                    col_number = 23
                    value = list_of_rows[row_number - 1][col_number - 1]

                    

                    try:
                        a = random.choice(list1)
                        zs = random.choice(z)
                        ys = random.choice(y)

                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="raffle-country"]')))
                        country_button = driver.find_element(By.XPATH, '//*[@id="raffle-country"]')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(country_button, ys, zs)
                        action.click()
                        action.perform()
                        sleep(a)

                        country1_xpath = '//*[@id="raffle-country"]'
                        country1_element = driver.find_element(By.XPATH, country1_xpath)
                        country1_element.send_keys(value)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find country")
                        r = "no"

                if r == "no":
                    pass
                else:
                    col_number = 10
                    value = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:

                        tel_element = driver.find_element(By.XPATH, '//*[@id="phone"]')
                        tel_element.send_keys(value)

                        sleep(a)

                    except:
                        print(Fore.RED + "can't find phone number")
                        r = "no"

                if r == "no":
                    pass
                else:


                    value_size = random.choice(List['size'])

                    a = random.choice(list1)

                    try:
                        zs = random.choice(z)
                        ys = random.choice(y)
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="Size_raffle"]')))
                        size_xpath = driver.find_element(By.XPATH, '//*[@id="Size_raffle"]')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(size_xpath, ys, zs)
                        action.click()
                        action.perform()
                        sleep(a)

                        zs = random.choice(z)
                        ys = random.choice(y)
                        size_xpath = driver.find_element(By.XPATH, '//*[@id="Size_raffle"]/option[' + value_size + ']')
                        size_xpath.click()
                        sleep(a+5)
                    except:
                        print(Fore.RED + "can't find size")
                        r = "no"


                if r == "no":
                    pass
                else:
                    try:

                        #bypass captcha
                        
                        #your 2captcha API key
                        API_KEY = List['2captcha API']
                        data_sitekey = '6LfjzmQUAAAAAJxTOcx3vYq3hroeYczGfDPU-NlX'
                        page_url = List['url']

                        #send a request to 2captcha service to solve the captcha and send back the solution
                        u1 = f"https://2captcha.com/in.php?key={API_KEY}&method=userrecaptcha&googlekey={data_sitekey}&pageurl={page_url}&json=1&invisible=1"
                        r1 = requests.get(u1)

                        #wait until the captcha is solved
                        rid = r1.json().get("request")
                        u2 = f"https://2captcha.com/res.php?key={API_KEY}&action=get&id={int(rid)}&json=1"
                        sleep(5)
                        while True:
                            r2 = requests.get(u2)

                            if r2.json().get("status") == 1:
                                form_tokon = r2.json().get("request")
                                break
                            sleep(5)
                            
                        #inject the solution in the g-recaptcha-response html to solve the captcha
                        write_tokon_js = f'document.getElementById("g-recaptcha-response").innerHTML="{form_tokon}";'
                        driver.execute_script(write_tokon_js)
                        print("captcha solve...")
                    except:
                        print(Fore.RED + "captcha can't be solved")
                        r = "no"

                if r == "no":
                    pass
                else:
                    try:

                        a = random.choice(list1)
                        zs = random.choice(z)
                        ys = random.choice(y)


                        enter2_button = driver.find_element(By.XPATH, '//*[@id="raffle-form"]/div[3]/button/span')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(enter2_button, ys, zs)
                        action.click()
                        action.perform()
                        sleep(a)


                        zs = random.choice(z)
                        ys = random.choice(y)

                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="raffle-form"]/div[3]/button')))
                        enter_button = driver.find_element(By.XPATH, '//*[@id="raffle-form"]/div[3]/button')
                        action = webdriver.common.action_chains.ActionChains(driver)
                        action.move_to_element_with_offset(enter_button, ys, zs)
                        action.click()
                        action.perform()

                        print(Fore.GREEN + "successfully enter task[" + str(row_number) + "]")
                        sleep(a+5)

                    except:
                        print(Fore.RED + "can't find enter button")


                driver.close()
                if List["mode"] == "normal":
                    sleep(10)
                    print(Fore.GREEN + "sleep during 10s")
                else:

                    min_delay = List['minimum delay']
                    max_delay = List['maximum delay']

                    g = randint(int(min_delay), int(max_delay))
                    v = g / 100
                    sleep(v)
                    print(Fore.GREEN + "sleep during " + str(v) + "s")





fileObject = open("webscraping.json", "r")
jsonContent = fileObject.read()
List = json.loads(jsonContent)

k = "yes"

#choose the line where we will start extracting the information from the csv
if List["custom_start_task"] == "yes":
    s = List["specific_line_start"]
else:
    s = 1
    
    
running = 0
threads = []
a = 0
#looping until x will egal to False
x=True
while x:

    #enter the path of your csv file
    with open(".csv", 'r') as csv_file:
        csv_reader = reader(csv_file)
        list_of_rows = list(csv_reader)
        # (list_of_rows)


        #Start to pick the information in the csv
        if List["paypal_email"] == "paypal":
            try:
                row_number = s
                col_number = 2
                value = list_of_rows[row_number - 1][col_number - 1]
            except IndexError:

                #close all the threads if that doesn't work and return to the main.py script
                x=False
                t.join()
                t.do_run = False
                print(Fore.WHITE + "program is over")
                print(Fore.WHITE + "Job done. Enjoy your day!")
                sleep(10)
                dict[3]()
        else:
            try:
                row_number = s
                col_number = 1
                value = list_of_rows[row_number - 1][col_number - 1]
            except IndexError:

                x=False
                t.join()
                t.do_run = False
                print(Fore.WHITE + "program is over")
                print(Fore.WHITE + "Job done. Enjoy your day!")
                sleep(5)
                dict[3]()

        #close all the threads if we have crossed the line where we must stop in the csv and choose to have a custom finish task 
        if List["custom_finish_task"] == "yes":
            if (int(s) > List["specific_line_finish"]):

                x=False
                t.join()
                t.do_run = False
                print(Fore.WHITE + "program is over")
                print(Fore.WHITE + "Job done. Enjoy your day!")
                sleep(5)
                dict[3]()
            else:
                pass

        #close all the threads if we have finish to read all the lines in the csv and choose to not have a custom finish task
        if List["custom_finish_task"] == "no":
            results = pd.read_csv('.csv', encoding='unicode_escape')

            if (int(s) == int(len(results))):
                x=False
                t.join()
                t.do_run = False
                print(Fore.WHITE + "program is over")
                print(Fore.WHITE + "Job done. Enjoy your day!")
                sleep(5)
                dict[3]()
            else:
                pass

        #when a thread is over, start a new one if the number of maximum tasks isn't reached 
        #Or if the task isn't alive, we reduce the running number in order to get new tasks
        if int(running) < int(List["number_of_task"]):

            t = threading.Thread(target=tres_bien_shop)
            threads.append(t)
            t.start()
            running += 1
            s += 1
            sleep(6)

        else:
            if t.is_alive() == False:
                running -= int(List["number_of_task"])













from colorama import init, Fore
from csv import reader
import pandas as pd
from fake_useragent import UserAgent
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
import time, random
import threading
import json
from random import randint
import requests
import requests.auth
from seleniumwire import webdriver
import warnings
from time import sleep
from liaison import *
warnings.filterwarnings('ignore')




def ballzy_shop():

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

                    r = "yes"
                    list1 = [3, 4, 5]

                    a = random.choice(list1)
                    
                    
                    try:
                        row_number = s
                        
                        #open the chromedriver navigator
                        driver = webdriver.Chrome(options=options)
                        
                        #search the url in the navigator
                        driver.get(List['url'])

                        
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
                            
                            header = requests.Session()
                            header.get(List['url'], headers=headers,proxies={'http': f'http://' + choice, 'https': f'http://' + choice}, verify=False)
                            
                        except:
                            ("header doesn't fully work")

                        #wait 15 until the new page is loaded
                        driver.set_page_load_timeout(15)


                        print(Fore.GREEN + str(s1) + "    " + "start task[" + str(row_number) + "]")
                    except:

                        print(Fore.RED + "can't find url")
                        r = "no"

                if r == "no":
                    pass
                else:


                    value_size = random.choice(List['size'])

                    a = random.choice(list1)

                    try:

                        #search the fullxpath of the element and click on it
                        size_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/form/select')
                        size_element.click()
                        sleep(a)

                        #search the fullxpath of the element and send a value to the element
                        size_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/form/select')
                        size_element.send_keys(value_size)
                        
                        #Do nothing during "a" secondes
                        #Note: we use a random number of secondes to look more like a humain
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find size")
                        r = "no"

                if r == "no":
                    pass
                else:

                    try:
                        #search the fullxpath of the element and click on it
                        enter_element = driver.find_element(By.XPATH, '/html/body/div[1]/div[2]/div/div[2]/div[2]/form/button')
                        enter_element.click()
                        sleep(a+8)

                    except:
                        print(Fore.RED + "can't find enter button")
                        r = "no"

                if r == "no":
                    pass
                else:


                    try:

                        a = random.choice(list1)


                        gender = ["mr", "mrs"]
                        random_gender = random.choice(gender)

                        if (random_gender == "mr"):
                            #search the xpath of the element and click on it
                            mr_xpath = driver.find_element(By.XPATH, '//*[@id="participant_gender1"]')
                            mr_xpath.click()


                        else:
                            #search the xpath of the element and click on it
                            mrs_xpath = driver.find_element(By.XPATH, '//*[@id="participant_gender2"]')
                            mrs_xpath.click()

                        sleep(a)

                    except:
                        print(Fore.RED + "can't find gender")
                        r = "no"

                if r == "no":
                    pass
                else:

                    if List["paypal_email"] == "paypal":

                        col_number = 2
                        email = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 1
                        email= list_of_rows[row_number - 1][col_number - 1]

                    try:
                        #search the xpath of the element and send a value to the element
                        email_element = driver.find_element(By.XPATH,'//*[@id="collapseOne"]/div/div[2]/input')
                        email_element.send_keys(email)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find email")
                        r = "no"

                if r == "no":
                    pass
                else:
                    col_number = 12
                    numero = list_of_rows[row_number - 1][col_number - 1]

                    col_number = 11
                    prefix_numero = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:
                        #search the xpath of the element and send a value to the element
                        tel_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[3]/input')
                        tel_element.send_keys('+' + prefix_numero + numero)
                        sleep(a)
                        
                        #scroll to the element
                        driver.execute_script("arguments[0].scrollIntoView();", tel_element)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find phone number")
                        r = "no"

                if r == "no":
                    pass
                else:

                    if List['fake/real firstname'] == "fake":

                        col_number = 5
                        firstname = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 4
                        firstname = list_of_rows[row_number - 1][col_number - 1]

                    try:
                        #search the xpath of the element and send a value to the element
                        firstname_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[4]/input')
                        firstname_element.send_keys(firstname)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find firstname")
                        r = "no"

                if r == "no":
                    pass
                else:


                    if List['fake/real lastname'] == "fake":

                        col_number = 7
                        lastname = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 6
                        lastname = list_of_rows[row_number - 1][col_number - 1]

                    try:
                        #search the xpath of the element and send a value to the element
                        lastname_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[5]/input')
                        lastname_element.send_keys(lastname)
                        sleep(a)

                    except:
                        print(Fore.RED +"can't find lastname")
                        r = "no"

                if r == "no":
                    pass
                else:

                    birthday = range(1, 30)
                    value1 = random.choice(birthday)

                    value2 = List['birthmonth']

                    birthyear = range(1985, 2002)
                    value3 = random.choice(birthyear)

                    try:

                        birthday_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[6]/div/select[1]')
                        birthday_element.click()
                        sleep(a)

                        birthday1_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[6]/div/select[1]')
                        birthday1_element.send_keys(value1)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find birthday")
                        r = "no"

                    try:

                        birthmonth_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[6]/div/select[2]')
                        birthmonth_element.click()
                        sleep(a)

                        birthmonth1_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[6]/div/select[2]')
                        birthmonth1_element.send_keys(value2)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find birthmonth")
                        r = "no"

                    try:

                        birthyear_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[6]/div/select[3]')
                        birthyear_element.click()
                        sleep(a)

                        birthyear1_element = driver.find_element(By.XPATH, '//*[@id="collapseOne"]/div/div[6]/div/select[3]')
                        birthyear1_element.send_keys(value3)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find birthmonth")
                        r = "no"

                if r == "no":
                    pass
                else:

                    col_number = 23
                    country = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:

                        country_selection_element = driver.find_element(By.XPATH, '//*[@id="addressCountry"]')
                        country_selection_element.click()
                        sleep(a)

                        country_selection_element = driver.find_element(By.XPATH, '//*[@id="addressCountry"]')
                        country_selection_element.send_keys(country)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find country")
                        r = "no"

                if r == "no":
                    pass
                else:

                    if List['fake/real address'] == "fake":

                        col_number = 20
                        city = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 15
                        city = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:

                        city_element = driver.find_element(By.XPATH, '//*[@id="collapseTwo"]/div/div[3]/input')
                        city_element.send_keys(city)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find city")
                        r = "no"

                if r == "no":
                    pass
                else:
                    a = random.choice(list1)


                    if List['fake/real address'] == "fake":

                        col_number = 16
                        street = list_of_rows[row_number - 1][col_number - 1]

                    else:
                        col_number = 11
                        street = list_of_rows[row_number - 1][col_number - 1]


                    if List['jig with street type'] == "yes":

                        col_number = 33
                        jig_with_street_type = list_of_rows[row_number - 1][col_number - 1]


                    else:

                        value4 = ""

                    try:

                        street_element = driver.find_element(By.XPATH, '//*[@id="collapseTwo"]/div/div[4]/input')
                        street_element.send_keys(jig_with_street_type + "  " + street)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find street")
                        r = "no"

                if r == "no":
                    pass
                else:

                    if List['fake/real address'] == "fake":

                        col_number = 17
                        streetnr = list_of_rows[row_number - 1][col_number - 1]


                    else:

                        col_number = 12
                        streetnr = list_of_rows[row_number - 1][col_number - 1]



                    if List['jig before address'] == "yes":

                        col_number = 32
                        jig_before_address = list_of_rows[row_number - 1][col_number - 1]


                    else:

                        jig_before_addres = ""
                    a = random.choice(list1)

                    try:

                        streetnr_element = driver.find_element(By.XPATH, '//*[@id="collapseTwo"]/div/div[5]/input')
                        sleep(a)
                        streetnr_element.send_keys(jig_before_addres + "  " + streetnr)
                        sleep(a)
                        driver.execute_script("arguments[0].scrollIntoView();", streetnr_element)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find street number")
                        r = "no"

                if r == "no":
                    pass
                else:


                    if List['fake/real address'] == "fake":

                        col_number = 18
                        zipcode = list_of_rows[row_number - 1][col_number - 1]


                    else:
                        col_number = 13
                        zipcode = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:
                        #Wait that the element is clickable during 15 if the time is up the chromedriver will show a error 
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH, '//*[@id="collapseTwo"]/div/div[6]/input')))
                        zipcode_element = driver.find_element(By.XPATH, '//*[@id="collapseTwo"]/div/div[6]/input')
                        zipcode_element.send_keys(zipcode)
                        sleep(a)

                    except:
                        print(Fore.RED +"can't find zipcode")
                        r = "no"

                if r == "no":
                    pass
                else:

                    try:
                        terme_element = driver.find_element(By.XPATH, '//*[@id="participant_approval"]')
                        terme_element.click()
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find terme button")
                        r = "no"

                if r == "no":
                    pass
                else:

                    a = random.choice(list1)

                    try:
                        enter2_element = driver.find_element(By.XPATH, '/html/body/div[1]/div/form/button')
                        enter2_element.click()
                        sleep(a+8)

                    except:
                        print(Fore.RED + "can't find enter button")
                        r = "no"

                if r == "no":
                    pass
                else:
                    col_number = 27
                    card_number = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)
                    
                    #switch to iframe to be able to continue the webscraping
                    driver.switch_to.frame(0)

                    try:
                        #Wait that the element is clickable during 15 if the time is up the chromedriver will show a error
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH,
                             '/html/body/div/div/div/div/div/form/div[1]/div[1]/div/input')))
                        card_number_button = driver.find_element(By.XPATH,
                                                                 '/html/body/div/div/div/div/div/form/div[1]/div[1]/div/input')
                        
                        #scroll to the element
                        driver.execute_script("arguments[0].scrollIntoView();", card_number_button)
                        sleep(a)

                        card_number_button.send_keys(card_number)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find card number")
                        r="no"

                if r == "no":
                    pass
                else:

                    col_number = 26
                    card_holder = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:
                        card_holder_element = driver.find_element(By.XPATH,
                                                                  '/html/body/div/div/div/div/div/form/div[1]/div[2]/div/input')
                        card_holder_element.send_keys(card_holder)
                        sleep(a)

                    except:
                        print(Fore.RED + "can't find card holder")
                        r="no"

                if r == "no":
                    pass
                else:
                    col_number = 28
                    card_expiration_month = list_of_rows[row_number - 1][col_number - 1]

                    col_number = 29
                    card_expiration_year = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:
                        #Wait that the element is clickable during 15 if the time is up the chromedriver will show a error
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH,
                             '/html/body/div/div/div/div/div/form/div[1]/div[3]/div[1]/div/div/input')))

                        card_expiration_button = driver.find_element(By.XPATH,
                                                                     '/html/body/div/div/div/div/div/form/div[1]/div[3]/div[1]/div/div/input')
                        card_expiration_button.send_keys(card_expiration_month + "/" + card_expiration_year)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find card expiration")
                        r = "no"

                if r == "no":
                    pass
                else:
                    col_number = 30
                    card_cvc = list_of_rows[row_number - 1][col_number - 1]

                    a = random.choice(list1)

                    try:
                        #Wait that the element is clickable during 15 if the time is up the chromedriver will show a error
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH,
                             '/html/body/div/div/div/div/div/form/div[1]/div[3]/div[2]/div/div/input')))

                        card_cvc_button = driver.find_element(By.XPATH,
                                                              '/html/body/div/div/div/div/div/form/div[1]/div[3]/div[2]/div/div/input')
                        card_cvc_button.send_keys(card_cvc)
                        sleep(a)
                    except:
                        print(Fore.RED + "can't find card cvc")
                        r = "no"

                if r == "no":
                    pass
                else:

                    a = random.choice(list1)

                    try:
                        enter3_element = driver.find_element(By.XPATH, '/html/body/div/div/div/div/div/form/div[2]/button')
                        enter3_element.click()
                        sleep(a+15)
                    except:
                        print(Fore.RED + "can't find enter button")
                        r = "no"

                if r == "no":
                    pass
                else:
                    try:
                       
                        a = random.choice(list1)

                        #switch to come out of all the frames and to focus at the page
                        driver.switch_to.default_content()
                        wait = WebDriverWait(driver, 15)
                        wait.until(expected_conditions.element_to_be_clickable(
                            (By.XPATH,
                             '//*[@id="payment-form"]/button')))
                        enter_xpath = driver.find_element(By.XPATH,
                                                          '//*[@id="payment-form"]/button')
                        enter_xpath.click()

                        print(Fore.GREEN + "successfully enter task[" + str(row_number) + "]")
                        sleep(a+5)

                    except:
                        p = "can't find enter button"
                        print(Fore.RED + p)


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

            t = threading.Thread(target=ballzy_shop)
            threads.append(t)
            t.start()
            running += 1
            s += 1

            sleep(6)
        else:
            if t.is_alive() == False:
                running -= int(List["number_of_task"])

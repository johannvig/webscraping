from colorama import init, Fore
import warnings
from time import sleep
warnings.filterwarnings('ignore')


def proxy():
    
    name_proxy_file = input(Fore.WHITE + "what is the name of your text file where you put your proxies?")

    print(Fore.WHITE + "What is the format of your proxies?(enter your option)")
    print(Fore.WHITE + "1. ip:port:username:password")
    print(Fore.WHITE + "2. ip:port  username and password are unique")
    print(Fore.WHITE + "Type the number:")
    option = input()
    
    
    choicefile1 = open(str(name_proxy_file) + '.txt', 'r')
    
    #read every lines of the text file one by one
    choice1 = choicefile1.readlines()

    if option == "1":

        n = 0

        x = True

        while x:
            try:
                #choose one line of the text file
                choice = choice1[n]
                
                #deconstructs all the previous strcture to recondition a new one
                #replace ':' by a space
                mot = choice.replace(':', ' ')

                #separates the different parts by a space
                séparer = mot.split(' ')

                
                ip = séparer[0]

                port = séparer[1]

                username = séparer[2]

                password = séparer[3]

                proxy = username + ":" + password + "@" + ip + ":" + port

                f = open('generator\\formatted proxy .txt', 'a+', encoding="utf-8") #you can change the path of the formatted proxy.py file
                
                #write the new proxy structure in the text file
                f.writelines(str(proxy) + "\n")

                f.close()

                n += 1

            except:
                f.close()
                x = False
    else:

        username = input(Fore.WHITE + "What is your username?")
        
        password = input(Fore.WHITE + "What is you password?")

        n = 0

        x = True

        while x:
            try:
                choice = choice1[n]

                mot = choice.replace(':', ' ')

                séparer = mot.split(' ')

                ip = séparer[0]

                port = séparer[1]

                proxy = username + ":" + password + "@" + ip + ":" + port

                f = open('generator\\formatted proxy .txt', 'a+', encoding="utf-8")
                f.writelines(str(proxy) + "\n")

                n += 1

            except:
                f.close()
                x = False


proxy()
print(Fore.WHITE + "program is over")
print(Fore.WHITE + "Job done. Enjoy your day!")

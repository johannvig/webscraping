# Import necessary libraries
from colorama import init, Fore
import warnings
from time import sleep

# Disable warning messages
warnings.filterwarnings('ignore')

def proxy():
    # Get the name of the proxy file from user input
    name_proxy_file = input(Fore.WHITE + "What is the name of your text file where you put your proxies? ")

    # Get the format of the proxies from user input
    print(Fore.WHITE + "What is the format of your proxies? (enter your option)")
    print(Fore.WHITE + "1. ip:port:username:password")
    print(Fore.WHITE + "2. ip:port  username and password are unique")
    option = input("Type the number: ")

    # Open the proxy file
    with open(name_proxy_file + '.txt', 'r') as proxy_file:
        # Read all lines of the file
        proxy_list = proxy_file.readlines()

        # If option 1 is selected
        if option == "1":
            n = 0
            while True:
                try:
                    # Get the next line from the proxy list
                    proxy_line = proxy_list[n]
                    
                    # Split the proxy line into its components
                    ip, port, username, password = proxy_line.strip().split(':')
                    
                    # Format the proxy string
                    formatted_proxy = f"{username}:{password}@{ip}:{port}"

                    # Write the proxy string to a file
                    with open('generator\\formatted proxy.txt', 'a+', encoding="utf-8") as output_file:
                        output_file.write(formatted_proxy + "\n")

                    n += 1
                except IndexError:
                    break

        # If option 2 is selected
        elif option == "2":
            username = input(Fore.WHITE + "What is your username? ")
            password = input(Fore.WHITE + "What is your password? ")
            n = 0
            while True:
                try:
                    # Get the next line from the proxy list
                    proxy_line = proxy_list[n]
                    
                    # Split the proxy line into its components
                    ip, port = proxy_line.strip().split(':')
                    
                    # Format the proxy string
                    formatted_proxy = f"{username}:{password}@{ip}:{port}"

                    # Write the proxy string to a file
                    with open('generator\\formatted proxy.txt', 'a+', encoding="utf-8") as output_file:
                        output_file.write(formatted_proxy + "\n")

                    n += 1
                except IndexError:
                    break

    # Print completion messages
    print(Fore.WHITE + "Program is over")
    print(Fore.WHITE + "Job done. Enjoy your day!")

# Call the proxy function
proxy()


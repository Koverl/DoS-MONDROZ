import time
import requests
from colorama import Fore, Style, init

# Initialize colorama
init(autoreset=True)

# Print ASCII art in green
print(Fore.GREEN + """
##   ##   ## ##   ###  ##  ### ##   ### ##    ## ##   ### ##   
 ## ##   ##   ##    ## ##   ##  ##   ##  ##  ##   ##  ##  ##   
# ### #  ##   ##   # ## #   ##  ##   ##  ##  ##   ##     ##    
## # ##  ##   ##   ## ##    ##  ##   ## ##   ##   ##    ##     
##   ##  ##   ##   ##  ##   ##  ##   ## ##   ##   ##   ##      
##   ##  ##   ##   ##  ##   ##  ##   ##  ##  ##   ##  ##  ##   
##   ##   ## ##   ###  ##  ### ##   #### ##   ## ##   # ####""")

# Print choices in green
choices = input(Fore.GREEN + """What would you like to choose?
                1: DoS
                2: IpLookup
                3: exit\n\n\n""")

if choices == "1":
    address = input("Which IP are you attacking?\n")
    attack = ("Attacking Host/Network " + address + " with 64000 requests and bytes sent\n\n" * 100)
    for _ in range(100):
        print(Fore.GREEN + attack)
        time.sleep(0.90)

elif choices == "2":
    ip_address = input("Enter the IP address for lookup:\n")
    print(Fore.GREEN + "Performing IP Lookup...")
    
    response = requests.get(f"https://ipinfo.io/{ip_address}/json")
    
    if response.status_code == 200:
        ip_info = response.json()
        print(Fore.GREEN + f"IP Address: {ip_info.get('ip', 'N/A')}")
        print(Fore.GREEN + f"Hostname: {ip_info.get('hostname', 'N/A')}")
        print(Fore.GREEN + f"City: {ip_info.get('city', 'N/A')}")
        print(Fore.GREEN + f"Region: {ip_info.get('region', 'N/A')}")
        print(Fore.GREEN + f"Country: {ip_info.get('country', 'N/A')}")
        print(Fore.GREEN + f"Location: {ip_info.get('loc', 'N/A')}")
        print(Fore.GREEN + f"Organization: {ip_info.get('org', 'N/A')}")
        print(Fore.GREEN + f"Postal: {ip_info.get('postal', 'N/A')}")
    else:
        print(Fore.GREEN + "Failed to perform IP lookup. Please check the IP address and try again.")

elif choices == "3":
    print(Fore.GREEN + "Exiting")
    exit()

else:
    print(Fore.GREEN + "Invalid choice. Please choose 1, 2, or 3.")

from colorama import Fore, Back, Style, init
import json
import requests
import sys

init(convert=True)

def globalData():
    url = "https://api.covid19api.com/summary"
    error = "You have reached maximum request limit."
    response = requests.get(url).text
    while response==error:
        response = requests.get(url).text
    data = json.loads(response)
    dataSet = data["Global"]
    print(Fore.GREEN+"You are viewing the data of "+Fore.YELLOW+"entire world as a whole"+Fore.WHITE+".\n"+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"New Confirmed: "+Fore.YELLOW+str(dataSet["NewConfirmed"])+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"New Recovered: "+Fore.YELLOW+str(dataSet["NewRecovered"])+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"New Deaths: "+Fore.YELLOW+str(dataSet["NewDeaths"])+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"Total Active: "+Fore.YELLOW+str(int(dataSet["TotalConfirmed"])-int(dataSet["TotalRecovered"])-int(dataSet["TotalDeaths"]))+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"Total Confirmed: "+Fore.YELLOW+str(dataSet["TotalConfirmed"])+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"Total Recovered: "+Fore.YELLOW+str(dataSet["TotalRecovered"])+Style.RESET_ALL)
    print(Back.RED+Fore.WHITE+"Total Deaths: "+Fore.YELLOW+str(dataSet["TotalDeaths"])+Style.RESET_ALL)
    sys.exit("\n\n"+Fore.BLUE+Back.WHITE+"Thank You for using!"+Style.RESET_ALL+"\n")
    
def country(code):
    url = "https://api.covid19api.com/summary"
    error = "You have reached maximum request limit."
    response = requests.get(url).text
    while response==error:
        response = requests.get(url).text
    data = json.loads(response)["Countries"]
    for dataSet in data:
        if code.upper() in dataSet["CountryCode"]:
            print(Fore.GREEN+"You are viewing the data of "+Fore.YELLOW+str(dataSet["Country"])+Fore.WHITE+".\n"+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"New Confirmed: "+Fore.YELLOW+str(dataSet["NewConfirmed"])+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"New Recovered: "+Fore.YELLOW+str(dataSet["NewRecovered"])+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"New Deaths: "+Fore.YELLOW+str(dataSet["NewDeaths"])+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"Total Active: "+Fore.YELLOW+str(int(dataSet["TotalConfirmed"])-int(dataSet["TotalRecovered"])-int(dataSet["TotalDeaths"]))+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"Total Confirmed: "+Fore.YELLOW+str(dataSet["TotalConfirmed"])+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"Total Recovered: "+Fore.YELLOW+str(dataSet["TotalRecovered"])+Style.RESET_ALL)
            print(Back.RED+Fore.WHITE+"Total Deaths: "+Fore.YELLOW+str(dataSet["TotalDeaths"])+Style.RESET_ALL)
    sys.exit("\n\n"+Fore.BLUE+Back.WHITE+"Thank You for using!"+Style.RESET_ALL+"\n")
            
if __name__ == "__main__":
    sys.stderr.write("\x1b[2J\x1b[H")
    print(Fore.WHITE+Back.BLUE+"\nCOVID-19 Tracking Command-line Utility for the Modern World"+Style.RESET_ALL)
    print(Fore.GREEN+"This utility is brought to you by "+Fore.YELLOW+Back.RED+"U-TEC 31337"+"."+Style.RESET_ALL)
    print("\nTo view the Global records, run the utility without any arguments.\nFor example:\n"+Fore.WHITE+Back.BLUE+"python main.py\n"+Fore.YELLOW+Back.BLACK+"This command will provide you the global data."+Style.RESET_ALL)
    print("\nTo view the records of a particular country, run the utility by passing the country code as argument.\nFor example:\n"+Fore.WHITE+Back.BLUE+"python main.py np\n"+Fore.YELLOW+Back.BLACK+"This command will provide you the records of Nepal."+Style.RESET_ALL+"\n\n")
    if len(sys.argv) == 1:
        globalData()
    elif len(sys.argv) == 2:
        country(sys.argv[1])
    else:
        sys.exit(Fore.WHITE+Back.BLUE+"Invalid Arguments Passed!"+"\n\n"+Fore.BLUE+Back.WHITE+"Thank You for using!"+Style.RESET_ALL+"\n")
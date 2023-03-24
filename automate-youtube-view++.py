import time
from selenium import webdriver
from colorama import Fore
from banner import banner

banner.killo()
banner.bannerKilloYT()

PATH = input("Enter links.txt path: [/home/user/../link.txt or C:/../links.txt] \n>>> ")
view_time = int(input("Set view length in second [minimum 15] \n>>> "))

file = open(PATH, "r")
links = [line for line in file]
file.close()
# print(*links)

numberOfLinks = len(links)
#print(numberOfLinks)
counter = 0
views = 0
while True:
    try:
        driver = webdriver.Firefox()
        driver.get(links[counter])
        playButton = driver.find_element_by_xpath('//*[@id="player"]')
        playButton.click()
        counter += 1
        time.sleep(view_time+2)
        if(counter == numberOfLinks):
            counter = 0
        driver.quit()
        views +=1
        print(Fore.LIGHTBLUE_EX + "[" + Fore.LIGHTGREEN_EX + " + " + Fore.LIGHTBLUE_EX + "]" + Fore.WHITE + " Checked")
        
    except:
        print(Fore.LIGHTGREEN_EX + "_____________________________________")
        if(views >= 1):
            print(Fore.LIGHTBLUE_EX + "[" + Fore.LIGHTGREEN_EX + " + " + Fore.LIGHTBLUE_EX + "]" + Fore.WHITE, views, "views collected")
        else:
            print(Fore.LIGHTRED_EX + "[" + Fore.LIGHTYELLOW_EX + " ! " + Fore.LIGHTRED_EX + "]" + Fore.WHITE, views, "view collected")
        print("Program closed")
        print(Fore.LIGHTGREEN_EX + "_____________________________________\n")

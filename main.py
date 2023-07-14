from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from valRank import getRanks
from helper import ranksToTier
from typing import List
import player
import IO

#if selenium isnt installed run pip install selenium





def run(filepath):
    #OPTIMIZATIONS
    checkTier1=True
    #read in the usernames and tier they are applying for
    players:List[player.player] = []
    players = IO.input(filepath)
    #find peak rank of player within act 4  
    driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
    names = []
    tiers = []
    validity = []
    for person in players:

        IGN = person.ign
        TIER = person.claimedTier
        names.append(IGN)
        tiers.append(TIER)
        if ((checkTier1 and TIER==1) or TIER ==2):
            driver.get("https://tracker.gg/valorant")

            searchBar = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div/main/div[3]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input")
            searchBar.send_keys(IGN)
            searchBar.send_keys(Keys.RETURN)


            time.sleep(5)
            #check whether peak rank fits tier

            #print (TIER)
            x = ranksToTier(getRanks(driver.current_url,driver))
            if x == 3:
                validity.append("ERROR OCCURED")
            else :validity.append(x==TIER)
            #validity.append(TIER == ranksToTier(getRanks(driver.current_url,driver)))
            time.sleep(1)
        elif (not checkTier1 and TIER ==1 ):
            validity.append(True)

    driver.close()
    driver.quit()

    # for item in names+tiers+validity:
    #     print (item)



    #output to file
    IO.output("output.csv",names,tiers,validity)

run("input.csv")
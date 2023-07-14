
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import time
from helper import validRank


#add these to the end of the URL to get certain episode ranks
E4ACTURLS = ["?season=573f53ac-41a5-3a7d-d9ce-d6a6298e5704","?season=d929bc38-4ab6-7da4-94f0-ee84f8ac141e","?season=3e47230a-463c-a301-eb7d-67bb60357d4f"]

#driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
#TAKES CURRENT ACT AND EPISODE RANK AND PRODUCES ACT 1 + ACT 2 + ACT 3
def getRanks(URL,driver):
    list = []
    driver.get(URL)


    for item in E4ACTURLS:
        driver.get(URL+item)
        #competitiveButton = driver.find_element(by=By.XPATH, value = "/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[2]/div/div[1]/div/ul/li[1]/span")
        #competitiveButton.click()
        
        # strrank = ""
        # try:
        #     altsearch = driver.find_element(by=By.XPATH,value="/html/body/div/div[2]/div[2]/div/main/div[3]/div[3]/div[3]/div[2]/div[1]/div[2]/div[2]/div/div/div[1]/span[2]")
        #     if validRank(altsearch.text):
        #         strrank=altsearch.text
        #     else:
        #         strrank = "ERROR COULD NOT FIND RANK - webpage missing element?"
        # except Exception:
        #     strrank="ERROR COULD NOT FIND RANK - profile not public?"



        search = driver.find_elements(by=By.CLASS_NAME, value="stat__value")
        
        #gives 2 different responses, sometimes correct value at index 0 sometimes at 6, keep in mind player may not have profile set to public
        strrank = ""
        try:
            if validRank(search[0].text):
                strrank = search[0].text
            elif validRank(search[6].text):
                strrank = search[6].text
            else:
                strrank = "ERROR COULD NOT FIND RANK - CODE 1"
        except Exception:
            strrank = "ERROR COULD NOT FIND RANK - CODE: 2"
        list.append(strrank)
    return list

#print(getRanks("https://tracker.gg/valorant/profile/riot/BubblySnowflake%236969/overview",driver))













from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.common.keys import Keys

from selenium.webdriver.common.by import By
import time
from helper import validRank


#add these to the end of the URL to get certain episode ranks
E4A3 = "?season=3e47230a-463c-a301-eb7d-67bb60357d4f"
E4A2 = "?season=d929bc38-4ab6-7da4-94f0-ee84f8ac141e"
E4A1 = "?season=573f53ac-41a5-3a7d-d9ce-d6a6298e5704"

driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))




driver.get("https://tracker.gg/valorant")


search = driver.find_element(by=By.XPATH, value="/html/body/div/div[2]/div[2]/div/main/div[3]/div/div[1]/div/div/div[1]/div[2]/div[1]/form/input")
search.send_keys("sen tenz#0505")
search.send_keys(Keys.RETURN)

time.sleep(10)
driver.quit()
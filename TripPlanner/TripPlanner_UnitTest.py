'''
Created on Oct 18, 2018

@author: Shirantha
'''
import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TripPlannerTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Firefox()
        
    def test_verify_trips(self):
        
        # Define variable values
        URL = "https://transportnsw.info/trip"
        FROM = "North Sydney Station, North Sydney"
        TO = "Wynyard Station, Sydney"
        
        driver = self.driver
        driver.maximize_window()
        driver.get(URL)

        # Look for the "From" input box and enter starting point of journey
        eleFrom = driver.find_element_by_id("search-input-From")
        eleFrom.clear()
        eleFrom.send_keys(FROM)
        eleFrom.send_keys(Keys.ARROW_DOWN)

        # wait for the dropdown option to appear and choose it
        first_option = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#suggestion-From-0")))
        first_option.send_keys(Keys.RETURN)

        # Look for the "To" input box and enter destination
        eleTo = driver.find_element_by_id("search-input-To")
        eleTo.clear()
        eleTo.send_keys(TO)        
        eleTo.send_keys(Keys.ARROW_DOWN)

        # wait for the dropdown option to appear and choose it
        first_option_to = WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "#suggestion-To-0")))
        first_option_to.send_keys(Keys.RETURN)

        # Look for the "Go" button * click it
        eleGo = driver.find_element_by_xpath("//*[@id='search-button']")
        eleGo.click()

        # wait for the search results appears
        WebDriverWait(driver, 20).until(EC.visibility_of_element_located((By.CLASS_NAME, "tripResults")))
        
        # Store trip results in a list
        lists= driver.find_elements_by_class_name("tripResults");
        
        noOfTrips = len(lists)
        
        # Assert if there are no trips found
        self.assertNotEqual(noOfTrips, 0, "No trips found between the given locations.")
            
        # Extract and display the trip results
        print (str(noOfTrips) + " Trips found From: "+ FROM + " TO: " + TO + "\n")
        
        anchorStr = ""
        i=0
        for listitem in lists:
            print ("Trip number", i+1 )

            anchorStr = "#tripAnchor"+ str(i)
    
            # Extract Departure Time
            depTime = listitem.find_element_by_css_selector( anchorStr + " > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(3)")
            print ("Departure Time: ", depTime.get_attribute('innerHTML'))

            # Extract Arrival Time    
            arrTime = listitem.find_element_by_css_selector( anchorStr + " > div:nth-child(1) > div:nth-child(1) > div:nth-child(1) > div:nth-child(2) > div:nth-child(1) > div:nth-child(2) > span:nth-child(6)")   
            print ("Arrival Time  : ", arrTime.get_attribute('innerHTML'))    
            print("=======================")
    
            anchorStr=""
            i=i+1
    
    def tearDown(self):
        self.driver.close()
            
if __name__ == "__main__":
    unittest.main()
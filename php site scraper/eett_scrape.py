import csv
import re
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select, WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException
from selenium.webdriver.firefox.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.common.exceptions import StaleElementReferenceException, TimeoutException, NoSuchElementException

#firefox options
firefox_options = Options()
firefox_options.headless = True
#below -- use in case something is obscured by page size
#firefox_options.add_argument("--width=1020")
#firefox_options.add_argument("--height=1440") 
firefox_profile = webdriver.FirefoxProfile()
firefox_profile.set_preference("browser.tabs.warnOnClose", False)
firefox_profile.set_preference("browser.tabs.warnOnCloseOtherTabs", False)
firefox_profile.set_preference("browser.tabs.warnOnOpen", False)
firefox_options.profile = firefox_profile

"""
with open('FILENAME.csv', 'w', newline='') as csvfile:
"""
        csvwriter = csv.writer(csvfile)

        for i in range(1, 26):


            """
            #open firefox
            driver = webdriver.Firefox(options=firefox_options)
            #open site 
            driver.get("https://keraies.eett.gr/anazhthsh.php")

            #wait for element
            select_div = WebDriverWait(driver, 10).until(
                EC.visibility_of_element_located((By.XPATH, '//div[@class="col-xs-9"]//select[@name="municipality"]'))
            )
            """
            #select object
            select = Select(select_div)

            #select variable from dropdown
            """
            select.select_by_visible_text("SEARCH TERM")
            """

            # Locate and click the search button
            search_button = WebDriverWait(driver, 10).until(
                EC.element_to_be_clickable((By.XPATH, "//button[@class='btn my-form-btn' and text()='Αναζήτηση']"))
            )
            search_button.click()
            #wait for content
            WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.TAG_NAME, "tr")))

               
            """
            #Construct the XPath for the <td> element in the ith row
            td_xpath = f"/html/body/div[2]/table/tbody/tr[{i}]/td[1]"
            
            csv_data = []
            for j in range(1, 6):
                cell_xpath = f"/html/body/div[2]/table/tbody/tr[{i}]/td[{j}]"
                cell_element = driver.find_element(By.XPATH, cell_xpath)
                cell_text = cell_element.text.strip()
                csv_data.append(cell_text)
            """
            print (csv_data)

            #find row
            td_element = driver.find_element(By.XPATH, td_xpath)

            #open more info
            number_inside_td = td_element.text.strip()

            #print (number_inside_td)
            """
            search_button_info = WebDriverWait(driver, 10).until(
            EC.element_to_be_clickable((By.XPATH, f"/html/body/div[2]/table/tbody/tr[{i}]/td[7]/a")))
            search_button_info.click()
                

            #csv_data.extend(list)
            #read coords
            page_text = driver.find_element(By.TAG_NAME, "body").text
            coordinates = re.findall(r'\b\d{2}\.\d+\b', page_text)
            """

            csv_data.extend(coordinates)
            #write to csv
            csvwriter.writerow(csv_data)

            time.sleep(3)
                
            #finally:
            driver.quit()

driver.quit()


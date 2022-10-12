from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.common.exceptions import NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException

ser = Service(r"C:\Development\chromedriver")
options = webdriver.ChromeOptions()
driver = webdriver.Chrome(service=ser, options=options)


driver.get("https://www.linkedin.com/jobs/search?keywords=Software%20Engineer&location=Australia&geoId=101452733&trk=public_jobs_jobs-search-bar_search-submit&position=1&pageNum=0r")

sign_in = driver.find_element(By.XPATH, "/html/body/div[1]/header/nav/div/a[2]")
sign_in.click()

email = driver.find_element(By.XPATH, '//*[@id="username"]')
email.send_keys("phonenumber")
password = driver.find_element(By.XPATH, '//*[@id="password"]')
password.send_keys("password")
sign_in_2 = driver.find_element(By.XPATH, '//*[@id="organic-div"]/form/div[3]/button')
sign_in_2.click()


jobs = driver.find_elements(By.CLASS_NAME, 'jobs-search-results__list-item')
for i, job in enumerate(jobs):
    try:
        job.click()
        ##this code saves only
        save_init = driver.find_element(By.CLASS_NAME, 'jobs-save-button')
        save_init.click()


        ## Below code opens job (apply) and then saves by closing
        # apply = driver.find_element(By.CSS_SELECTOR, '.jobs-apply-button')
        # apply.click()
        # cancel = driver.find_element(By.CLASS_NAME, 'artdeco-button__icon')
        # cancel.click()
        # save = driver.find_element(By.CLASS_NAME, 'artdeco-modal__confirm-dialog-btn')
        # save.click()
        print("Job Saved")
    except (NoSuchElementException, StaleElementReferenceException, ElementClickInterceptedException):
        print("Job skipped")

driver.close()
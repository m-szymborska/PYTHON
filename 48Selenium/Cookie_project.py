from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
import time

chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrom_option)

driver.get("https://orteil.dashnet.org/experiments/cookie/")

duration = 1 * 60
interval = 5
start_time = time.time()
end_time = start_time + duration
actions = ActionChains(driver)


while time.time() < end_time:

    remaining_time = end_time - time.time()
    minutes, seconds = divmod(remaining_time, 60)
    cookie = driver.find_element(By.ID, value="cookie")
    cookie.click()









# driver.quit()


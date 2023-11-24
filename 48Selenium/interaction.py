from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrom_option)
# driver.get("https://en.wikipedia.org/wiki/Main_Page")
driver.get("http://secure-retreat-92358.herokuapp.com/")

# number_article = driver.find_element(By.XPATH, value='//*[@id="articlecount"]/a[1]')
# number_article = driver.find_element(By.ID, value="articlecount")
# stat = number_article.find_element(By.TAG_NAME, value="a")

# klikanie linku =========================== n
# stat.click()
# anyone_can = driver.find_element(By.LINK_TEXT, value="anyone can edit")
# anyone_can.click()

# wpisywanie okienka i klikniecie==========================owy import

# search = driver.find_element(By.NAME, value="search")
# search.send_keys("Python")
# search.send_keys(Keys.ENTER)


# challenge
name = driver.find_element(By.NAME, value="fName")
l_name = driver.find_element(By.NAME, value="lName")
mail = driver.find_element(By.NAME, value="email")

name.send_keys("Python")
l_name.send_keys("Pythonbit")
mail.send_keys("aasjdhdj@dd.pl")

submit = driver.find_element(By.CSS_SELECTOR, value="form button")
submit.click()
# mail.send_keys(Keys.ENTER)




# driver.quit()
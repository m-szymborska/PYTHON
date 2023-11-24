import requests
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys

google_form = \
    ('https://docs.google.com/forms/d/e/'
     '1FAIpQLScFh22ghE074jU70TLhAuM2IaTgflvP3Jw32GoZPNVx--h_iw/viewform?usp=sf_link')

zillow_link = "https://appbrewery.github.io/Zillow-Clone/"

end_link = "https://docs.google.com/forms/d/11A9zGO_IK7cZZcakevARuICfFZKUT1wUqn6iLIyAKPg/edit#responses"

response = requests.get(zillow_link)
rent_html = response.text

soup = BeautifulSoup(rent_html, "html.parser")

links_list = []
price_list = []
address_list = []

link_element = soup.select(".StyledPropertyCardDataArea-anchor")
for tag in link_element:
    link = tag.get("href")
    links_list.append(link)
    # print(links_list)

price_element = soup.select(".PropertyCardWrapper__StyledPriceLine")
for cost in price_element:
    price = cost.getText()
    price_list.append(price)
    # print(price_list)

price_list2 = [s.replace('+', '') for s in price_list]
price_list3 = [s.replace('1 bd', '') for s in price_list2]
price_list4 = [s.replace('/mo', '') for s in price_list3]
# print(price_list4)

address_element = soup.select(selector="address")
for addr in address_element:
    address = addr.getText()
    address_list.append(address)
    # print(address_list)
address_list2 = [item.strip().replace('\n', '') for item in address_list]
# print(address_list2)
# ======================================================================================SELENIUM
chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach", True)
driver = webdriver.Chrome(options=chrom_option)
driver.get(google_form)

for i in range(3):
    i += 1
    driver.find_element(By.XPATH, value="//input[@type='text']").send_keys(address_list2[i])
    driver.find_element(By.XPATH, value="//input[@type='text']").send_keys(Keys.TAB)
    driver.switch_to.active_element.send_keys(price_list4[i])
    driver.switch_to.active_element.send_keys(Keys.TAB)
    driver.switch_to.active_element.send_keys(links_list[i])

    submit = driver.find_element(By.XPATH, value='//*[@id="mG61Hd"]/div[2]/div/div[3]/div[1]/div[1]/div/span/span')
    submit.click()

    next_q = driver.find_element(By.XPATH, value='/html/body/div[1]/div[2]/div[1]/div/div[4]/a')
    next_q.click()
driver.quit()



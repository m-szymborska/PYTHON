from selenium import webdriver
from selenium.webdriver.common.by import By
#Keep open
chrom_option = webdriver.ChromeOptions()
chrom_option.add_experimental_option("detach", True)


driver = webdriver.Chrome(options=chrom_option)
driver.get("https://www.python.org")

# price_dollar = driver.find_element(By.CLASS_NAME, value="a-price-whole")
# price_cents = driver.find_element(By.CLASS_NAME, value="a-price-fraction")
#
# print(f"{price_dollar.text},{price_cents.text}")

# search_bar= driver.find_element(By.NAME, value="q")
# print(search_bar.tag_name)
# print(search_bar.get_attribute("placeholder"))
# button = driver.find_element(By.ID, value="submit")
# print(button.size)
# documentation = driver.find_element(By.CSS_SELECTOR, value=".documentation-widget a")
# print(documentation.text)

# driver.find_element(By.XPATH, value="'link xpath pobrany ze strony/prawy przycisk myszki'")
#xpath ścieżka pozwalaąca dotrzec do każdej części dokumentu XML

# cwiczenie 1===================================================================
list_ul = driver.find_element(By.XPATH, '//*[@id="content"]/div/section/div[2]/div[2]/div/ul')
lists_entries = list_ul.find_elements(By.TAG_NAME, "li")

events_dict = {
    n: {"name": lists_entries[n - 1].find_element(By.TAG_NAME, "time").text,
        "time": lists_entries[n - 1].find_element(By.TAG_NAME, "a").text
        }
    for n in range(1, len(lists_entries) + 1)
}

print(events_dict)
# =====================================================================================


driver.quit()














#driver.close() #zamyka aktualna stronę

driver.quit() #zamyka całą przeglądarke





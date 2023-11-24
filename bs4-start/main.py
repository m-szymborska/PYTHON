from bs4 import BeautifulSoup
#
# with open("website.html") as file:
#     contents = file.read()
# soup = BeautifulSoup(contents, "html.parser")
# # print(soup.prettify())
# # print(soup.title)
# #daje pierwsze
# # print(soup.li)
#
# anchtag = soup.find_all(name="a")
# print(anchtag)
#
# for tag in anchtag:
#     print(tag.get("href"))
#
# comp_url = soup.select_one(selector="p a")
# print(comp_url)

from bs4 import BeautifulSoup
import requests

response = requests.get("https://news.ycombinator.com/news")
yc_web = response.text

soup = BeautifulSoup(yc_web, "html.parser")
article_tag = soup.find(name="a", class_="titleline")
article_text = article_tag.getText()
print(article_text)





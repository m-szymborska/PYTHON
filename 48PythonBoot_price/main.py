import requests
from bs4 import BeautifulSoup
from datetime import datetime
import smtplib
import lxml

URL = "https://www.amazon.com/LEGO-Countdown-Collectible-Minifigures-Spider-Man/dp/B0BXQ4ZNPR/ref=sxin_14_hcs-la-na-tqprod?content-id=amzn1.sym.c39e9304-b82e-4187-9775-3c2b3f55540c:amzn1.sym.c39e9304-b82e-4187-9775-3c2b3f55540c&crid=W3BTMC8LN04R&cv_ct_cx=lego+calendar&keywords=lego+calendar&pd_rd_i=B0BXQ4ZNPR&pd_rd_r=1a9f8d8d-e015-487e-ab38-e020f31b4ff5&pd_rd_w=k0A5Z&pd_rd_wg=m9zsz&pf_rd_p=c39e9304-b82e-4187-9775-3c2b3f55540c&pf_rd_r=KYB4WAF4S5TG6699G29J&qid=1698856543&sbo=RZvfv//HxDF+O5021pAnSA==&sprefix=lego+calendar,aps,193&sr=1-3-2a86f2ef-fd22-4701-9988-69c7c933cba5&language=en_US&currency=USD"

headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/118.0.0.0 Safari/537.36",
    "Accept-Language":"en,pl-PL;q=0.9,pl;q=0.8,en-US;q=0.7"
}

response = requests.get(URL, headers=headers)
website_html = response.text

# print(website_html)


soup = BeautifulSoup(website_html, "lxml")

thing_price = soup.find(class_="a-offscreen").get_text()

price_2 = thing_price.split("$")[1]
price_good = float(price_2)
print(price_good)


my_email = "magazynmgmonixpsc@gmail.com"
password = "jdgqdqlpwunfzfon"
my2_mail = "monikagalanciak@gmail.com"

if price_good < 50:
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        contents = f"Your product is {price_good}"
        connection.sendmail(
            from_addr=my_email,
            to_addrs= my2_mail,
            msg=f"Subject:Price alert\n\n{contents}")


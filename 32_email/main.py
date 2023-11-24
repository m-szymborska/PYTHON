import smtplib
import random
import datetime as dt


my_email = "magazynmgmonixpsc@gmail.com"
password = "jdgqdqlpwunfzfon"

now = dt.datetime.now()
day = now.weekday()

if day == 3:
    with open("quotes.txt") as data:
        qu = data.readlines()
        text = random.choice(qu)
    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=my_email, password=password)
        connection.sendmail(
            from_addr=my_email,
            to_addrs="secret_girl@tlen.pl",
            msg=f"Subject:Monday motivation\n\n{text}"
    )

















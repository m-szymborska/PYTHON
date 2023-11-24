import requests
from datetime import datetime
import smtplib
MY_LAT = 54.075909
MY_LONG = 23.840332



response = requests.get(url="http://api.open-notify.org/iss-now.json")
response.raise_for_status()

data = response.json()
longitude = float(data["iss_position"]["longitude"])
latitude = float(data["iss_position"]["latitude"])

iss_position = (longitude, latitude)


parameters = {
    "lat": MY_LAT,
    "lng": MY_LONG,
    "formatted": 0,
}

response = requests.get(url="https://api.sunrise-sunset.org/json", params=parameters)
response.raise_for_status()
data = response.json()
sunrise = int(data["results"]["sunrise"].split("T")[1].split(":")[0])
sunset = int(data["results"]["sunset"].split("T")[1].split(":")[0])

time_now = datetime.now()

if MY_LONG-5 <= longitude <= MY_LONG+5 and MY_LAT-5 <= latitude <= MY_LAT+5:
    if time_now >= sunset and time_now < sunrise:
        my_email = "magazynmgmonixpsc@gmail.com"
        password = "jdgqdqlpwunfzfon"
        with smtplib.SMTP("smtp.gmail.com") as connection:
            connection.starttls()
            connection.login(user=my_email, password=password)
            connection.sendmail(
                from_addr=my_email,
                to_addrs="secret_girl@tlen.pl",
                msg="Subject:ISS\n\nISS is above you"

            )
    else:
        print("Its ISS above you but is too light to see")
else:
    print("Not now")



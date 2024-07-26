import smtplib
import datetime as dt
import random

MY_EMAIL = "asdasd123@gmail.com"
PASSWORD = "asdasd123"

now = dt.datetime.now()
weekday = now.weekday()

if weekday == 1:
    with open("quotes.txt") as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)

    with smtplib.SMTP("smtp.gmail.com") as connection:
        connection.starttls()
        connection.login(user=MY_EMAIL, password=PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs="dsadsa321@gmail.com",
            msg=f"Subject: Hello World {quote}"
        )



import smtplib
import datetime as dt
import random

MY_EMAIL = input("Email:")
MY_PASSWORD = input("password:")

now = dt.datetime.now()
weekday = now.weekday()
if weekday == 0:
    with open("/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/quote.txt") \
            as quote_file:
        all_quotes = quote_file.readlines()
        quote = random.choice(all_quotes)
    print(quote)
    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=MY_EMAIL,
            msg=f"Subject:Monday Motivation\n\n{quote}"
        )

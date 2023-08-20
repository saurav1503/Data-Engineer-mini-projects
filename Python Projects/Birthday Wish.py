from datetime import datetime
import pandas
import random
import smtplib

MY_EMAIL = input("Email: ")
MY_PASSWORD = input("Password: ")

today = datetime.now()
today_tuple = (today.month, today.day)

data = pandas.read_csv("/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/birthdays.csv")
birthdays_dict = {(data_row["month"], data_row["day"]): data_row for (index, data_row) in data.iterrows()}
if today_tuple in birthdays_dict:
    birthday_person = birthdays_dict[today_tuple]
    file_path = f"/Users/softy/DataEngineer/Data-Engineer-mini-projects/Data Sets/letter_templates/" \
                f"letter_{random.randint(1,3)}.txt"
    with open(file_path) as letter_file:
        contents = letter_file.read()
        contents = contents.replace("[NAME]", birthday_person["name"])

    with smtplib.SMTP("smtp.gmail.com", port=587) as connection:
        connection.starttls()
        connection.login(MY_EMAIL, MY_PASSWORD)
        connection.sendmail(
            from_addr=MY_EMAIL,
            to_addrs=birthday_person["email"],
            msg=f"Subject:Happy Birthday!\n\n{contents}"
        )

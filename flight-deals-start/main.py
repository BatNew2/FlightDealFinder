from data_manager import DataManager
from flight_search import FlightSearch
from sign_up import Start
import smtplib
import requests

print("Link for inputting flight destination: https://docs.google.com/spreadsheets/d/1ZtR7meYBk8NMsz8NrMzzUoNKYLKf9QH3aXJfjoDJD8g/edit#gid=1501973841")
x = False
sign_up = Start()
data_manager = DataManager()
print(data_manager.data)
flight_search = FlightSearch(data_manager.data)
for data in flight_search.prices:
    for dt in data_manager.data:
        if data[0] == dt[1]:
            if data[1] < dt[2]:
                with smtplib.SMTP("smtp.gmail.com") as connection:
                    connection.starttls()
                    connection.login(user="9751.johannes@smp.kanisius.edu", password="cnamsmabmfgrtrae")
                    for user in sign_up.users["users"]:
                        line = f"""Subject:Low price alert!\n\nHey {user["firstName"]} {user["lastName"]}!\nIts only €{data[1]} to fly from {dt[0]} to {dt[1]}-{dt[3]}, on {data[3].replace("T", " ")}. Book at {data[2]}
"""
                        try:
                            connection.sendmail(
                                from_addr="9751.johannes@smp.kanisius.edu",
                                to_addrs=user["email"],
                                msg=line.encode()
                            )
                        except smtplib.SMTPRecipientsRefused:
                            response = requests.delete(f"https://api.sheety.co/b3d5e792cbcb8a687f1186193cb7e04c/flightDeals/users/{user['id']}")
                            response.raise_for_status()
                            print("Invalid email, data not saved")
                        else:
                            x = True
                            if not x:
                                print(f"Welcome to the club {user['firstName']} {user['lastName']}!")

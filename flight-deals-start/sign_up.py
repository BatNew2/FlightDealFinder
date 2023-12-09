import requests


class Start:
    def __init__(self):
        print("Welcome to the flight club")
        self.first_name = input("What is your first name? ")
        self.last_name = input("What is your last name? ")
        stop = False
        while not stop:
            self.email = input("What is your email? ")
            self.email2 = input("Please rewrite that email ")
            if self.email == self.email2:
                stop = True
        print("Please wait")
        self.write_data()
        self.users = []
        self.get_users()

    def write_data(self):
        params = {
            "user": {
                "firstName": self.first_name,
                "lastName": self.last_name,
                "email": self.email
            }
        }
        response = requests.post("https://api.sheety.co/b3d5e792cbcb8a687f1186193cb7e04c/flightDeals/users", json=params)
        response.raise_for_status()

    def get_users(self):
        self.users = requests.get("https://api.sheety.co/b3d5e792cbcb8a687f1186193cb7e04c/flightDeals/users")
        self.users.raise_for_status()
        self.users = self.users.json()

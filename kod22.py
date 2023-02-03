class Trip:

    def __init__(self, destionation="", price=0):
        self.destination = destionation
        self.price = price

    def message(self):
        print(f"I'm going to {self.destination}. It will cost me {self.price} USD")


tanzania_trip = Trip(destionation="Tanzania")
tanzania_trip.message()

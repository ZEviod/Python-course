class Train:
    def __init__(self,name,fare,seats):
        self.name = name
        self.fare = fare
        self.seats = seats

    def getStatus(self):
        print("****************")
        print(f"The name of the train is {self.name}")
        print(f"The total seats in the train is {self.seats}")
        print("****************")

    def fareInfo(self):
        print(f"The price of the ticket is Rs {self.fare}")

    def bookTicket(self):
        if (self.seats>>0):
            print(f"Your ticket is booked! Your seat number is {self.seats}")
            self.seats = self.seats - 1
        else:
            print("Sorry,this train is full! Kindly try in tatkal")

    def cancelTicket(self,seatNo):
        pass

interCity = Train("Intercity Express: 14098",90,300)
interCity.getStatus()
interCity.bookTicket()
interCity.getStatus()
interCity.bookTicket()
interCity.getStatus()
interCity.fareInfo()
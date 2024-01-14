class RailwayForm:
    formType = "RailwayForm"
    def printData(self):
        print(f"Name is {self.name}")
        print(f"Train is {self.train}")

merryApplication = RailwayForm()
merryApplication.name = "Raaju"
merryApplication.train = "Ramdhani Express"
merryApplication.printData()
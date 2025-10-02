class Snow:
    def __init__(self):
        self.year = 1882
        self.month = 1

    def retrieve_snow_data(self):
        print("data")

class Precipitation:
    def __init__(self,year):
        super.__init__(year)

    def get_precipitation_data(self):
        print("precipitation")

class Temperature:
    def __init__(self,year):
        super.__init__(year)

    def get_temp_data(self):
        print("temperature")




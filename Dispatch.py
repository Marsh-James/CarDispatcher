class Dispatch:
    def __init__(self, cars: list, rides: list):
        self.car_list = cars
        self.ride_list = rides
        self.turn_counter = 0

    def filter_rides(self, car_list: list, ride_list: list):
        possible_rides = []

        for ride in ride_list:
            for car in car_list:


    def assign_ride(self):
        for car in self.car_list:
            if not car.in_use:

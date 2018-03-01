class Dispatch:
    def __init__(self, cars: list, rides: list, bonus: int, max_turn: int):
        self.car_list = cars
        self.ride_list = rides
        self.turn_counter = 0
        self.point_counter = 0
        self.bonus = bonus
        self.max_turn = max_turn

    def assign_ride(self, car_list: list, ride_list: list):
        for ride in ride_list:
            for car in car_list:
                if not car.in_use:
                    if (abs(car.pos_x - ride.start_x) + abs(car.pos_y - ride.start_y) + self.turn_counter) <= ride.earliest_start:
                        car.pos_x = ride.final_x
                        car.pos_y = ride.final_y
                        car.in_use = True
                        car.turn_available = self.turn_counter + ride.distance + (ride.earliest_start - self.turn_counter)
                        self.point_counter += ride.distance + self.bonus
                        self.ride_list.remove(ride)
                elif car.in_use and (car.turn_available - self.turn_counter) == 1:
                    car.in_use = False

    def start(self):
        while self.turn_counter < self.max_turn:
            self.assign_ride(self.car_list, self.ride_list)
            self.turn_counter += 1

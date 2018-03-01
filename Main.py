from entities.Car import car
from Dispatch import Dispatch
from entities.Human import human

sim_vars = {'R': 0, 'C': 0, 'F': 0, 'N': 0, 'B': 0, 'T': 0}
rides = []
cars = []


def parse_file(file_name):
    counter = 0
    path = 'data/' + file_name
    file = open(path, 'r')
    for line in file:
        if counter == 0:
            number_set = line.split(' ')
            sim_vars['R'] = int(number_set[0])
            sim_vars['C'] = int(number_set[1])
            sim_vars['F'] = int(number_set[2])
            sim_vars['N'] = int(number_set[3])
            sim_vars['B'] = int(number_set[4])
            sim_vars['T'] = int(number_set[5].strip())
        else:
            ride_data = line.split(' ')
            new_ride = human(
                int(ride_data[0]),
                int(ride_data[1]),
                int(ride_data[2]),
                int(ride_data[3]),
                int(ride_data[4]),
                int(ride_data[5].strip())
            )
            rides.append(new_ride)
        counter += 1


def output_data(file_name):
    path = 'data/' + 'output_' + file_name
    file = open(path, 'w+')
    for car in cars:
        file.write(str(car.ride_count) + " " + car.ride_history + "\n")


parse_file('d_metropolis.in')

for x in range(sim_vars['F']):
    cars.append(car())

my_dispatch = Dispatch(cars, rides, sim_vars['B'], sim_vars['T'])
my_dispatch.start()
output_data('d_metropolis.in')

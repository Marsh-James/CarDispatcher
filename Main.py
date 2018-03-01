from entities.Car import car
from entities.Human import human
sim_vars = {'R':0, 'C': 0, 'F':0, 'N':0, 'B':0, 'T':0}
rides = []
cars = []

def parse_file(file_name):
    counter = 0
    path = 'data/' + file_name
    file = open(path, 'r')
    for line in file:
        if counter == 0:
            number_set = line.split(' ')
            sim_vars['R'] = number_set[0]
            sim_vars['C'] = number_set[1]
            sim_vars['F'] = number_set[2]
            sim_vars['N'] = number_set[3]
            sim_vars['B'] = number_set[4]
            sim_vars['T'] = number_set[5].strip()
        else:
            ride_data = line.split(' ')
            new_ride = human(ride_data[0], ride_data[1], ride_data[2], ride_data[3], ride_data[4], ride_data[5].strip())
            rides.append(new_ride)
        counter += 1


parse_file('a_example')

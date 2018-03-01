sim_vars = {'R':0, 'C': 0, 'F':0, 'N':0, 'B':0, 'T':0}
rides = []
cars = []
def main():
    parse_file('a_example.in')

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
            x = 2
        counter += 1

main()
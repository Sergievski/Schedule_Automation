
def read_file ():
    #Use csv read from library
    all_possible_shifts = {} 
    with open ("possible_shifts.csv") as file :
        file.readline()
        for line in file:
                line = line.split(",")[:-1]
                all_possible_shifts[line[0]] = line[1:100]
        return all_possible_shifts










def read_file ():
    #Use csv read from library
    all_possible_shifts = {} 
    with open ("possible_shifts.csv") as file :
        file.readline()
        for line in file:
                line = line.split(",")[:-1]
                all_possible_shifts[line[0]] = line[1:100] # if you want all you can just do line[1:]
                # also - maybe i would think to make the shift into a class
                # this class can have - day, time, yes/no/prefer

        return all_possible_shifts









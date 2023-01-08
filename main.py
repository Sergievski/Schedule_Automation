from data import Results, Schedule
from main_builder import main_schedule_builder
from itertools import permutations 

### The main_schedule_builder creates only one schedule , and if the result is feasible , prints only one result (probably not the best),
### therefore , i used permutations to get more feasible solutions and sort they by their value -  "points" . 

def main ():
    
    for i in permutations([0, 1, 2, 3]) :
        for j in permutations([0, 1, 2, 3]) :
            main_schedule_builder(i, j)  
            
            
main()

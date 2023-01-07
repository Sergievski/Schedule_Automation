Welcome to the Schedule Automation project! 
This program allows you to input a CSV file containing the scheduling preferences of 4 workers,
and generates a full week schedule based on those preferences.
Simply input your preferences in the specified format,
and the program will handle the rest. 

The program first checks that all shifts are covered.
It then prioritizes the scheduling of "problematic" shifts that are only covered by a single worker.
The program then assigns the remaining shifts,
taking into account the constraint that workers cannot work two shifts in a row. 
If a feasible schedule can be generated, it is displayed.
If not, the program will output a message indicating that there is no feasible solution and to try covering more shift options.



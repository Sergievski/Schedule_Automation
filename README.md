Welcome to my Schedule Automation and Optimization project! 
This program allows you to input a CSV file containing the scheduling preferences ("YES","NO","PREFER") of 4 workers,
for 21 shifts (7 days , 3 shifts every day- Morning, Afternoon, Night) 
and generates a full week schedule based on those preferences.
Simply input your preferences in the specified format,
and the program will handle the rest. 

The program first checks that all shifts are covered (at least one worker marked it as not "NO" preference).
It then prioritizes the scheduling of "problematic" shifts that are only covered by a single worker.
The program then assigns the remaining shifts,
taking into account the constraint that workers cannot work two shifts in a row. 
If a feasible schedule can be generated, it is displayed.
If not, the program will output a message indicating that there is no feasible solution and to try covering more shift options.

To optimaized the solution , i used permutations of indexes , on which the main algorithm is running , 
to get 24*24 = 576 diffrent schedules/solution , and after feasibility check , every feasible schedule printed with it's "points" 
measurment. The highest point schedule is -the higher amount of preferable shifts assigned. 



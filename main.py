from data import Employee, Schedule, Shift, Team 
from file import read_file
from optimization import search_for_problematic_shifts, covering_problematic_shifts
from optimization import test_if_all_shifts_are_covered, main_algorithm, solution_presentation


def main():
    all_possible_shifts = read_file()   # creation of dictionary - name:[posible shifts] , from a csv file 

    workers_names = [] #creation of list of names 
    for name in all_possible_shifts:
        workers_names.append(name)

    # creation of Emploee objects 
    employee1 = Employee(workers_names[0], 5)
    employee2 = Employee(workers_names[1], 5)
    employee3 = Employee(workers_names[2], 5)
    employee4 = Employee(workers_names[3], 6)

    # creation of Team object 
    team = Team()
    team.add_worker(employee1)
    team.add_worker(employee2)
    team.add_worker(employee3)
    team.add_worker(employee4)
    

    #addition of possible shifts to each worker 
    for worker in team.workers:
        worker.possible_shifts = all_possible_shifts[worker.name]

    
    # creation of Schedule object
    days = ["Sunday","Monday","Tuesday","Wednesday","Thursday","Friday","Saturday"]
    day_times = ["morning","afternoon","night"]
    schedule = Schedule(days,day_times)

    # testing if all shifts are covered (at least one worker can take each shift)
    test_if_all_shifts_are_covered (team, schedule) 

    # searching for "problematic" shifts (covered by one worker only )
    barely_covered_shifts = search_for_problematic_shifts(team)

    # covering "problematic" shifts (only one worker can take + the last shift - index 20)
    team, schedule = covering_problematic_shifts(barely_covered_shifts,team,schedule)

    # covering the "regular" shifts by workers priority 
    team , schedule =  main_algorithm (team, schedule )

    # printing personal schedule for each worker and a general week schedule 
    team, schedule = solution_presentation (team, schedule) 
    

    schedule.get_extra_paid_shifts()


main()


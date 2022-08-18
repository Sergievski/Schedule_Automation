
from data import Schedule, Team


def test_if_all_shifts_are_covered (team : Team, schedule:Schedule) : #checking that all the shifts are covered (by one worker at least) . 
    print()
    print ("Checking if all she shifts are covered .......")
    print()
    covered_count = 0 
    for i in range (21):
        count4 = 0
        for worker in team.workers:
            if not (worker.possible_shifts[i] == "NO"):
                covered_count += 1
                break
            else : 
                count4 += 1 
                if count4 == 4 :
                    print (f"Shift number : {i}, is not covered !!! ")
                    print (f"Please cover {schedule.shifts[i].name} ")

    if covered_count == 21 :
        print ( "All she shifts are covered  !!!  ")
        print()
    return


def search_for_problematic_shifts(team):  # searching for "problematic" shifts (covered by one worker only )
    barely_covered_count = 0
    barely_covered_shifts = []
    print("Checking for 'problematic' shifts that covered by only one worker .......")
    for i in range (20): # except the last shift, which covered anyway (not matter if "problematic" or not)
        no_list = []
        for worker in team.workers:
            if worker.possible_shifts[i] == "NO":
                no_list.append(i)
        if len(no_list) == 3:
            barely_covered_count += 1
            barely_covered_shifts.append(i)       
    print()
    print("The number of barely covered shifts is : " , barely_covered_count)
    print()
    print("The index list of barely covered shifts is : " , barely_covered_shifts)
    print()
    return barely_covered_shifts 


def covering_problematic_shifts(barely_covered_shifts,team:Team,schedule:Schedule):  # covering of "problematic" shifts

    # covering problematic shifts
    for i in barely_covered_shifts :
        for worker in team.workers :
            if worker.possible_shifts[i] != "NO" :
                schedule.shifts[i].worker = worker.name 
                worker.schedule.append(schedule.shifts[i].name)
                worker.shifts_num -= 1

    # covering the last (20) shift :
    order = [3,0,2,1] 
    for i in order :
        if team.workers[i].possible_shifts[20] != "NO":
            schedule.shifts[20].worker = team.workers[i].name
            team.workers[i].schedule.append(schedule.shifts[20].name)
            team.workers[i].shifts_num -= 1
            break

    return team,schedule


def main_algorithm (team, schedule ) : # algorithm that runs on every shift "i" and maches it a worker  
    
    index1 = [0,3,2,1]
    index2 = [1,2,3,0]
    for i in range (20):  # except the last shift, that already covered 
        for j in index1 :
            if team.workers[j].possible_shifts[i] == "PREFER" and team.workers[j].shifts_num > 0 and schedule.shifts[i-1].worker != team.workers[j].name and schedule.shifts[i].worker == None and schedule.shifts[i+1].worker != team.workers[j].name :
                schedule.shifts[i].worker = team.workers[j].name
                team.workers[j].shifts_num -= 1
                team.workers[j].schedule.append(schedule.shifts[i].name)
                break
        for k in index2 :
            if team.workers[k].possible_shifts[i] == "YES" and team.workers[k].shifts_num > 0 and schedule.shifts[i-1].worker != team.workers[k].name and schedule.shifts[i].worker == None and schedule.shifts[i+1].worker != team.workers[k].name :
                schedule.shifts[i].worker = team.workers[k].name
                team.workers[k].shifts_num -= 1
                team.workers[k].schedule.append(schedule.shifts[i].name)
                break
    return team , schedule


def solution_presentation (team:Team, schedule:Schedule) :
    
    my_count = 0
    for shift in schedule.shifts:
        if shift.worker == None:
            print ("No feasible solution - Cover more options")
            break
        else :
            my_count += 1
            
    if my_count == 21 :        
            
        print("Personal shedules :")
        print()
        for worker in team.workers :
            team.get_personal_schedule(worker.name)
            print()
           
        print("General week schedule : ")
        print()
        schedule.print()    
        print()   
        print()
                
            
    return team, schedule







class Employee :

    def __init__(self, name, shifts_num):
        self.name = name
        self.shifts_num = shifts_num
        self.possible_shifts = None
        self.schedule = []

    def __str__(self):
        return f"{self.shifts_num},{self.name},{self.schedule}"
    
    
class Team:

    def __init__(self) :
        self.workers = []

    def add_worker(self,worker:Employee):
        self.workers.append(worker)
            
    def get_personal_schedule (self, name):
        for worker in self.workers:
            if worker.name == name:
                print(worker.name, worker.schedule)
                
                   

class Shift :

    def __init__(self, name):
        # instead of name - 2 parameters: day, time
        self.name = name
        self.worker = None
    
    def __str__(self):
        return f"{self.name},{self.worker}"

    
class Schedule :

    def __init__(self,days,day_times) :
    
        shift_names = []
        self.shifts = []
        for day in days:
            for time_of_day in day_times:
                shift_names.append(day+"_"+time_of_day)
                # shift_name - why not add time_of_day to shift object?
        for i in shift_names :
            shift = Shift (i)
            self.shifts.append(shift)

    
    def print (self):
        
        for shift in self.shifts:
            print (shift.name,"", shift.worker)



    def get_extra_paid_shifts (self):
        print("Extra paid shifts :")
        print()
        for shift in self.shifts[15:22]:
            print (shift.name , shift.worker)
            
    
            


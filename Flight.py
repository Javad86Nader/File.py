class Flight():
    def __init__(self,x):
        self.capasity = x
        self.passengers = []
    def add_paasenger(self,name):
        if self.capasity > 0:
            return True
        else :
            return False
people = []
number = 1
E = True
L = 0
while E:
    if L == 0:
        Aircraft_capasity = int(input("Aircraft capasity : "))
        f = Flight(Aircraft_capasity)
        L += 1
    else:        
        traveler = input(f"traveler_{number} : ")
        if traveler == "Exit":
            for person in people:
                if f.add_paasenger(person):
                    f.passengers.append(person)
                    f.capasity -= 1
                    print(f"{person} added succesfully")
                else:
                    print(f"{person} not available seat")
                E = False
        else:
            people.append(traveler)
            number += 1
L = 0 
print(f"{f.capasity} seat Available")
print(f"list of passengers :  {f.passengers}")
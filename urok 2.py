import random

class Student:
    def __init__(self, name):
        self.name = name
        self.gladness = 50
        self.progress = 0
        self.alive = True

    def to_study(self):
        print("time to study")
        self.progress += 0.15
        self.gladness -= 3
    def to_sleep(self):
        print("will sleep")
        self.gladness += 3
    def to_chill(self):
        print("rest time")
        self.gladness += 5
        self.progress -= 0.2
    def is_alive(self):
        if self.progress < -0.5:
            print("cast out...")
            self.alive = False
        elif self.gladness <= 0:
            print("depression...")
            self.alive = False
        elif self.progress > 5:
            print("passed externally")
            self.alive = False
    def end_on_day(self):
        print(f'Progress = {self.progress}')
        print(f'Gladness = {self.gladness}')
    def live(self, day):
        day = "Day" + str(day) + " of " + self.name + " life "
        print(f'= {day:=^50}')
        live_cube = random.randint(1, 3)
        if live_cube == 1:
            self.to_study()
        elif live_cube == 2:
            self.to_sleep()
        elif live_cube == 3:
            self.to_chill()

nick = Student(name = "Nick")
for day in range(365):
    if nick.alive == False:
        break
    nick.live(day)







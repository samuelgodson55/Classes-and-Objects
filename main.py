class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, track, score):
        self.name = str(name)
        self.age = int(age)
        self.track = track
        self.score = float(score)

    def change_name(self, name):
        self.name = str(name)

    def change_age(self, age):
        self.age = int(age)

    def add_track(self, strng):
        self.track.append(strng)
        
    def get_score(self):
        return self.score

#initialization
Bob = Student(name='Bob', age=26, track=['FE','BE'], score=20.9)

# Expected methods, used in resting the codes
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

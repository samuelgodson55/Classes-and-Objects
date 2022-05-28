class Student:
    # [assignment] Skeleton class. Add your code here
    
    def __init__(self, name, age, track, score):
        self.name = name
        self.age = age
        self.track = track
        self.score = score

    def change_name(self, name):
        self.name = name

    def change_age(self, age):
        self.age = int(age)

    def add_track(self, strng):
        self.track.append(strng)
        
    def get_score(self):
        return self.score

Bob = Student('Bob', 26, ['FE','BE'],20.9)

# Expected methods
#Bob.change_name("Peter")
#Bob.change_age(34)
#Bob.add_track("UI/UX")
#Bob.get_score()

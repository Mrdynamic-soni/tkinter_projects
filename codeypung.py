class nikita:
    grade = 10
    def __init__(self, name, age, adds, sec):
        self.name = name
        self.age = age
        self.adds = adds
        self.sec = sec

    def display(self):
        print("hi my name is " + self.name)
        print(self.age) 
        print(self.adds)
        print(self.grade)
        print(self.sec)

football = nikita("nikitaa",14,"uk","a")
football.display()

basketball = nikita("saurabh",21,"india","3rd")
basketball.display()
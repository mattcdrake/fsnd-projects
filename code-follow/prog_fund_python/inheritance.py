class Parent():
    def __init__(self, last_name, eye_color):
        print("Parent constructor")
        self.last_name = last_name
        self.eye_color = eye_color

class Child(Parent):
    def __init__(self, last_name, eye_color, toys):
        print("Child constructor")
        Parent.__init__(last_name, eye_color)
        self.toys = toys

billy_cyrus = Parent("Cyrus", "Blue")
miley_cyrus = Child("Cyrus", "Blue", 3)


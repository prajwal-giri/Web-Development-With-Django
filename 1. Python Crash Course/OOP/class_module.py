class HomoSapiens:    # creating a class
    name = "Hari"
    sex = "Male"  # attributes
    age = 30

  # creating method to print name when called
    def display_username(self):
        print(f"Your name is {self.name}")

    # creating method to print age when called
    def display_age(self):
        print(f"Your age is {self.age}")

    # creating method to print gender if called.
    def display_sex(self):
        print(f"Your gender is {self.sex}")


def add(a, b):
    print(a + b)


def sub(a, b):
    print(a - b)


def mult(a, b):
    print(a * b)

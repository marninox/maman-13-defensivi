import random

# Base class
class User:
    def __init__(self, name):
        self.name = name
        self.profession = "user"

class Engineer(User):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "engineer"

class Technician(User):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "technician"

class Politician(User):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "politician"

# Subtypes of engineers (as requested in the MAMAN)
class ElectricalEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "electrical engineer"

class ComputerEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "computer engineer"

class MechanicalEngineer(Engineer):
    def __init__(self, name):
        super().__init__(name)
        self.profession = "mechanical engineer"

# Method template for dynamically created classes
def method_template(self):
    print(f"{self.__class__.__name__}: method called!")

# Store known classes
class_dict = {
    'User': User,
    'Engineer': Engineer,
    'Technician': Technician,
    'Politician': Politician,
    'ElectricalEngineer': ElectricalEngineer,
    'ComputerEngineer': ComputerEngineer,
    'MechanicalEngineer': MechanicalEngineer
}

# Input from user
new_class_name = input("Please enter the name of new class: ").strip()
base_class_name = input("Please enter name of base class (blank if none): ").strip()
new_method_name = input(f"Please enter name of new method for class {new_class_name}: ").strip()
new_attr_name = input(f"Please enter name of new attribute for class {new_class_name}: ").strip()

# Validate base class
if base_class_name:
    if base_class_name not in class_dict:
        print(f"Base class {base_class_name} does not exist.")
        exit(1)
    base_class = class_dict[base_class_name]
else:
    base_class = object

# Create new class dynamically - as requested
# method_template that prints once and attr with random number
new_class = type(
    new_class_name,
    (base_class,),
    {
        new_method_name: method_template,
        new_attr_name: random.randint(1, 100)
    }
)

# Store new class
class_dict[new_class_name] = new_class

# Output info
print(f"Class {new_class_name} created with base class: {base_class.__name__}")
print(f"Class __name__ is: {new_class.__name__}")
print(f"Class __dict__ is: {new_class.__dict__}")

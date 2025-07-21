import ast
import importlib.util
import inspect
import types

# get filename and code from user
filename = input("Enter python file name: ").strip()
code_to_inject = input("Enter a python code: ").strip()

# load the module dynamically
spec = importlib.util.spec_from_file_location("target_module", filename)
module = importlib.util.module_from_spec(spec)
spec.loader.exec_module(module)

# find the first class defined in the file
classes = [obj for name, obj in vars(module).items() if isinstance(obj, type)]
if not classes:
    print("No classes found in the module.")
    exit(1)

target_class = classes[0]

# list of special method names (everything relevant I thought of)
special_methods = ['__init__', '__str__', '__repr__', '__eq__', '__lt__', '__len__']

# inject code into all relevant methods
for method_name in special_methods:
    if hasattr(target_class, method_name):
        original_method = getattr(target_class, method_name)

        def make_wrapper(func):
            def wrapper(self, *args, **kwargs):
                exec(code_to_inject, globals(), locals())
                return func(self, *args, **kwargs)
            return wrapper

        wrapped = make_wrapper(original_method)
        setattr(target_class, method_name, wrapped)

# testing the result with the examples from question 2 of the MAMAN
try:
    obj1 = target_class("red", 4)
    print(obj1)
    obj2 = target_class("blue", 50)
    print(obj2)
except Exception as e:
    print(f"Error testing class methods: {e}")

"""
answer to section 3 in question 3 of the MAMAN:
To find all methods in a class, including ones the programmer added, 
we can use inspect.getmembers() with inspect.isfunction or inspect.ismethod
The inspect module helps us look inside Python objects to check things like
functions, methods, and properties
"""


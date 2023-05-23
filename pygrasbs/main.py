import json
import fmodule as fm;
import platform
import datetime
import ensurepip
import camelcase

print(fm.x, fm.z, fm.y)
class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age
    def __str__(self) -> str:
        return f"{self.name}({self.age})"
    def greeting(classargs):
        print("Hello, Mr. ", classargs.name)

    

p1 = Person('ali', 32)
p1.name = 'Abdulrahman'
p1.greeting()

# print(fm.person1["Age"])

# print(platform.system())
# print(dir(platform))

# d = datetime.datetime.now()
# print(d.date())
# print(d.ctime())
# print(d.timetz())
# print(d.strftime("%C"))

x = {
  "name": "John",
  "age": 30,
  "married": True,
  "divorced": False,
  "children": ("Ann","Billy"),
  "pets": None,
  "cars": [
    {"model": "BMW 230", "mpg": 27.5},
    {"model": "Ford Edge", "mpg": 24.1}
  ]
}
# print(json.dumps(x, indent=4, separators=(". ", " = "), sort_keys=True))

c = camelcase.CamelCase()
text = "hello, world!"
print(c.hump(text))
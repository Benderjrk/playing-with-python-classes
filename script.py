print(type(5))

my_dict = {}
print(type(my_dict))
my_list = []
print(type(my_list))

class ClassCreation:
  pass

class Facade:
  pass

facade_1 = Facade()
facade_1_type = type(facade_1)
print(facade_1_type)

class Grade:
  minimum_passing = 65

class Rules:
  pass
  def washing_brushes(self):
    return "Point bristles towards the basin while washing your brushes."

class Circle:
  pi = 3.14
  def area(self, radius):
    area = self.pi * radius ** 2
    return area

circle = Circle()
pizza_area = circle.area(12/2)
teaching_table_area = circle.area(36/2)
round_room_area = circle.area(11460/2)

class Circle:
  pi = 3.14
  # Add constructor here:
  def __init__(self, diameter):
    string = "New circle with diameter: {diameter}".format(diameter=diameter)
    print(string)

teaching_table = Circle(36)

class Store:
  pass

alternative_rocks = Store()
isabelles_ices = Store()
alternative_rocks.store_name = "Alternative Rocks"
isabelles_ices.store_name = "Isabelle's Ices"

how_many_s = [{'s': False}, "sassafrass", 18, ["a", "c", "s", "d", "s"]]

for data in how_many_s:
  if hasattr(data, "count") == True:
    s_count = data.count('s')
    print(s_count)

class Circle:
  pi = 3.14
  def __init__(self, diameter):
    print("Creating circle with diameter {d}".format(d=diameter))
    # Add assignment for self.radius here:
    self.radius = diameter / 2

  def circumference(self):
    return 2 * self.pi * self.radius 

medium_pizza = Circle(12)

teaching_table = Circle(36)

round_room = Circle(11460)

print(medium_pizza.circumference())
print(teaching_table.circumference())
print(round_room.circumference())

# print(dir(5))

def this_function_is_an_object():
  pass

print(dir(this_function_is_an_object))

class Circle:
  pi = 3.14
  
  def __init__(self, diameter):
    self.radius = diameter / 2
  def __repr__(self):
    return "Circle with radius {radius}".format(radius=self.radius)
  def area(self):
    return self.pi * self.radius ** 2
  
  def circumference(self):
    return self.pi * 2 * self.radius
  
  
medium_pizza = Circle(12)
teaching_table = Circle(36)
round_room = Circle(11460)

print(medium_pizza)
print(teaching_table)
print(round_room)

class Student:
  pass
  def __init__(self, name, year):
    self.name = name
    self.year = year
    self.grades = []

  def add_grade(self, grade):
    if type(grade) == Grade:
      self.grades.append(grade)

roger = Student("Roger van der Weyden", 10)
sandro = Student("Sandro Botticelli", 12)
pieter = Student("Pieter Bruegel the Elder", 8)

class Grade:
  minimum_passing = 65
  def __init__(self, score):
    self.score = score

  def is_passing(self):
    is_passing = self.score >= self.minimum_passing
    return is_passing 

print(Grade(100).is_passing())
pieter.add_grade(Grade(70))
print(pieter.grades)

class Bin:
  pass

class RecyclingBin(Bin):
  pass

class Message:
  def __init__(self, sender, recipient, text):
    self.sender = sender
    self.recipient = recipient
    self.text = text

class User:
  def __init__(self, username):
    self.username = username
    
  def edit_message(self, message, new_text):
    if message.sender == self.username:
      message.text = new_text

class Admin(User):
  pass

  def edit_message(self, message, new_text):
    message.text = new_text

class PotatoSalad:
  def __init__(self, potatoes, celery, onions):
    self.potatoes = potatoes
    self.celery = celery
    self.onions = onions

class SpecialPotatoSalad(PotatoSalad):
  def __init__(self, potatoes, celery, onions):
    super().__init__(potatoes, celery, onions)
    self.raisins = 40


class InsurancePolicy:
  def __init__(self, price_of_item):
    self.price_of_insured_item = price_of_item

class VehicleInsurance(InsurancePolicy):
  
  def get_rate(self):
    return .001 * self.price_of_insured_item

class HomeInsurance(InsurancePolicy):
  def get_rate(self):
    return .00005 * self.price_of_insured_item

a_list = [1, 18, 32, 12]
a_dict = {'value': True}
a_string = "Polymorphism is cool!"

print("list", len(a_list)) 

print("dict", len(a_dict)) 

print("string", len(a_string))

class Atom:
  def __init__(self, label):
    self.label = label
  def __add__(self, other):
    return Molecule([self, other])
    
class Molecule:
  def __init__(self, atoms):
    if type(atoms) is list:
	    self.atoms = atoms
    else: 
      return "Needs a list to be added"
      
sodium = Atom("Na")
chlorine = Atom("Cl")

salt = sodium + chlorine

class LawFirm:
  def __init__(self, practice, lawyers):
    self.practice = practice
    self.lawyers = lawyers
  def __len__(self):
    return len(self.lawyers)
  def __contains__(self, lawyer):
    return lawyer in self.lawyers

d_and_p = LawFirm("Injury", ["Donelli", "Paderewski"])


class SortedList(list):
  def __init__(self, lst):
    self.lst = lst
    self.lst.sort()
    
  def append(self, value):
    super().append(value)
    self.sort()
    



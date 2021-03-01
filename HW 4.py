# 1. Create a Vehicle class with max_speed and mileage instance attributes

class Vehicle:
    def __init__(self, max_speed=100, mileage=10000):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_information(self):
        print(f"Max speed {self.max_speed} M/H and Mileage {self.mileage} miles")


vehicle = Vehicle()
vehicle.print_information()


# 2. Create a child class Bus that will inherit all of the variables and methods of the Vehicle class and will have
# seating_capacity own method

class Bus(Vehicle):
    def __init__(self, max_speed=90, mileage=90000, length=10):
        self.length = length
        self.max_speed = max_speed
        self.mileage = mileage
        super(Bus, self).__init__(max_speed, mileage)

    def car_length(self):
        print(f"length car is {self.length} meters")


car = Bus()
car.print_information()
car.car_length()


# 3. Determine which class a given Bus object belongs to (Check type of an object)

print(type(car))
print(issubclass(Bus, Vehicle))

# 4. Determine if School_bus is also an instance of the Vehicle class

print(isinstance(car, Vehicle))

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:
    def __init__(self, get_school_id=171, number_of_students=5000):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

    def print_school(self):
        print(f"The school is {self.get_school_id} number and school has {self.number_of_students} students")


# 6*. Create a new class SchoolBus that will inherit all of the methods from School and Bus and will have its own -
# bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, get_school_id=171, number_of_students=50, max_speed=70, mileage=1000, length=10,
                 bus_school_color='Yellow'):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students
        self.max_speed = max_speed
        self.mileage = mileage
        self.length = length
        self.bus_school_color = bus_school_color
        super(School, self).__init__(get_school_id, number_of_students)
        super(Bus, self).__init__(max_speed, mileage)

    def school_bus_color(self):
        print(f'School Bus color is {self.bus_school_color}')


school_bus = SchoolBus()
school_bus.school_bus_color()


# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances,
# one of Bear and one of Wolf, make a tuple of it and by using for call their action using the same method.

class Bear:
    def make_sound(self):
        print('I want raspberries')


class Wolf:
    def make_sound(self):
        print('I want meat')


bear = Bear()
wolf = Wolf()

Animals = (bear, wolf)

for Animals in Animals:
    Animals.make_sound()


# Magic methods:
# 8. Create class City with name, population instance attributes, return a new instance only when population > 1500,
# otherwise return message: "Your city is too small".

class City:
    def __init__(self, name, population):
        self.name = name
        self.population = population

    def __new__(cls, name, population):
        instance = super(City, cls).__new__(cls)
        if population > 1500:
            return instance
        else:
            print('Your city is too small')

# 9. Override a printable string representation of the City class and return:
# The population of the city {name} is {population}

    def __str__(self):
        print(f'The population of the city {self.name} is {self.population}')

people = City('Kiev', 2884000)
people.__str__()

# 10*. Override magic method __add__() to perform the additional action as 'multiply' (*)
# the value which is greater than 10. And perform this add (+) of two instances.

class New:
    def __init__(self, multiply):
        self.multiply = multiply

    def __add__(self, new_1):
        if self.multiply > 10 or new_1.multiply > 10:
            multiply_1 = self.multiply * new_1.multiply
        else:
            multiply_1 = self.multiply + new_1.multiply
        return New(multiply_1)

    def __str__(self):
        return f'multiply: {self.multiply}'


c1 = New(20)
c2 = New(2)
c3 = c1 + c2
print(c3)

# 11. The __call__ method enables Python programmers to write classes where the instances behave like functions and
# can be called like a function. Create a new class with __call__ method and define this call to return sum.

class Call:
    def __call__(self, *args):
        return sum(args)


result = Call()
print(result(-5, 7, 9, 11, 15))

#12*. Making Your Objects Truthy or Falsey Using __bool__().
#Create class MyOrder with cart and customer instance attributes.
#Override the __bool__magic method considered to be truthy if the length of the cart list is non-zero.

class MyOrder:
    def __init__(self, cart, customer):
        self.cart = cart
        self.customer = customer

    def __bool__(self):
        if len(self.cart) > 0:
            return True
        else:
            return False


order_1 = MyOrder(['a', 'b', 'c'], 'd')
order_2 = MyOrder([], 'a')
print(bool(order_1))
print(bool(order_2))
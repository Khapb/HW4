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


# 4. Determine if School_bus is also an instance of the Vehicle class


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
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def sound(self):
        print(f'Bear say - {self.make_sound}')


bear = Bear('I want raspberries')
bear.sound()


class Wolf:
    def __init__(self, make_sound):
        self.make_sound = make_sound

    def sound(self):
        print(f'Wolf say - {self.make_sound}')


wolf = Wolf('I want meat')
wolf.sound()


class Animals(Bear, Wolf):
    pass


animals = Animals()
animals.sound()

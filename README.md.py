# OOP-Assignment2
Activity 1
# Parent class
class Superhero:
    def __init__(self, name, power, origin):
        self.name = name
        self._power = power   # Encapsulated attribute
        self.origin = origin

    def introduce(self):
        return f"I am {self.name} from {self.origin} and I have {self._power} powers!"

    def use_power(self):
        return f"{self.name} uses their amazing {self._power} power!"

# Child class
class FlyingHero(Superhero):
    def __init__(self, name, origin, flight_speed):
        super().__init__(name, "Flight", origin)
        self.flight_speed = flight_speed

    def use_power(self):
        return f"{self.name} zooms through the sky at {self.flight_speed} km/h!"

# Another child class
class StrengthHero(Superhero):
    def __init__(self, name, origin, lifting_capacity):
        super().__init__(name, "Super Strength", origin)
        self.lifting_capacity = lifting_capacity

    def use_power(self):
        return f"{self.name} lifts {self.lifting_capacity} tons effortlessly!"

# Example usage
hero1 = FlyingHero("Skyblade", "Neo-City", 800)
hero2 = StrengthHero("IronBrawn", "Titan Valley", 200)

print(hero1.introduce())
print(hero1.use_power())
print(hero2.introduce())
print(hero2.use_power())


class Vehicle:
    def move(self):
        raise NotImplementedError("This method should be overridden!")

class Car(Vehicle):
    def move(self):
        return "Driving 🚗"

class Plane(Vehicle):
    def move(self):
        return "Flying ✈️"

class Boat(Vehicle):
    def move(self):
        return "Sailing 🚢"

# Example of polymorphism
vehicles = [Car(), Plane(), Boat()]

for v in vehicles:
    print(v.move())

# class Time:
#     def __init__(self, hour, minute):
#         # Assert invariants
#         assert isinstance(hour, int) and 0 <= hour <= 23, "Hour must be int between 0 and 23."
#         assert isinstance(minute, int) and 0 <= minute <= 59, "Minute must be int between 0 and 59."
#         self.hour = hour
#         self.minute = minute
#
#     def increment(self, hours, minutes):
#         total_minutes = self.hour * 60 + self.minute + hours * 60 + minutes
#         total_minutes %= 1440
#         self.hour = total_minutes // 60
#         self.minute = total_minutes % 60
#
#     def isPM(self):
#         return self.hour >= 12
#
#     def __str__(self):
#         # Format time as HH:MM in 24-hour format
#         return f"{self.hour:02}:{self.minute:02}"
#
#
# # Example usage
# if __name__ == "__main__":
#     t = Time(23, 58)
#     print(t)  # Output: 23:58
#     t.increment(0, 3)
#     print(t)  # Output: 00:01
#     t.increment(11, 0)
#     print(t, t.isPM())  # Output: 11:01 False
#     t.increment(5, 100)
#     print(t, t.isPM())  # Output: 17:41 True


class Animal:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def speak(self):
        return f"{self.name} makes a sound "

    def __str__(self):
        return f"{self.name} is {self.age} years old."


class Dog(Animal):
    def __init__(self, name, age, breed):
        super().__init__(name, age)
        self.breed = breed

    def speak(self):
        return super().speak() + "Woof!"

    def fetch(self, item):
        return f"{self.name} is fetching the {item}."

    def __str__(self):
        return f"{self.name} is a {self.breed} dog, {self.age} years old."


class Cat(Animal):
    def __init__(self, name, age, color):
        super().__init__(name, age)
        self.color = color

    def speak(self):
        return super().speak() + "Meow!"

    def scratch(self):
        return f"{self.name} is scratching the furniture."

    def __str__(self):
        return f"{self.name} is a {self.color} cat, {self.age} years old."



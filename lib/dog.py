#!/usr/bin/env python3

class Dog:
    def __init__(self, name, breed="Mutt"):
        self.name = name
        self.breed = breed
# Creating a Dog instance with specific name and breed
my_dog = Dog("Buddy", "Labrador")

# Creating a Dog instance with only a name (defaults breed to "Mutt")
another_dog = Dog("Max")

print(my_dog.name)  # Output: Buddy
print(my_dog.breed)  # Output: Labrador

print(another_dog.name)  # Output: Max
print(another_dog.breed)  # Output: Mutt

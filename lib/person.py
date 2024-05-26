#!/usr/bin/env python3

class Person:
    def talk(self):
        print("Hello World!")

    def walk(self):
        print("The person is walking.")

# Creating an instance of the Person class
john = Person()

# Calling the talk() instance method on the john object
john.talk()  # Output: Hello World!

# Calling the walk() instance method on the john object
john.walk()  # Output: The person is walking.

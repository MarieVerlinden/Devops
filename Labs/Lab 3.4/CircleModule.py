# Given a radius value, print the circumference of a circle.
# Formula for a circumference is c = pi * 2 * radius
class Circle:
    def __init__(self, radius):
        self.radius = radius
    def circumference(self):
        pi = 3.14
        circumferenceValue = pi * self.radius * 2
        return circumferenceValue
    def printCircumference(self):
        myCircumference = self.circumference()
        print ("Circumference of a circle with a radius of " + str(self.radius) + " is " + str(myCircumference))

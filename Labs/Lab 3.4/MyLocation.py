#define class "Location"
class Location:
    #define init fuction. 
    #First parameter self (current instance of class itself)
    #Then add all the variables the entire class needs.
    def __init__(self, name, country):
        self.name = name
        self.country = country

    def myLocation(self):
        print("Hi, my name is "+ self.name +" and I live in "+ self.country +".")



# #calling method
# loc = Location("Blue", "Belgium")

# #print name 
# print(loc.name)
# #print name of country
# print(loc.country)
# #verify it is a class
# print(type(loc))

#calling new(?) method
loc1 = Location("Blue", "Belgium")
loc1.myLocation()

#calling the method again
loc2 = Location("Jo", "Sweden")
loc3 = Location("Ruby", "USA")
your_loc = Location("Jonathan", "Belgium")

loc2.myLocation()
loc3.myLocation()
your_loc.myLocation()

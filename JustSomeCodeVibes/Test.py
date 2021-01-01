#function for closing the screen
def close():
    input("press enter key to stop")

#function for area of a circle
def area_circle():
    d = int(input("whats the diameter? "))
    r = d/2
    c = 3.141592*(r ** 2)
    print ("the area of a circle with a", d,"cm diameter is", c, "cm².")

#function for area of a triangle
def area_triangle():
    h = int(input("what's the height of the triangle? "))
    b = int(input("what's the width of the triangle? "))
    a = (h*b)/2
    print ("the area of a triangle with a height of", h,"cm and a base of", b,"cm is", a, "cm²")

#function application
def running():
    choice = input("do you want to know the area of a circle or a triangle?")
    if choice == "circle":
        area_circle()
        
   
    elif choice == "triangle":
        area_triangle()
        

    else: 
        print("please choose circle or triangle.")



while input("Do you want to calculate the area? (y/n)") == "y":
    running()
    if input("Do you want to calculate the area? (y/n)") == "n":
        break
close()



  



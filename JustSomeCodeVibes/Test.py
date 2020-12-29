choice = input("do you want to know the area of a circle or a triangle?")
if choice == "circle":
    d = int(input("whats the diameter? "))
    r = d/2
    c = 3.141592*(r ** 2)
    print ("the area of a circle with a", d,"cm diameter is", c, "cm².")
elif choice == "triangle":
    h = int(input("what's the height of the triangle? "))
    b = int(input("what's the width of the triangle? "))
    a = (h*b)/2
    print ("the area of a triangle with a height of", h,"cm and a base of", b,"cm is", a, "cm²")
else: 
    print("please choose circle or triangle.")
  



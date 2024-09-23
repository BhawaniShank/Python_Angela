print("Welcome to the rollercoaster")
height = int(input("What is your height in centimeter?"))    
if  height >= 120:
    print("You can ride the rollercoaster")
    age = int(input("What is your age"))
    if age > 18:
        print("you have to pay 12$")
    elif age>12:
        print("you have to pay 7$")
    else : 
        print("you have to pay 5$")    
else:
    print("you can't ride") 
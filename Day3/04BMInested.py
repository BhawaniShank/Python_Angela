height = float(input("enter your height in meters: "))
weight = float(input("enter your weight in kg: "))

BMI = round(weight/height**2 ,1)

if BMI<18.5:
    print(f"Your BMI is {BMI},You are underweight eat more")
elif BMI<25:
    print(f"Your BMI is {BMI},You are normalweight keep it up")
elif BMI<35:
    print(f"Your BMI is {BMI},You are overweight Do some exercise")
else:
    print(f"Your BMI is {BMI},You are clinically obese  Do some exercise and eat less")    
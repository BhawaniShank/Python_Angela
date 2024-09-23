year = int(input("which year do you want to check"))
# On every year that is evenly divisible by 4
# except every year that is evenly divisible by 100
# unless the year is also evenly divisible by 400

if year%4==0:
        if year %100==0:
              if year%400==0:
                     print("Leap year")
              else:
                     print("Leap Year")      
        else:
               print("Leap Year")
else:
      print("This is not a leap year")
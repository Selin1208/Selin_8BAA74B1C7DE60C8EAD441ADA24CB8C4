# 1.2 Implement a recursive function to calculate the factorial of a given number.

def isleapyear(year):
 if(year % 4 == 0 and year %  100 != 0)or year % 400 ==0:
   return True
 else:
   return False
 
year = int(input("Enter a year:"))
  
if isleapyear(year):
  print('{} is a leap year .'. format(year))
else:
  print('{} is not a leap year .'. format(year))



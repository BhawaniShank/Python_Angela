TOTAL_LIFE_EXPECTANCY_YEARS = 90
DAYS_IN_YEAR = 365
DAYS_IN_MONTH = 30
DAYS_IN_WEEK = 7

age = int(input("What is your current age? "))  
days_lived = age * DAYS_IN_YEAR
remaining_days = (TOTAL_LIFE_EXPECTANCY_YEARS * DAYS_IN_YEAR) - days_lived
remaining_weeks = remaining_days // DAYS_IN_WEEK
remaining_months = remaining_days // DAYS_IN_MONTH
print(f"You have {remaining_days} days, {remaining_weeks} weeks, and {remaining_months} months left.")
# 🚨 Don't change the code below 👇
age = input("What is your current age? ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

age = int(age)

days_left =  90*365 - age*365

weeks_left =  90*52 - age*52

months_left =  90*12 - age*12

years_left = 90 - age

print(f"you are left with {days_left} days, {weeks_left} weeks, {months_left} months, {years_left} years of your life is you live for 90 years")
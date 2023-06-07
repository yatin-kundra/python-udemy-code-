#If the bill was $150.00, split between 5 people, with 12% tip.

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

bill = input("Enter the total amount spent $")
p = input("Enter the percentage of tip: ")          # p is percentage
people = input("Enter number of people you want to split the net amount: ")
bill = float(bill)          #it's float so that you can use floating point numbers
p = int(p)
people = int(people)

tip_money = (bill * p)/100


share = round(((bill + tip_money)/people) , 2)
# share = (bill + tip_money)/people
share = "{:.2f}".format(share)          # foramt function is use so that we can peoperly round off our bill.
print(f" each person have to pay ${share}")

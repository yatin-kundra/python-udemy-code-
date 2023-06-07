#Write your code below this row 👇
for number in range(1,101):
  if number%3 == 0 and number%5 == 0 :
    print("fizzbuzzz")

  elif number%3==0:
    print("fizz")


  elif number%5==0:
    print("buzz")
 # elif number%15==0:

  else:
    print(number)


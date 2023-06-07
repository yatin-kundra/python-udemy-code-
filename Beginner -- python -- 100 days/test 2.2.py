# 🚨 Don't change the code below 👇
height = input("enter your height in m: ")
weight = input("enter your weight in kg: ")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

# BMI = WEIGHT(KG) / HEIGHT * 2 (M^2)

BMI =  int(weight) / (float(height) ** 2)

# print(type(BMI))

print("your BMI - body mass index is " + str(int(BMI)))

# we have converted BMI to int to give ans in whole number









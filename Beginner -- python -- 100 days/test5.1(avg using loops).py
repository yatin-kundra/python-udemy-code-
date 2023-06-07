# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
  total = 0
for height in student_heights:
  total += height
print(total)
total = float(total)

leen = 0
for people in student_heights:
  leen += 1
print(leen)
leen = float(leen)

print(f"{total/leen } is the average height of the class")




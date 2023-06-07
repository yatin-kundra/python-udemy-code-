# max()  functon can do the folloing thing in a go but we want to lean how is max created
# min() givies  minimum value in a list




# 🚨 Don't change the code below 👇
student_scores = input("Input a list of student scores ").split()
for n in range(0, len(student_scores)):
  student_scores[n] = int(student_scores[n])
print(student_scores)
# 🚨 Don't change the code above 👆

#Write your code below this row 👇
maximum = 0
# student_scores = int(student_scores)
for score in student_scores:
  if score >  maximum:
    maximum = score
print(maximum)
# maximum = int(score[0]) > int(score[1])




# 🚨 Don't change the code below 👇
student_heights = input("Input a list of student heights ").split()
for n in range(0, len(student_heights)):
  student_heights[n] = int(student_heights[n])
# 🚨 Don't change the code above 👆


#Write your code below this row 👇
total_height = 0
count = 0

#not using len or sum function
for heights in student_heights:
  total_height += heights
  count += 1

print(f"Thre are total {count} heights in student_heights")

avg_height = total_height / count
print(f"The average height of all students is {round(avg_height)}")


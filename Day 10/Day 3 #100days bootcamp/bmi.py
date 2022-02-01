# 🚨 Don't change the code below 👇
height = float(input("enter your height in m: "))
weight = float(input("enter your weight in kg: "))
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

bmi = weight / (height * height)


if bmi < 18.5:
  print("You're underweight")
elif bmi < 25:
  print("You're normal weight")
elif bmi < 30:
  print("You're slightly overweight")
elif bmi < 35:
  print("You're obese")
else:
  print("You're clinically obese")



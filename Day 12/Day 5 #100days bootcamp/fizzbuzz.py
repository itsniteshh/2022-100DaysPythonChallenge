#Write your code below this row 👇

for nums in range(1, 100+1):
    #for catching nums divisible by all 
  if nums % 3== 0 and nums % 5== 0:
    print("FizzBuzz")
  elif nums % 3== 0:
    print("Fizz")
  elif nums % 5== 0:
    print("Buzz")
  else:
    print(nums)
#Write your code below this row 👇
#for storing the total
total = 0

for nums in range(1, 100+1):
  if nums % 2 == 0:
    total += nums
  

print(f"The sum of all even nums from 1 to 100 including both will be {total}")
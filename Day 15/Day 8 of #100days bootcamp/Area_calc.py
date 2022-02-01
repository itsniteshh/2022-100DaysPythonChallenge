#Write your code below this line 👇
def paint_calc(height, width, cover):
    #a function for getting to know the number of cans we'll need for paintaing the wall
    number_of_cans = (test_h + test_w) / coverage
    print(f"We need '{round(number_of_cans)}' for painting the wall")



#Write your code above this line 👆
# Define a function called paint_calc() so that the code below works.   

# 🚨 Don't change the code below 👇
test_h = int(input("Height of wall: "))
test_w = int(input("Width of wall: "))
coverage = 5
paint_calc(height=test_h, width=test_w, cover=coverage)



def number_of_cans(height, width):
   no_cans = round((int(height) * int(width)) / 5)
   print(f"You need {no_cans} cans to paint the wall")

number_of_cans(input("Enter the height: "), input("Enter the weight: "))
weight = int(input("Enter weight: "))
height = float(input("Enter height: "))
x = weight/float(height*height)
if x < 18.5:
  print("Underweight")
elif x >= 18.5 and x < 25:
  print("Normal")
elif x >= 25 and x < 30:
  print("Overweight")
else:
  print("Obesity")


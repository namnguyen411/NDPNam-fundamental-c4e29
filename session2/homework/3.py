x = int(input("Height in cm: "))
y = int(input("Weight in kg: "))

bmi = y / ((x/100)**2)

if bmi < 16:
    print("severely underweight")
elif bmi <= 18.25:
    print("underweight")
elif bmi <=25:
    print("normal")
elif bmi <=30:
    print("overweight")
else:
    print("obese")
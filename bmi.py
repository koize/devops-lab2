def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    if bmi < 18.5:
        weightclass = "Under Weight"
    elif 25 > bmi >= 18.5:
        weightclass = "Normal Weight"
    else:
        weightclass = "Over Weight"
    print("BMI = " + str(bmi) + ", " + weightclass)


calculate_bmi(weight=57, height=1.73)
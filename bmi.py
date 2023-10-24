def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    weightClass = ""
    if bmi < 18.5:
        weightClass = "Under Weight"
    elif bmi < 25 and bmi >= 18.5:
        weightClass = "Normal Weight"
    else:
        weightClass = "Over Weight"
    print("BMI = " + str(bmi) + ", " + weightClass)


calculate_bmi(weight=57, height=1.73)
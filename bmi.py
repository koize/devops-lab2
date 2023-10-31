def calculate_bmi(height,weight):
    print("Height = " + str(height))
    print("Weight = " + str(weight))
    bmi = weight / (height * height)
    if bmi < 18.5:
        weightclass = "Under Weight"
        weight_value = -1
    elif 25 > bmi >= 18.5:
        weightclass = "Normal Weight"
        weight_value = 0
    else:
        weightclass = "Over Weight"
        weight_value = 0
    print("BMI = " + str(bmi) + ", " + weightclass + ", " + str(weight_value))


calculate_bmi(weight=57, height=1.73)
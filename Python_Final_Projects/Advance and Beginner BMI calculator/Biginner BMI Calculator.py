
def calculate_bmi(weight, height):
    bmi = weight / (height ** 2)
    return bmi

def check_bmi(bmi):
    if bmi < 19.5:
        return "Underweight"
    elif 19.5 <= bmi < 25:
        return "Normal weight"
    elif 26 <= bmi < 30:
        return "Overweight"
    else:
        return "Obesity"

def main():
    weight = float(input("Enter your weight in kilograms: "))
    height = float(input("Enter your height in meters: "))


    bmi = calculate_bmi(weight, height)
    checking = check_bmi(bmi)

    print("Your BMI is: {:.2f}".format(bmi))
    print("Interpretation: ", checking)

if __name__ == "__main__":
    main()

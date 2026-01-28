# BMI Calculator
height = float(input("Enter height in meters: "))
weight = float(input("Enter weight in kilograms: "))
bmi = weight / (height ** 2)
if bmi >= 30:
    print("Obesity")
elif bmi >= 25:
    print("Overweight")
elif bmi >= 18.5:
    print("Normal")
else:
    print("Underweight")


# City to Country
city = input("Enter city name: ")
if city in ["Sydney", "Melbourne", "Brisbane", "Perth"]:
    print(city, "is in Australia")
elif city in ["Dubai", "Abu Dhabi", "Sharjah", "Ajman"]:
    print(city, "is in UAE")
elif city in ["Mumbai", "Bangalore", "Chennai", "Delhi"]:
    print(city, "is in India")
else:
    print("City not found")

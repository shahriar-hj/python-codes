# Tamrin 1 BMI

w = float(input('وزن خود را وارد کنید!'))
h = float(input('قد خود را وارد کنید!'))
bmi = w/(h**2)

if bmi < 18.5:
    print("Under weight")
elif 18.5 <= bmi < 25:
    print("Normal")
elif 25 <= bmi < 30:
    print("Over Weight")
else:
    print("Obesity")

# Tamrin Kelassi BMI by IS

q = str(input('آیا از واحد های IS استفاده میکنید ؟!'))
d = ["yes", "are", "ohoom", "y", "no", "na", "noch", "n"]
indx = d.index(q)
print(indx)
if 0 <= indx < 3:
    w = float(input('وزن خود را وارد کنید!'))
    h = float(input('قد خود را وارد کنید!'))
    bmi = w / (h ** 2)

    if bmi < 18.5:
        print("Under weight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Over Weight")
    else:
        print("Obesity")
else:
    w = float(input('وزن خود را وارد کنید!'))
    h = float(input('قد خود را وارد کنید!'))
    bmi = (w / (h ** 2))*703

    if bmi < 18.5:
        print("Under weight")
    elif 18.5 <= bmi < 25:
        print("Normal")
    elif 25 <= bmi < 30:
        print("Over Weight")
    else:
        print("Obesity")

number = float(input())
convert_from = str(input())
convert_to = str(input())

if convert_from == "m" and convert_to == "mm":
    result = number * 1000
    print(f"{result:.3f}")
elif convert_from == "m" and convert_to == "cm":
    result = number * 100
    print(f"{result:.3f}")
elif convert_from == "cm" and convert_to == "m":
    result = number / 100
    print(f"{result:.3f}")
elif convert_from == "cm" and convert_to == "mm":
    result = number * 10
    print(f"{result:.3f}")
elif convert_from == "mm" and convert_to == "cm":
    result = number / 10
    print(f"{result:.3f}")
elif convert_from == "mm" and convert_to == "m":
     result = number / 1000
     print(f"{result:.3f}")

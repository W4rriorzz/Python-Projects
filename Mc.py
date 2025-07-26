def app():
    while True:
        try:
            eng = int(input("English mark? "))
            break
        except ValueError:
            print("Type a number please")

    while True:
        try:
            math = int(input("Math mark? "))
            break
        except ValueError:
            print("Type a number please")

    while True:
        try:
            arabic = int(input("Arabic mark? "))
            break
        except ValueError:
            print("Type a number please")

    while True:
        try:
            science = int(input("Science mark? "))
            break
        except ValueError:
            print("Type a number please")

    while True:
        try:
            social = int(input("Social mark? "))
            break
        except ValueError:
            print("Type a number please")
    marks = eng + math + arabic + social + science
    print(f"Total marks : {marks}")
app()

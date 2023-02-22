age = input("Insert your age: ")
age_int = int(age)

height = input("Insert your height(m): ")
height_int = float(height)

if height_int >= 1.62 and age_int > 14:
    print("Enjoy the game!")
elif height_int < 1.62:
    print("You are not tall enough")
elif age_int < 14:
    print("You are too young for this game")
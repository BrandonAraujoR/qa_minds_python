day = input("Insert the number of day when you born: ")
month = input("Insert the number of month when you born: ")
month_int = int(month)
year = input("Insert the year when you born : ")
year_int = int(year)

person_age = 2023 - year_int
print(f"You are {person_age}")

if month_int >= 2:
    print("You will turn one year soon")
else:
    print("You turned one year, congrats")

if year_int <= 1939:
    print("You are from La Generacion silenciosa")
elif year_int < 1920:
    print("Your generation doesn't have a name, sorry")
elif year_int <= 1959:
    print("You are from Los babyboomers")
elif year_int <= 1979:
    print("You are from Generacion X")
elif year_int <= 1989:
    print("You are from Generacion Y or Millenials")
elif year_int <= 1990:
    print("You are from Generacion Z")

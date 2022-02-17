infile = open("WorldSeriesWinners.txt", "r")

dict = {}
dict2 = {}

user_year = int(input("What year (from 1903-2009) would you like to display? "))


year = 1903


for line in infile:
    if user_year < 1903:
        print("Please choose a year within the range 1903-2009")
        user_year = int(input())
    elif user_year > 2009:
        print("Please choose a year within the range 1903-2009")
        user_year = int(input())
    else:
        if line in dict:
            dict[line] += 1
        else:
            dict[line] = 1
    dict2[year] = line
    year += 1

print(dict2)

print(
    "The",
    dict2[user_year],
    "have won the World Series",
    dict[dict2[user_year]],
    "times.",
)

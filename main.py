
# String Concatenation
day = "30"
year = "2021"
month = "August"

today_is = month + " " + day + ", " + year

print(today_is)

# Converting Data to Strings

day = "30"
year = "2021"
month = "August"

today_is = month + " " + str(day) + ", " + str(year)

print(today_is)

day = "30"
year = "2021"
month = "August"

today_is = str.format("{0} {1}, {2}", month, day, year)
print(today_is)

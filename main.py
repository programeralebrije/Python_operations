
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

today_is = str.format("The day is {0} {1}, {2}", month, day, year)
print(today_is)


my_message = "THESE ARE ALL CAPS"

print(my_message.lower())

my_message = "these are all lower"

print(my_message.upper())

# This is a string concatenation

experience = "I have " + str(10) + " years of experience"   

# Replacing Text in a String

experience = "this game is fun "
better_experience = experience.replace("fun" , "amazing") 

print(better_experience)
print(experience)

message = "I like cats, because cats are friendly"
new_message = message.replace('cats', 'dogs')

print(new_message)


# Splitting with Defaults

my_message = "Split these words for me"
split_at_spaces = my_message.split()

print(split_at_spaces)

# Splitting with a Specified Separator


my_message = "apples,oranges,bananas"
split_at_commas = my_message.split(",")

print(split_at_commas)

# Assignment Operators

a = 15
b = 5
c = 0

c = a + b
print("1. C =", c)

c += a
print("2. C =", c)

c *= a
print("3. C =", c)

c /= a
print("4. C =", c)

c %= a
print("5. C =", c)

c //= b
print("6. C =", c)

c = 4
c **= a
print("7. C =", c)

my_burger_price = 15

is_fifteen_dollars = my_burger_price == 15

is_not_twenty_dollars = my_burger_price != 20

# Comparison Operators with Strings
my_name = "Sally"
your_name = "Billy"
some_name = "Sally"

print(my_name == your_name)
print(my_name != your_name)
print(some_name == my_name)

print("---")

my_name = "Joe"   # uppercase j
some_name = "joe" # lowercase j

print(my_name == some_name)
print(my_name.upper() == some_name.upper())

# Logical Operators

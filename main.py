
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


# details of the person who wants to watch the movie
person_age = 17
person_money = 25

# the requirements to watch the movie
age_restriction = 18
movie_price = 10

# conditions
is_old_enough = person_age >= age_restriction
has_enough_money = person_money >= movie_price

# two conditions combined using 'and'
can_watch_movie = is_old_enough and has_enough_money
print(can_watch_movie)

# the output is False, because the person's age is less than the required age

# Combining Logical Operators

amount_of_money = 10
is_a_friend = True


result = (10 > 3) and (3 < 9) and ("this" != "that")
can_hangout_with_me = amount_of_money >= 25 or is_a_friend
print(can_hangout_with_me)

person_age = 12
is_old_enough = person_age >= 18

must_leave = not is_old_enough
print(must_leave)

# output is True (must leave), because the person is NOT old enough (age < 18)

my_age = 17
my_money = 7
is_friend = True
has_food = False

can_watch_movie = not has_food and ((my_age >= 18 and my_money >= 15) or (is_friend and my_money >= 5))

print(can_watch_movie)

a = 15
b = 5
c = 0

c = a + b
print("1. C =", c)

a = 25
b = 19
c = 0

c = a - b
print ("c =",c)


# Indentation

my_message = "Hello World"
print (my_message)

person_money = 8

if person_money >= 10:
  print("This person can watch the movie")
else:
  print("Sorry, but you don't have enough money")

#   elif

person_age = 18

if person_age >= 18:
  print("I can watch an R-rated movie")
elif person_age >= 13:
  print("I can watch a PG13-rated movie")
else:
  print("I can watch a G-rated movie")


  person_age = 13

if person_age >= 13:
  print("I can watch a PG13-rated movie")
elif person_age >= 18:
  print("I can watch an R-rated movie")
else:
  print("I can watch a G-rated movie")

  person_age = 5

if person_age >= 18:
  print("I can watch an R-rated movie")
elif person_age >= 13:
  print("I can watch a PG13-rated movie")
else:
  print("I can watch a G-rated movie")

#   Multiple Decision Making Blocks per Variable

# assign 10 to types_of_people
types_of_people = 10
# assign the f-string to x (insert types_of_people ub tge string)
x = f"There are {types_of_people} types of people."

# assign the string "binary" to the variable, binary
binary = "binary"
# assign the string "don't" to the variable, do_not
do_not = "don't"
y = f"Those who know {binary} and those who {do_not}."

print(x)
print(y)

print(f"I said: {x}")
print(f"I also said: '{y}'")

hilarious = False
joke_evaluation = "Isn't that joke so funny?! {}"

print(joke_evaluation.format(hilarious))

w = "This is the left side of..."
e = "a string with a right side."

print(w + e)

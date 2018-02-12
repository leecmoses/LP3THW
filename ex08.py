formatter = "{} {} {} {}"

print(formatter.format(1, 2, 3, 4,))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Don't let ego",
    "get to your head.",
    "And, don't let failure",
    "get to your hear."
))

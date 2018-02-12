name = 'Moses Lee'
age = 25 # not a lie
height = 66 # inches
i_height = round(height * 2.54) # centimeters
weight = 142.5 # lbs
i_weight = round(weight * 0.453592) # kilograms
eyes = 'Brown'
teeth = 'White'
hair = 'Black'

print(f"Let's talk about {name}.")
print(f"He's {height} inches tall which is about {i_height} centimeters.")
print(f"He's {weight} pounds heavy which is about {i_weight} kilograms.")
print("Actually that's not heavy.")
print(f"He's got {eyes} eyes and {hair} hair.")
print(f"His teeth are usually {teeth} depending on the tea.")

# this line is tricky, try to get it exactly right
total = age + height + weight
print(f"If I add {age}, {height}, and {weight} I get {total}.")

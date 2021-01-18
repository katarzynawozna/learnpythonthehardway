name = "Kajetan Bochajczuk"
age = 24  # still
height = 180  # cm
height_inch = round(height * 0.393)
weight = 75  # kg
weight_lbs = round(weight * 2.2)
eyes = "Brown"
teeth = "White"  # lol
hair = "Blonde"
pron1 = "He's"
pron2 = "His"

print(f"Let's talk about {name}. \n{pron1} {height} cm tall (that is {height_inch} inches) and {weight} kilo heavy, which is {weight_lbs} lbs. \nActually that's not that heavy. \n{pron1} got {eyes} eyes and {hair} hair. \n{pron2} teeth are usually {teeth} depending on the coffee.")

total = age + height + weight
print(f"If I add {age}, {height} and {weight} I get {total}")

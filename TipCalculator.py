meal = input("What was the cost of your meal? $")

# Convert string to floating integer
meal = float(meal)

tip = input("Please enter the tip percentage you want to give (20,25,30...) ")

# Convert string to floating integer
tip = float(tip)

# Calculating tip
tipamt = meal * tip / 100
print("Tip amout is $%5.2f at %2.0f percent" % (tipamt,tip))
total = meal + tipamt
print("Total cost of the meal is $%5.2f" % total)
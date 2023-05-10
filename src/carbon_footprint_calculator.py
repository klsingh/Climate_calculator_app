# Import the calculate_carbon_footprint function from the carbon_footprint module
from carbon_footprint import calculate_carbon_footprint

# Get input from user
miles_driven = float(input("How many miles have you driven in the last year? "))
flights_taken = int(input("How many flights have you taken in the last year? "))
meat_consumption = float(input("How many pounds of meat have you consumed in the last year? "))

# Calculate carbon footprint
carbon_footprint = calculate_carbon_footprint(miles_driven, flights_taken, meat_consumption)

# Display result
print(f"Your carbon footprint for the last year is {carbon_footprint:.2f} metric tons of CO2e.")

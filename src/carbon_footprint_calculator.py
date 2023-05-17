class CarbonFootprintCalculator:
    def calculate_carbon_footprint(self, miles_driven, flights_taken, meat_consumption):
        # Calculate the carbon footprint based on the provided inputs
        carbon_footprint = miles_driven * 0.42 + flights_taken * 1.5 + meat_consumption * 3.6
        return carbon_footprint

# Get input from user
miles_driven = float(input("How many miles have you driven in the last year? "))
flights_taken = int(input("How many flights have you taken in the last year? "))
meat_consumption = float(input("How many pounds of meat have you consumed in the last year? "))

# Create an instance of the CarbonFootprintCalculator class
calculator = CarbonFootprintCalculator()

# Calculate carbon footprint
carbon_footprint = calculator.calculate_carbon_footprint(miles_driven, flights_taken, meat_consumption)

# Display result
print(f"Your carbon footprint for the last year is {carbon_footprint:.2f} metric tons of CO2e.")

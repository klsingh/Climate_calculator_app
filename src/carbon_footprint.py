# Calculate carbon footprint based on lifestyle choices
def calculate_carbon_footprint(miles_driven, flights_taken, meat_consumption):
    total_carbon_footprint = (miles_driven * 0.404) + (flights_taken * 0.747) + (meat_consumption * 7.61)
    return total_carbon_footprint
from user_authentication import UserAuthentication
from data_handler import DataHandler
from carbon_credit_system import CreditPointTracker
from carbon_footprint_calculator import calculate_carbon_footprint

def main():
    # Connect to the database
    data_handler = DataHandler('db/climate_calculator.db')

    # Create an instance of UserAuthentication
    user_auth = UserAuthentication()

    # Login or create an account
    user_id = user_auth.authenticate_user(data_handler)

    # Get credit points for the user
    credit_point_tracker = CreditPointTracker(user_id)

    # Get input from the user
    miles_driven = float(input("How many miles have you driven in the last year? "))
    flights_taken = int(input("How many flights have you taken in the last year? "))
    meat_consumption = float(input("How many pounds of meat have you consumed in the last year? "))

    # Calculate carbon footprint
    carbon_footprint = calculate_carbon_footprint(miles_driven, flights_taken, meat_consumption)

    # Deduct credit points based on the carbon footprint
    credit_point_tracker.deduct_credit_points(carbon_footprint)

    # Update credit points in the database
    data_handler.update_credit_points(user_id, credit_point_tracker.credit_points)

    # Display the result
    print(f"Your carbon footprint for the last year is {carbon_footprint:.2f} metric tons of CO2e.")

if __name__ == '__main__':
    main()

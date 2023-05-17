from src.user_authentication import authenticate_user
from src.data_handler import DataHandler
from src.carbon_credit_system  import CreditPointTracker
from src.carbon_footprint import CarbonFootprint

def main():
    # Connect to database
    data_handler = DataHandler('db/climate_calculator.db')

    # Login or create account
    user_id = authenticate_user(data_handler)

    # Get credit points for user
    credit_point_tracker = CreditPointTracker(user_id)

    # Calculate carbon footprint
    carbon_footprint = CarbonFootprint()
    carbon_footprint.calculate()

    # Deduct credit points based on carbon footprint
    carbon_credits = carbon_footprint.get_carbon_credits()
    credit_point_tracker.deduct_credit_points(carbon_credits)

    # Update credit points in the database
    data_handler.update_credit_points(user_id, credit_point_tracker.credit_points)

if __name__ == '__main__':
    main()

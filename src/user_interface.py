import tkinter as tk
from tkinter import *
from climate_calculator.src.user_authentication import UserAuthentication
from src.carbon_footprint_calculator import calculate_carbon_footprint
from src.carbon_credit_system import add_credit_points, get_credit_points
from src.user_authentication import authenticate_user, login, logout

# Create the main window
root = tk.Tk()
root.title('Climate Calculator')

# Define global variables
user_id = None

# Create a function to handle the login button
def handle_login():
    global user_id

    # Get the username and password from the entry fields
    username = username_entry.get()
    password = password_entry.get()

    # Attempt to log in with the given credentials
    user_id = login(username, password)

    # If login is successful, show the main window
    if user_id is not None:
        # Hide the login window
        login_window.destroy()

        # Show the main window
        show_main_window()
    else:
        # Show an error message
        error_label.config(text='Invalid username or password')

        # Create the login window
        login_window = tk.Tk()

        # Create a label for the username
        username_label = tk.Label(login_window, text='Username')
        username_label.pack()

        # Create an entry field for the username
        username_entry = tk.Entry(login_window)
        username_entry.pack()

        # Create a label for the password
        password_label = tk.Label(login_window, text='Password')
        password_label.pack()

        # Create an entry field for the password
        password_entry = tk.Entry(login_window, show='*')
        password_entry.pack()

        # Create a button for the login
        login_button = tk.Button(login_window, text='Login', command=handle_login)
        login_button.pack()

        # Create a label for displaying errors
        error_label = tk.Label(login_window, fg='red')
        error_label.pack()

        # Start the login window's event loop
        login_window.mainloop()

        # Create a function to handle the login button
    def handle_login():
        global user_id

        # Get the username and password from the entry fields
        username = username_entry.get()
        password = password_entry.get()

        # Attempt to log in with the given credentials
        user_id = login(username, password)

    # If login is successful, show the main window
    if user_id is not None:
        # Hide the login window
        login_window.destroy()

        # Show the main window
        show_main_window()
    else:
        # Show an error message
        error_label.config(text='Invalid username or password')

# Create a function to handle the calculate button
    def handle_calculate():
        global user_id

    # Get the inputs from the entry fields
    distance = float(distance_entry.get())
    vehicle = vehicle_var.get()
    fuel_efficiency = float(fuel_efficiency_entry.get())
    electricity = float(electricity_entry.get())

    # Calculate the carbon footprint
    carbon_footprint = calculate_carbon_footprint(distance, vehicle, fuel_efficiency, electricity)

    # Update the result label
    result_label.config(text='{:.2f} kg CO2e'.format(carbon_footprint))

    # Add credit points to the user's account
    credit_points = int(carbon_footprint / 10)  # 1 credit point for every 10 kg CO2e
    add_credit_points(user_id, credit_points)

    # Update the credit points value label
    credit_points_value.config(text=str(get_credit_points(user_id)))

# Create a function to show the main window
def show_main_window():
    # Create a new window
    global main_window
    main_window = Toplevel(root)
    main_window.title('Climate Calculator')

    # Create a label for the welcome message
    welcome_label = Label(main_window, text='Welcome, {}'.format(user_id))
    welcome_label.grid(row=0, column=0)

    # Create a label for the carbon footprint calculator
    calculator_label = Label(main_window, text='Carbon Footprint Calculator')
    calculator_label.grid(row=1, column=0)

    # Create a label for the distance
    distance_label = Label(main_window, text='Distance (km)')
    distance_label.grid(row=2, column=0)

    # Create an entry for the distance
    global distance_entry
    distance_entry = Entry(main_window)
    distance_entry.grid(row=2, column=1)

    # Create a label for the vehicle type
    vehicle_label = Label(main_window, text='Vehicle Type')
    vehicle_label.grid(row=3, column=0)

    # Create a variable for the vehicle type
    global vehicle_var
    vehicle_var = StringVar(main_window)
    vehicle_var.set('Car')

    # Create a dropdown for the vehicle type
    vehicle_dropdown = OptionMenu(main_window, vehicle_var, 'Car', 'Motorcycle', 'Bus', 'Train', 'Airplane')
    vehicle_dropdown.grid(row=3, column=1)

        # Create a label for the fuel efficiency
    fuel_efficiency_label = Label(main_window, text='Fuel Efficiency (km/L)')
    fuel_efficiency_label.grid(row=4, column=0)

    # Create an entry for the fuel efficiency
    global fuel_efficiency_entry
    fuel_efficiency_entry = Entry(main_window)
    fuel_efficiency_entry.grid(row=4, column=1)

    # Create a label for the electricity usage
    electricity_label = Label(main_window, text='Electricity Usage (kWh)')
    electricity_label.grid(row=5, column=0)

    # Create an entry for the electricity usage
    global electricity_entry
    electricity_entry = Entry(main_window)
    electricity_entry.grid(row=5, column=1)

    # Create a button to calculate the carbon footprint
    calculate_button = Button(main_window, text='Calculate', command=handle_calculate)
    calculate_button.grid(row=6, column=0)

    # Create a label for the result
    global result_label
    result_label = Label(main_window, text='')
    result_label.grid(row=6, column=1)

    # Create a button to log out
    logout_button = Button(main_window, text='Log Out', command=handle_logout)
    logout_button.grid(row=7, column=0)

    # Create a label for the credit points
    credit_points_label = Label(main_window, text='Credit Points')
    credit_points_label.grid(row=8, column=0)

    # Create a label for the credit points value
    global credit_points_value
    credit_points_value = Label(main_window, text=str(get_credit_points(user_id)))
    credit_points_value.grid(row=8, column=1)


def handle_logout():
    """
    Performs the logout operation for the user.
    """
    # Clear the current user session or any relevant data
    # Redirect to the login page or perform any other desired action
    # Example: Clearing the current user session
    UserAuthentication.logout()
    print("Logout successful. Redirecting to the login page...")
    # Redirect to the login page or perform any other desired action after logout
    pass
# Create a function to handle the calculate button
def handle_calculate():
    global user_id

    # Get the inputs from the entry fields
    distance = float(distance_entry.get())
    vehicle = vehicle_var.get()
    fuel_efficiency = float(fuel_efficiency_entry.get())
    electricity = float(electricity_entry.get())

    # Calculate the carbon footprint
    carbon_footprint = calculate_carbon_footprint(distance, vehicle, fuel_efficiency, electricity)

    # Update the result label
    result_label.config(text='{:.2f} kg CO2e'.format(carbon_footprint))

    # Add credit points to the user's account
    credit_points = int(carbon_footprint / 10)  # 1 credit point for every 10 kg CO2e
    add_credit_points(user_id, credit_points)

    # Update the credit points value label
    credit_points_value.config(text=str(get_credit_points(user_id)))
def show_login_window():
    """
    Displays the login window.
    """
    login_window = tk.Tk()

    # Create a label for the username
    username_label = Label(login_window, text='Username')
    username_label.pack()

    # Create an entry field for the username
    username_entry = Entry(login_window)
    username_entry.pack()

    # Create a label for the password
    password_label = Label(login_window, text='Password')
    password_label.pack()

    # Create an entry field for the password
    password_entry = Entry(login_window, show='*')
    password_entry.pack()

    # Create a button for the login
    login_button = Button(login_window, text='Login', command=handle_login)
    login_button.pack()

    # Create a label for displaying errors
    error_label = Label(login_window, fg='red')
    error_label.pack()

    # Start the login window's event loop
    login_window.mainloop()

def handle_logout():
    """
    Performs the logout operation for the user.
    """
    # Destroy the main window
    main_window.destroy()

    # Show the login window
    show_login_window()

# Call the function to show the login window
    show_login_window()

# Start the main event loop
    root.mainloop()
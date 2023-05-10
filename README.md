# Climate Calculator
## App allows user to calculate their day-to-day carbon footprint

The Climate Calculator is an application that allows users to calculate their carbon footprint and track their carbon credit points. It provides a user-friendly interface for entering travel and energy consumption data, and calculates the corresponding carbon footprint. Users can also earn credit points based on their carbon footprint and track their progress over time.

## Directory Structure
### The directory structure of the Climate Calculator application is as follows:
```
climate_calculator/
├── data/
│   ├── users.json
│   ├── carbon_data.csv
│   └── credit_points.json
├── db/
│   └── climate_calculator.db
├── src/
│   ├── __init__.py
│   ├── carbon_footprint_calculator.py
│   ├── carbon_credit_system.py
│   ├── data_handler.py
│   ├── main.py
│   ├── user_interface.py
│   └── user_authentication.py
└── ui/
    ├── __init__.py
    ├── climate_calculator_gui.py
    ├── create_account_gui.py
    └── login_gui.py
 ```

The `data/ directory` contains the data files used by the application, including `users.json` for user information, `carbon_data.csv` for carbon footprint data, and `credit_points.json` for credit point tracking.

The `db/ directory` contains the database file `climate_calculator.db` used for storing persistent data.

The `src/ directory` contains the main source code files of the application:

`__init__.py` is an initialization file for the `src` module.

`carbon_footprint_calculator.py` contains the logic for calculating the carbon footprint based on user input.

`carbon_credit_system.py` handles the credit point system, including adding and retrieving credit points.

`data_handler.py` provides functions for reading and writing data to the data files.

`main.py` is the main entry point of the application.

`user_interface.py` contains the graphical user interface (GUI) code for the application.

`user_authentication.py` handles user authentication and login/logout functionality.

## The ui/ directory contains GUI-related files:

`__init__.py` is an initialization file for the ui module.

`climate_calculator_gui.py` contains the main GUI code for the Climate Calculator application.

`create_account_gui.py` provides the GUI for creating a new user account.

`login_gui.py` provides the GUI for user login.

## Usage
### To use the Climate Calculator application, follow these steps:

Ensure you have the necessary dependencies installed. You can refer to the `Dependencies` section in the README file or any installation instructions provided.

### Set up the required data files and database:

Ensure the `data/ directory` is present and contains the required data files (`users.json`, `carbon_data.csv`, and `credit_points.json`).

Ensure the `db/ directory` is present and contains the `climate_calculator.db` database file.

Run the `main.py` file to start the application.

The application will launch, and you will be presented with the login screen. If you don't have an account, you can click on the `Create Account` button to create a new account.

After logging in, you will see the main interface of the Climate Calculator application. Enter the necessary data such as `distance traveled`, `vehicle type`, `fuel efficiency`, and `electricity usage`.

Click on the `Calculate` button to calculate the carbon footprint based on the entered data. The result will be displayed on the screen, showing the calculated carbon footprint value.

The application also tracks your carbon credit points. Based on your carbon footprint, you will earn or lose credit points. The credit points are updated automatically and displayed on the screen.

You can navigate through different sections of the application using the provided menu options or buttons. This includes viewing your profile, updating account information, and accessing the credit point history.

In the profile section, you can view and modify your personal information, including name, email, and password. You can also view your current carbon footprint and credit point balance.

The credit point history section displays a log of your earned or lost credit points over time. This allows you to track your progress and see the impact of your actions on your credit point balance.

To log out of the application, click on the `Logout` button. This will securely end your session and return you to the login screen.

Remember to save your data periodically by clicking on the `Save` button or using any provided save functionality. This ensures that your data is stored securely and can be accessed in future sessions.

## Dependencies
### The Climate Calculator application has the following dependencies:
```
Python (version 3.6 or higher)
PyQt5 (for GUI components)
SQLite (for database functionality)
```
### To install the dependencies, you can use the following command:
```
pip install -r requirements.txt
```
Make sure you have a compatible version of `Python` installed before running the above command.

## Conclusion
The Climate Calculator application provides an easy-to-use interface for calculating carbon footprints and tracking carbon credit points. By using this application, you can gain insights into your carbon emissions and take steps to reduce your impact on the environment.

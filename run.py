# Your code goes here.
# You can delete these comments, but do not change the name of this file
# Write your code to expect a terminal of 80 characters wide and 24 rows high
import gspread
from google.oauth2.service_account import Credentials

SCOPE = [
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
    ]

CREDS = Credentials.from_service_account_file('creds.json')
SCOPED_CREDS = CREDS.with_scopes(SCOPE)
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)
SHEET = GSPREAD_CLIENT.open('love_sandwiches')

# Commented-out code below was to check the API was working:
# sales = SHEET.worksheet('sales')
# data = sales.get_all_values()
# print(data)

def get_sales_data():
    """
    Get sales data from user input in the form of a csv file
    """
    print("Please enter sales data from the last market.")
    print("Data should be 6 numbers, seperated by commas.")
    print("Example: 10,20,30,40,50,60\n")

    data_str = input("Enter you data here: ")
    print(f"The data provided is {data_str}")

get_sales_data()
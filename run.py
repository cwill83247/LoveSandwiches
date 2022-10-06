import gspread                                                      #std for importing
from google.oauth2.service_account import Credentials               #std for using google api    

SCOPE = [                                                           #std defining the apis we want to use
    "https://www.googleapis.com/auth/spreadsheets",
    "https://www.googleapis.com/auth/drive.file",
    "https://www.googleapis.com/auth/drive"
]

CREDS = Credentials.from_service_account_file('creds.json')         #std in UPPERCASE as constant Variable
SCOPED_CREDS = CREDS.with_scopes(SCOPE)                             #std
GSPREAD_CLIENT = gspread.authorize(SCOPED_CREDS)                    #std    
SHEET = GSPREAD_CLIENT.open('love_sandwichescw')                    #specific to spreadsheet calling

sales = SHEET.worksheet('sales')                                    #specific to sheet in worksheet
data = sales.get_all_values()                                       #std calling the above sales variable
print(data)                                                         #std displaying the output

def get_sales_data():                                               #start of function
    """
    our function is getting the sales data for each sandwich formt he user
    """
    print ("Pleae enter sales data")
    print ("Sales data shoud be entered in csv format ie 10,12,14,16,18\n") #backslash n \n adds a new line for layout purposes

    data_str = input("Enter your data here:")                   # variable to request and hold data expecting 6 entries seperated by commas
    print(f"The data you have entered is {data_str}")           # end of function

    sales_data = data_str.split(",")                            # this is removing the commas, so just gettign the values and then putting them into an Array seperted by commas
    print(sales_data)
    validate_data(sales_data)                                   # calling function "validate_data" and running it against the values from sales_data


def validate_data(values):                                    # new function for validating data expecting a parameter we have called it "values" just as a holder
    """
    try to convert all strings to ints
    check exactly 6 values

    """
    try:                                                       # start of our try staement 
        if len(values) !=6:                                      # passing in values, if lenght of our array list  that we dont know what they are yet checkign if array is Not = 6
            raise ValueError(
                f"6 Values are required, you provided {len(values)}"
            )
    except ValueError as e:                                    # ???? not sure on this bit 6/10/2022
        print(f"Invalid Data {e}, please try again. \n")


    print(values)


get_sales_data()                                                # calling function



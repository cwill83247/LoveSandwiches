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
    while loop checks if errors and keeps looping until the if statement is true and it hits the break
    """
    while True:
        print ("Please enter sales data")
        print ("Sales data shoud be entered in csv format ie 10,12,14,16,18\n") #backslash n \n adds a new line for layout purposes

        data_str = input("Enter your data here:")                   # variable to request and hold data expecting 6 entries seperated by commas
        print(f"The data you have entered is {data_str}")           # end of function

        sales_data = data_str.split(",")                            # this is removing the commas, so just gettign the values and then putting them into an Array seperted by commas
        print(sales_data)
        validate_data(sales_data)                                   # calling function "validate_data" and running it against the values from sales_data

        if validate_data(sales_data):                               # if statement part of while loop that calls function "validate_data" passes the paramameters form "sales_data"
            print("Data is valid")
            break                                                   # break keyword stops the while loop  when data is valid otherwise wil lre run the programme for the user                                               
    
    return sales_data                                               # ????? is this just returning it to the function ?

def validate_data(values):                                    # new function for validating data expecting a parameter we have called it "values" just as a holder
    """
    try to convert all strings to ints
    check exactly 6 values

    """
    try:                                                         # start of our try statement
        [int(value) for value in values]                         # std this is List Comprehension and trys to convert the string values into ints                            
        if len(values) !=6:                                      # passing in values, if length of our array list  that we dont know what they are yet checkign if array is Not = 6
            raise ValueError(
                f"6 Values are required, you provided {len(values)}"
            )
    except ValueError as e:                                    # std we are assigning the ValueError to the e variable (shorthand in python for error)
        print(f"Invalid Data {e}, please try again. \n")
        return False
    return True                                                 #this has been added so we can evaluate in our While loop     


    print(values)

def update_sales_worksheet(data):                           #function to update worksheet
    """
    function to update the sales worksheet                 
    from users input
    """
    print("updating worksheet.....")
    sales_worksheet = SHEET.worksheet("sales")           # std "sales is name of worksheet in spreadsheet" GSuite GSPREAD Method being used to provide alot of the functionality
    sales_worksheet.append_row(data)                    # std  appending row in worksheet with "data" the data gets passed when it get called/invoked
    print("Sales sheet updated succesfully ")

def main():
    """
    Standard practice to add our function calls 
    into a  function called main
    """
    data = get_sales_data()                                 # calling function
    sales_data =[int(num) for num in data]
    update_sales_worksheet(sales_data)                      # function gets called and passes in the sales_data which needs ot be an int thats why converted above.


print("Welcome to out love Sandwiches data process")


main()                                                      #note functions need to be called after the function has been written


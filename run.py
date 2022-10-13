import gspread                                                      #std for importing
from google.oauth2.service_account import Credentials               #std for using google api    
from pprint import pprint
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
#print(data)                                                         #std displaying the output

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

"""   previous functions that have been refactored
def update_surplus_worksheet(data):                           #function to update worksheet
    
    #function to update the surplus worksheet                 
    #from users input
    
    print("updating worksheet.....")
    surplus_worksheet = SHEET.worksheet("surplus")           # std "sales is name of worksheet in spreadsheet" GSuite GSPREAD Method being used to provide alot of the functionality
    surplus_worksheet.append_row(data)                    # std  appending row in worksheet with "data" the data gets passed when it get called/invoked
    print("surplus updated succesfully ")

def update_sales_worksheet(data):                           #function to update worksheet
    
    #function to update the sales information worksheet                 
    #from users input
    
    print("updating sales worksheet.....")
    sales_worksheet = SHEET.worksheet("sales")           # std "sales is name of worksheet in spreadsheet" GSuite GSPREAD Method being used to provide alot of the functionality
    sales_worksheet.append_row(data)                    # std  appending row in worksheet with "data" the data gets passed when it get called/invoked
    print("Sales sheet updated succesfully ")    
""" #end of refactoring

def update_worksheet(data, worksheet):                  #this is refactoring the 2 above into one function
    """gets figures passed to it for example sales or surplus
    it then updates the relevant worksheet
    """
    print (f" Updating the worksheet: {worksheet}")
    worksheet_to_update = SHEET.worksheet(worksheet) 
    worksheet_to_update.append_row(data)
    print(f"{worksheet} updated succesfully")




def calculate_surplus_data(sales_row):
    """
    calculating the surplus sandwiches
    """
    print("calculating surplus sandwiches")
    stock = SHEET.worksheet("stock").get_all_values()      #this gets all of the values and presents each row as a list form stock sheet, i.e headers row1 = 1 list, row 2 = another list etc...
                                           #pprint has been imported at top of .py filethis is a fancier way of displaying data
    stock_row = stock[-1]                                   # this grabs the last row from our list "stock"  which is effectivley our last row in the stock spreadsheet
    print(f"stock row last entry in sheet {stock_row}")
    print(f"sales row last entry in sheet {sales_row}")

    surplus_data =[]                                         # being used so can append value sinto a new list   
    for sales,stock in zip(sales_row,stock_row):             #std python ZIP method  used to iterate through 2 lists.........
        surplus = (int(stock) -sales)                       # needed to convert stock to an int  CANT takeaway a string and int....
        # print(surplus)
        surplus_data.append(surplus)                        # adding vaues to our empty surplus_data array/list
        print(surplus_data)

    return surplus_data                                        # have to return them      

def get_last_5_sales():
    """
    getting the last 5 sales so we can get an average
    """
    sales = SHEET.worksheet("sales")
    # sales_column = sales.col.values(3)                      #this is getting the values from column 3 these start at 1, not like list index that start at 0 - so creates a list *dont forget its in a string
    sales_columns = []
    
    for ind in range (1,7):                                     #1 is number it should start from and 7 is the number it should end.. this will get 6 entries
        column = sales.col_values(ind)                # creatinga  varible to hold value(s)    sales.col_values is part of gspread method ?? unsure on why passing ind variable
        sales_columns.append(column[-5:])           # this part is using slice column[-5:]  to get last 5 entries .. 
    print(sales_columns)

    return sales_columns    

def calculate_stock_req(data):
    """
    used to calculate stock base don previous 5 days
    of sales
    """
    print("calculating stock data")
    new_stock_data = []                                     #empty array/list to hold the values

    for column in data:
        int_column = [int(num) for num in column]
        average = sum(int_column) / len(int_column)
        stock_num = average * 1.1
        new_stock_data.append(round(stock_num))

    return new_stock_data    


def main():
    """
    Standard practice to add our function calls 
    into a  function called main
    """
    data = get_sales_data()                                 # calling function
    sales_data =[int(num) for num in data]                  # need this new variable so can use it outside of the orignal function ??
    #update_sales_worksheet(sales_data)                      # function gets called and passes in the sales_data which needs ot be an int thats why converted above.
    update_worksheet(sales_data, "sales")
    new_surplus_data = calculate_surplus_data(sales_data)                      # why am i passing in sales_data ?????
    #update_surplus_worksheet(new_surplus_data)
    update_worksheet(new_surplus_data, "surplus")            # need this new variable so can use it outside of the orignal function ??
    print(f"new surplus data {new_surplus_data}")
    sales_columns = get_last_5_sales()
    stock_data = calculate_stock_req(sales_columns)         # when we call function we are passing in "sales_columns" result above.. 
    print(stock_data)
    update_worksheet(stock_data, "stock")   
print("Welcome to out love Sandwiches data process")


main()                                                      #note functions need to be called after the function has been written

#get_last_5_sales()

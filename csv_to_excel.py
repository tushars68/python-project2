# Import necessary library
import pandas as pd

# Function to convert CSV to Excel
def csv_to_excel(csv_file, excel_file):
    # Read the CSV file
    data = pd.read_csv(csv_file)
    
    # Save the data to an Excel file
    data.to_excel(excel_file, index=False)
    
    print(f"File converted successfully and saved as '{excel_file}'")

# Input the CSV file name and desired Excel file name
csv_file = "/Users/tusharsharma/Desktop/csv_to_xsl/data.csv"
excel_file = "output_data.xlsx"  

# Call the function to convert CSV to Excel
csv_to_excel(csv_file, excel_file)

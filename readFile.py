# ---IMPORTS---
import pdfplumber  # Used to open PDFs and extract text
import pandas as pd  # Organize data in a table and export it
import re  # Regular expressions library for pattern recognition


# ---GLOBAL VARIABLES---
PDF_PATH = "Apple Card Statement - MONTH YEAR.pdf"  # Apple Card Statement - MONTH YEAR.pdf
TRANSACTIONS = []
TARGET_CHAR = "#-$"

# ---USER DATE INPUT---
month = input("Enter the month: ").title() # Ask for the month
year = input("Enter the year: ").title() # Ask for the year
PDF_PATH = f"Apple Card Statement - {month} {year}.pdf" # Set the PDF path

# ---EXTRACT TRANSACTIONS---
with pdfplumber.open(PDF_PATH) as pdf: # Open the PDF file
    
    # Loop through each page
    print("Extracting transactions...")
    for page in pdf.pages:
        text = page.extract_text()  # Extract text from the page
        lines = text.split("\n")  # Split the text into lines

        date_pattern = r"\d{2}/\d{2}/\d{4}"  # matches MM/DD/YYYY using imported re library
        
        for line in lines:  # loop through lines
            if re.match(date_pattern, line):  # Check for date at the start
                parts = line.split()  # Split the line into parts
                
                date = parts[0]  # First part is the date

                merchant_name = []  # List to hold merchant name parts
                merchant_parts = []  # List to hold merchant address/misc parts
                
                i = 1  # index for merchant name parts
                while i < len(parts) - 3:
                    # ---Case 1 (TST* Transactions)---
                    pattern = r"^([A-Za-z]+)([0-9]+)$" # GOLF2401
                    match = re.match(pattern, parts[i])
                    
                    if match:
                        # print(parts[i] + " matches Case 1")
                        letters = match.group(1) # GOLF
                        merchant_name.append(letters)
                        
                        numbers = match.group(2) # 2401
                        merchant_parts.append(numbers)
                        break
                        
                    # ---Case 2 (Address information)---
                    if parts[i][0].isdigit() or parts[i][0] in TARGET_CHAR:
                        # print(parts[i] + " matches Case 2")
                        break  # stop at address or special character

                    # ---Case 3 (Normal word)---
                    # print(parts[i] + " matches Case 3")
                    merchant_name.append(parts[i])
                    i += 1

                merchant_name = " ".join(merchant_name)  # Join the merchant name parts into a single string
                merchant_parts = " ".join(merchant_parts + parts[i:-3])
                daily_cash_percentage = parts[-3]  # Second to last part is daily cash percentage
                daily_cash = parts[-2]  # Last part is daily cash
                amount = parts[-1]  # Last part is amount
                
                # Clean necessary dollar amount fields
                daily_cash = daily_cash.replace("$", "").replace(",", "")
                amount = amount.replace("$", "").replace(",", "")
                
                # Add transactions to the global list
                TRANSACTIONS.append([
                    # --- CHANGE ORDER OF DATA L -> R ORGANIZATION INTO EXCEL OUTPUT
                    merchant_name, date, amount, merchant_parts, daily_cash_percentage, daily_cash
                ])
                
print("Transactions parsed successfully, appending...")

# --- CONVERT TRANSACTIONS TO A DATAFRAME AND EXPORT TO EXCEL ---
print("Converting transactions to DataFrame...")
                                                    # --- CHANGE COLUMN HEADERS ACCORDDING TO TRASACTIONS ORDER ---
df = pd.DataFrame(TRANSACTIONS, columns=["Merchant Name", "Date", "Amount", "Merchant Information", "Daily Cash %", "Daily Cash"])
print("Exporting to Excel...")
df.to_excel(f"Apple Card Transactions - {month} {year}.xlsx", index=False) # Apple Card Transactions - MONTH YEAR.xlsx

# Exit the program
print("Transactions successfully extracted and saved to Excel file.")
print("Process complete.")
print("Exiting program.")
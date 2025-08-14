# ---IMPORTS---
import pdfplumber  # Used to open PDFs and extract text
import pandas as pd  # Organize data in a table and export it
import re  # Regular expressions library for pattern recognition

# ---GLOBAL VARIABLES---
pdfPath = "<---here--->"  # Apple Card Statement - MONTH YEAR.pdf
transactions = []

# Open the PDF file
with pdfplumber.open(pdfPath) as pdf:
    # Loop through each page
    for page in pdf.pages:
        text = page.extract_text()  # Extract text from the page
        lines = text.split("\n")  # Split the text into lines

        date_pattern = r"\d{2}/\d{2}/\d{4}"  # matches MM/DD/YYYY
        
        for line in lines:  # loop through lines
            if re.match(date_pattern, line):  # Check for date at the start
                parts = line.split()  # Split the line into parts
                date, *merchant_parts, amount = parts
                merchant = " ".join(merchant_parts)  # Join the merchant parts into a single string
                
                # Clean the amount
                amount = amount.replace("$", "").replace(",", "")
                
                # Add transactions to the list
                transactions.append([
                    date, merchant, amount
                ])

# Convert transactions to a DataFrame and export to Excel
df = pd.DataFrame(transactions, columns=["Date", "Merchant", "Amount"])
df.to_excel("Apple Card Transactions - MONTH YEAR.xlsx", index=False)

# Exit the program
print("Transactions successfully extracted and saved to Excel file.")
print("Process complete.")
print("Exiting program.")
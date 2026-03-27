"""
Data Science Journey - String Manipulation Lab
This study involves text processing and data validation processes 
on store data (ID, ZIP, URL).
"""

# Task 1: Type Conversion
store_id = 1101
store_id = str(store_id)

# Task 2: ZIP Code Checker
def zip_checker(zipcode):
    if len(zipcode) == 5:
        if zipcode[0:2] == '00':
            return 'Invalid ZIP Code.'
        else:
            return zipcode
    elif len(zipcode) == 4 and zipcode[0] != '0':
        return '0' + zipcode
    else:
        return 'Invalid ZIP Code.'

# Task 3: URL Slicing
url = "https://exampleURL1.com/r626c36"
# Extracts the last 7 characters (ID) from the URL
id_extracted = url[-7:]

# Task 4: URL Checker (Refactored & Fixed)
def url_checker(url):
    parts = url.split('/')
    # parts[0] is the protocol (https:), parts[-1] is the ID at the end
    protocol = parts[0]
    store_id = parts[-1]
    
    if protocol != 'https:' and len(store_id) != 7:
        print(f"Error: {protocol} is invalid and ID {store_id} length is wrong.")
        return None
    elif protocol != 'https:':
        print(f"Error: {protocol} is an invalid protocol.")
        return None
    elif len(store_id) != 7:
        print(f"Error: {store_id} is an invalid store ID.")
        return None
    else:
        # Returns the ID if everything is correct
        return store_id

# --- Example Usage (Optional for testing) ---
# print(url_checker("https://example.com/r626c36")) # Success: returns r626c36
# print(url_checker("http://example.com/r626c3"))   # Error: returns None
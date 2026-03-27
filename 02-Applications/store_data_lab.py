"""
Data Science Journey - String Manipulation Lab
Bu çalışma, mağaza verileri (ID, ZIP, URL) üzerindeki metin işlemlerini 
ve veri doğrulama (validation) süreçlerini içerir.
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
id_extracted = url[-7:]

# Task 4: URL Checker
def url_checker(url):
    parts = url.split('/')
    protocol = parts[0]
    store_id = parts[-1]
    
    if protocol != 'https:' and len(store_id) != 7:
        print(f'{protocol} is an invalid protocol.\n{store_id} is an invalid store ID.')
    elif protocol != 'https:':
        print(f'{protocol} is an invalid protocol.')
    elif len(store_id) != 7:
        print(f'{store_id} is an invalid store ID.')
    else:
        return store_id

# Testler (Opsiyonel)
if __name__ == "__main__":
    print(f"Extracted ID: {id_extracted}")
    print(f"ZIP Check (2806): {zip_checker('2806')}")
    
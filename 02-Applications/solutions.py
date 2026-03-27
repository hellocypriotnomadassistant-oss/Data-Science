from string_utils import format_price, format_user

# Calling the functions
price_result = format_price(15.756)
user_result = format_user("Ahmet", 5)

# Printing results to the console (This part is very important!)
print(price_result)
print(user_result)

from string_utils import format_price, format_user, clean_text, format_percentage

# Testing new tools
print(clean_text("   Let's See   "))
print(format_percentage(0.856))
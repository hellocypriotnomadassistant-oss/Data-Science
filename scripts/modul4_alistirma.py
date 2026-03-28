# Our Data Set (Sample data as in the course)
fruits = ["apple", "banana", "strawberry", "kiwi"]  # List
prices = (20, 30, 45, 50)                          # Tuple

print("--- Product and Price Matching (zip and enumerate) ---")
# We combined them with zip and numbered them with enumerate
for index, (fruit, price) in enumerate(zip(fruits, prices), start=1):
    print(f"{index}. {fruit} per kilo is {price} USD")

print("\n--- Discounted Prices (List Comprehension) ---")
# Creating a new list by applying a 10% discount to prices
discounted_prices = [p * 0.9 for p in prices]
print(f"New Price List: {discounted_prices}")
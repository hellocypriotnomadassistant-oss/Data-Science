"""
PYTHON DICTIONARIES: THE ULTIMATE GUIDE
--------------------------------------
A comprehensive reference for creating, managing, and using 
dictionaries in Python for Data Science and Web Development.
"""

# 1. CREATING DICTIONARIES
# Method 1: Using curly braces {} - Most common
smallest_countries = {
    'Africa': 'Seychelles',
    'Asia': 'Maldives',
    'Europe': 'Vatican City'
}

# Method 2: Using the dict() constructor
# Note: Keys are passed as keywords (no quotes), spaces not allowed.
capitals = dict(France='Paris', Italy='Rome', Germany='Berlin')

# Creating an empty dictionary
empty_dict = {} 
# or 
empty_dict_alt = dict()


# 2. KEY AND VALUE RULES (CRITICAL)
# Keys: Must be IMMUTABLE (string, int, float, tuple).
# Values: Can be ANYTHING (lists, other dictionaries, etc.).
# Rule: One key can only point to one object. 

data_sample = {
    'numbers': [1, 2, 3],  # Correct: Value is a list
    'status': True,
    'metadata': {'id': 101, 'source': 'API'} # Nested dictionary
}


# 3. ACCESSING AND MODIFYING DATA
# Accessing by Key (No indexing!)
print(f"Smallest in Africa: {smallest_countries['Africa']}")

# Adding/Updating Data (Dictionaries are MUTABLE)
smallest_countries['North_America'] = 'Saint Kitts and Nevis'
smallest_countries['Asia'] = 'Maldives' # Updates existing key


# 4. ESSENTIAL METHODS (THE POWER TOOLS)
print("\n--- Dictionary Methods ---")

# .keys() -> Returns a View Object of all keys
print(f"Regions: {smallest_countries.keys()}")

# .values() -> Returns a View Object of all values
print(f"Countries: {smallest_countries.values()}")

# .items() -> Returns Key-Value pairs (Perfect for loops)
print("\n--- Iterating with .items() ---")
for region, country in smallest_countries.items():
    print(f"Region: {region} | Country: {country}")


# 5. USEFUL OPERATIONS
# Checking if a key exists (Used heavily in data analysis)
if 'Europe' in smallest_countries:
    print("\n'Europe' key is present.")

# Deleting a key
del smallest_countries['North_America']


# 6. WHY IT MATTERS (THE BIG PICTURE)
"""
- FOUNDATION: The primary structure for data manipulation in Data Science.
- JSON COMPATIBILITY: Matches the structure of JSON, the language of the web/APIs.
- VIEW OBJECTS: keys(), values(), and items() reflect real-time changes 
  made to the dictionary (they are not static lists).
"""

print("\nGuide successfully executed.")
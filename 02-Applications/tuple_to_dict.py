"""
TUPLE LIST TO DICTIONARY CONVERSION
-----------------------------------
This script demonstrates how to transform a list of tuples into a 
structured dictionary for better data organization and accessibility.
"""

# 1. Initial Data: A list of tuples (Name, Age, Position)
team_data = [
    ("Alice", 25, "Forward"),
    ("Bob", 28, "Defender"),
    ("Charlie", 22, "Midfielder"),
    ("David", 30, "Forward"),
    ("Eve", 24, "Defender")
]

# 2. Transformation Logic
# Purpose: Organize players by their positions (Keys: Position, Values: List of Players)
new_team = {}

for name, age, position in team_data:
    # Conditional Logic: If position key exists, append to the list. 
    # Otherwise, create a new list for that key.
    if position in new_team:
        new_team[position].append((name, age))
    else:
        new_team[position] = [(name, age)]

# 3. Displaying Results
print("--- Organized Team Dictionary ---")
print(new_team)

# 4. Dictionary Methods for Data Analysis
print("\n--- Key Dictionary Methods ---")

# Accessing Keys (Positions)
print(f"Positions (Keys): {list(new_team.keys())}")

# Accessing Values (Player Info)
print(f"Player Data (Values): {list(new_team.values())}")

# Iterating with .items() for clean output
print("\n--- Detailed Team Roster ---")
for position, players in new_team.items():
    print(f"Position: {position}")
    for player in players:
        print(f"  - Name: {player[0]}, Age: {player[1]}")

"""
CRITICAL RULES & WHY IT MATTERS:
- Keys are unique and immutable (Positions in this case).
- Values can be any data type (Lists of tuples here).
- Efficiency: Dictionaries allow for very fast data retrieval.
- Scalability: Essential for organizing large datasets in Data Science.
"""

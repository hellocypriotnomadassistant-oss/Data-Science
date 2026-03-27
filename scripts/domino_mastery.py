# --- 1 & 5. LIST OF TUPLES AND ACCESSING ---
# Storing player data in a list of tuples (Name, Age, Position)
players = [
    ("Alice", 25, "Guard"),
    ("Bob", 28, "Forward"),
    ("Charlie", 22, "Center")
]

print("--- 1. Player Positions (Tuple Unpacking) ---")
player_info = []
# Unpacking: 3 variables for 3 elements in the tuple
for name, age, position in players:
    # --- 2. STRING FORMATTING ---
    player_info.append(f"{name} plays as {position}")

for info in player_info:
    print(info)

print("\n--- 3 & 4. DOMINOES (Nested Loops & end=' ') ---")
dominoes = []
# Creating combinations 0-6
for left in range(7):
    for right in range(left, 7): # 'left' starts to avoid duplicates like (1,0) after (0,1)
        dominoes.append((left, right))
        print(f"[{left}|{right}]", end=" ") # Using end=" " to stay on the same line

print(f"\n\nTotal dominoes created: {len(dominoes)}")

# --- 5. ACCESSING NESTED DATA ---
# Accessing the 5th domino (index 4) and its 2nd value (index 1)
sample_value = dominoes[4][1]
print(f"The 2nd value of the 5th domino is: {sample_value}")

# --- 6. LIST COMPREHENSION ---
# Summing the dots on each domino in a single, elegant line
total_pips = [pip[0] + pip[1] for pip in dominoes]
print(f"Sum of dots for the first 5 dominoes: {total_pips[:5]}")
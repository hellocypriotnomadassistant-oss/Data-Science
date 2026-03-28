"""
LAB REPORT: AIR QUALITY INDEX (AQI) ANALYSIS
--------------------------------------------
A practical application of Dictionaries and Sets using 
Environmental Protection Agency (EPA) data.
"""

# TASK 1: DATA PREPARATION & DICTIONARY CREATION
# Sample data representing States, Counties, and their AQI values
state_list = ['Arizona', 'California', 'California', 'Vermont', 'Vermont', 'Arizona']
county_list = ['Maricopa', 'Alameda', 'Sacramento', 'Chittenden', 'Chittenden', 'Pima']
aqi_list = [18.0, 11.0, 8.0, 18.0, 20.0, 15.0]

# Combining lists into a list of tuples using zip()
aqi_tuples = list(zip(state_list, county_list, aqi_list))

# Building the aqi_dict: {State: [(County, AQI), ...]}
aqi_dict = {}
for state, county, aqi in aqi_tuples:
    if state in aqi_dict:
        aqi_dict[state].append((county, aqi))
    else:
        aqi_dict[state] = [(county, aqi)]

print("--- AQI Dictionary Created ---")
print(f"Arizona Records: {aqi_dict.get('Arizona')}")


# TASK 2: DATA EXTRACTION & ANALYSIS
# Calculating mean AQI for a specific state (e.g., California)
if 'California' in aqi_dict:
    ca_aqis = [aqi for county, aqi in aqi_dict['California']]
    mean_ca_aqi = sum(ca_aqis) / len(ca_aqis)
    print(f"\nMean AQI for California: {mean_ca_aqi:.2f}")


# TASK 3: DYNAMIC ANALYSIS WITH FUNCTIONS
def county_counter(state):
    """Counts AQI readings for each county in a given state."""
    county_counts = {}
    # .get(state, []) prevents errors if state is not found
    for county, aqi in aqi_dict.get(state, []):
        county_counts[county] = county_counts.get(county, 0) + 1
    return county_counts

print(f"\nCounty Counts for Arizona: {county_counter('Arizona')}")


# TASK 4: USING SETS TO FIND DUPLICATE COUNTY NAMES
# Collecting all county names from across all states
all_counties = []
for state in aqi_dict:
    all_counties.extend(county_counter(state).keys())

# Using set() to find unique names and calculate duplicates
unique_counties = set(all_counties)
duplicate_count = len(all_counties) - len(unique_counties)

print(f"\nTotal County Records: {len(all_counties)}")
print(f"Unique County Names: {len(unique_counties)}")
print(f"Number of Duplicate County Names across States: {duplicate_count}")


# KEY TAKEAWAYS:
"""
- TUPLES: Ideal for immutable data records (State, County, AQI).
- DICTIONARIES: Efficient for grouping data and fast key-based lookups.
- SETS: Perfect for removing duplicates and analyzing uniqueness.
- FUNCTIONS: Create modular, reusable code for large datasets.
"""
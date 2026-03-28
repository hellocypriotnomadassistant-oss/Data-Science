"""
LAB: AIR QUALITY DATA ANALYSIS (EPA)
------------------------------------
Objective: Practice using Dictionaries and Sets for data storage, 
manipulation, and analysis using real-world Environmental Protection Agency data.
"""

# SAMPLE DATA PREPARATION
state_list = ['Arizona', 'California', 'California', 'Vermont', 'Vermont', 'Arizona', 'Pennsylvania', 'Indiana']
county_list = ['Maricopa', 'Alameda', 'Sacramento', 'Chittenden', 'Chittenden', 'Pima', 'Washington', 'Marion']
aqi_list = [18.0, 11.0, 8.0, 18.0, 20.0, 15.0, 7.0, 12.0]

# TASK 1: DICTIONARY CREATION
# 1a. Creating a list of tuples using zip()
# Structure: (state, county, aqi)
epa_tuples = list(zip(state_list, county_list, aqi_list))

# 1b. Creating the aqi_dict
# Key: State | Value: List of (County, AQI) tuples
aqi_dict = {}
for state, county, aqi in epa_tuples:
    if state in aqi_dict:
        aqi_dict[state].append((county, aqi))
    else:
        aqi_dict[state] = [(county, aqi)]

print("--- Task 1: Dictionary Created ---")
print(f"Arizona Records: {aqi_dict.get('Arizona')}\n")


# TASK 2: DATA EXTRACTION
# 2a. Record count for Arizona
print(f"Number of readings in Arizona: {len(aqi_dict.get('Arizona', []))}")

# 2b. Average AQI for California
if 'California' in aqi_dict:
    ca_aqi_list = [aqi for county, aqi in aqi_dict['California']]
    ca_aqi_mean = sum(ca_aqi_list) / len(ca_aqi_list)
    print(f"California Average AQI: {ca_aqi_mean:.2f}\n")


# TASK 3: COUNTY COUNTER FUNCTION
def county_counter(state):
    """Returns a dictionary with the count of readings for each county in a state."""
    county_dict = {}
    for county, aqi in aqi_dict.get(state, []):
        if county in county_dict:
            county_dict[county] += 1
        else:
            county_dict[county] = 1
    return county_dict

# Example: Washington County in Pennsylvania
pa_counties = county_counter('Pennsylvania')
print(f"Readings for Washington, PA: {pa_counties.get('Washington', 0)}")


# TASK 4: ANALYZING SHARED COUNTY NAMES WITH SETS
# 4a. Collecting all county names
all_counties = []
for state in aqi_dict.keys():
    counties = list(county_counter(state).keys())
    all_counties += counties

# 4b. Finding shared (duplicate) county names using set()
unique_counties = set(all_counties)
shared_count = 0
for county in unique_counties:
    if all_counties.count(county) > 1:
        shared_count += all_counties.count(county)

print(f"\n--- Task 4: Set Analysis ---")
print(f"Total County Records: {len(all_counties)}")
print(f"Unique County Names: {len(unique_counties)}")
print(f"Shared County Count (Names appearing in multiple states): {shared_count}")


# KEY HIGHLIGHTS:
"""
- DICTIONARIES: Perfect for mapping keys (States) to complex values (Lists of Tuples).
- SETS: Essential for identifying unique items and finding overlaps/duplicates.
- FUNCTIONS: county_counter() makes data analysis modular and reusable.
"""
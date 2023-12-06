'''
This script is used to create a mapping between the RMP data and the Board of Education data.
'''

import csv
from fuzzywuzzy import process


schools_path = '../data/school.csv'
boe_path = '../data/Most-Recent-Cohorts-Institution.csv'

# From the school.csv file, read in the school id and school name
schools = {}
with open(schools_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        schools[row['School ID']] = row['School Name'].lower()

# From the Most-Recent-Cohorts-Institution.csv file, read in the school id and name
boe = {}
with open(boe_path, 'r') as f:
    reader = csv.DictReader(f)
    for row in reader:
        boe[row['UNITID']] = row['INSTNM'].lower()

# Create a new file with the mapping
with open('../data/rmp_board_of_ed_mapping.csv', 'w') as f:
    # Write the header row
    writer = csv.writer(f)
    writer.writerow(['RMP School ID','Board of Education School ID'])

    # Write the mapping rows with fuzzy matching
    for school_id, school_name in schools.items():
        # Find the best match for school_name in boe values
        best_match, similarity = process.extractOne(school_name, boe.values())
        # You can adjust the threshold based on how close a match you want
        if similarity > 95:  # Assuming a similarity threshold of 95%
            # Find the key (boe_id) for the matched value (best_match)
            boe_id = next(key for key, value in boe.items() if value == best_match)
            writer.writerow([school_id, boe_id])
    
print("Mapping created and saved as 'rmp_board_of_ed_mapping.csv'")

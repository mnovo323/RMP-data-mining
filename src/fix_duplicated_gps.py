import csv

# Input and output file paths
input_file = '../data/schools_gps.csv'
output_file = '../data/schools_gps_modified.csv'

# Initialize variables to store the previous latitude and longitude
prev_lat = None
prev_lng = None

# Open the input CSV file for reading and the output CSV file for writing
with open(input_file, 'r') as input_csv, open(output_file, 'w', newline='') as output_csv:
    reader = csv.DictReader(input_csv)
    fieldnames = reader.fieldnames
    writer = csv.DictWriter(output_csv, fieldnames=fieldnames)
    writer.writeheader()

    for row in reader:
        # Check if latitude and longitude are equal to the previous row
        if row['lat'] == prev_lat and row['lng'] == prev_lng:
            # Replace with 0,0
            row['lat'] = '0'
            row['lng'] = '0'

        # Store the current latitude and longitude for the next iteration
        prev_lat = row['lat']
        prev_lng = row['lng']

        # Write the modified row to the output file
        writer.writerow(row)

print("Replacement completed. Modified data saved to 'schools_gps_modified.csv'")

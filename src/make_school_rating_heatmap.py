import folium
import pandas as pd
from branca.colormap import LinearColormap

ratings_data = pd.read_csv('../data/school_rating_distribution.csv')
# filter schools with less than 10 ratings
ratings_data = ratings_data[ratings_data['Total Ratings'] >= 10]

# Load your latitude and longitude data CSV
latlong_data = pd.read_csv('../data/schools_gps_modified.csv')

# Merge the two DataFrames on the 'School ID' column
merged_data = pd.merge(ratings_data, latlong_data, on='School ID')

# Create a linear color map for the gradient (adjust colors as needed)
color_map = LinearColormap(['red', 'yellow', 'green', 'blue'], vmin=0, vmax=5)

# Create a map centered around the first school's coordinates
m = folium.Map(location=[merged_data['lat'].iloc[0], merged_data['lng'].iloc[0]], zoom_start=10)

# Add markers for each school with a color gradient based on ratings
for index, row in merged_data.iterrows():
    rating = row['Average Rating']
    lat = row['lat']
    lng = row['lng']
    
    # Get the color from the color map based on the rating
    color = color_map(rating)
    
    # Create a marker and add it to the map
    folium.CircleMarker(
        location=[lat, lng],
        radius=5,
        color=color,
        fill=True,
        fill_color=color,
        fill_opacity=0.7,
        popup=f"School ID: {row['School ID']}, Rating: {rating}"
    ).add_to(m)

# Add the color map to the map legend
color_map.add_to(m)

# Save the map to an HTML file
m.save('../output/school_ratings_map.html')

print("Map created and saved as 'school_ratings_map.html'")

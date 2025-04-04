#  Crime Data Analysis & Heatmap with FireDucks 
import fireducks as fd
import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt

# 🔹 Simulated Crime Data (Replace with real NCRB data)
data = {
    "City": ["Delhi", "Mumbai", "Bangalore", "Chennai", "Kolkata"],
    "Latitude": [28.6139, 19.0760, 12.9716, 13.0827, 22.5726],
    "Longitude": [77.2090, 72.8777, 77.5946, 80.2707, 88.3639],
    "Crime Type": ["Theft", "Murder", "Assault", "Cybercrime", "Fraud"],
    "Year": [2020, 2021, 2022, 2023, 2024]
}

# 🔹 Convert to FireDucks DataFrame
df = fd.DataFrame(data)

# 🔹 EDA: Crime Count by City
top_cities = df["City"].value_counts()
print("\n🔹 Crime Count by City:")
print(top_cities)

# 🔹 Crime Trends Over Time
plt.figure(figsize=(8, 4))
df["Year"].value_counts().sort_index().plot(kind="bar", color="red")
plt.title("Crime Trends (2020-2024)")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.show()

# 🔹 Generate Interactive Heatmap
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
heat_data = df[["Latitude", "Longitude"]].to_numpy().tolist()
HeatMap(heat_data, radius=10).add_to(india_map)

# 🔹 Save Heatmap
india_map.save("india_crime_heatmap.html")
print("\n Crime Heatmap Saved as 'india_crime_heatmap.html'")

# Import necessary libraries
import pandas as pd
import fireducks.pandas as fpd
import folium
from folium.plugins import HeatMap
import matplotlib.pyplot as plt

# Simulated Crime Data
data = {
    "City": ["Delhi", "Delhi", "Delhi", "Mumbai", "Mumbai", "Mumbai",
             "Bangalore", "Bangalore", "Bangalore", "Chennai", "Chennai",
             "Chennai", "Kolkata", "Kolkata", "Kolkata"],
    "Crime Type": ["Theft", "Murder", "Assault", "Cybercrime", "Theft",
                   "Assault", "Fraud", "Theft", "Assault", "Murder",
                   "Fraud", "Assault", "Fraud", "Murder", "Cybercrime"],
    "Year": [2020, 2020, 2021, 2020, 2021, 2022, 2020, 2021, 2022,
             2020, 2021, 2022, 2020, 2021, 2022],
    "Crime Count": [120, 25, 65, 45, 90, 100, 30, 50, 80, 40, 60,
                    70, 35, 55, 65],
    "Latitude": [28.6139, 28.6139, 28.6139, 19.0760, 19.0760, 19.0760,
                 12.9716, 12.9716, 12.9716, 13.0827, 13.0827, 13.0827,
                 22.5726, 22.5726, 22.5726],
    "Longitude": [77.2090, 77.2090, 77.2090, 72.8777, 72.8777, 72.8777,
                  77.5946, 77.5946, 77.5946, 80.2707, 80.2707, 80.2707,
                  88.3639, 88.3639, 88.3639]
}

# Create a pandas DataFrame
df_pandas = pd.DataFrame(data)

# Convert pandas DataFrame to FireDucks DataFrame
df = fpd.from_pandas(df_pandas)

# EDA: Crime Count by City
top_cities = df["City"].value_counts()
print("\n🔹 Crime Count by City:")
print(top_cities)

# Crime Trends Over Time
crime_trends = df.groupby('Year')['Crime Type'].count()
crime_trends.plot(kind='bar', figsize=(10, 5), color='red')
plt.title("Crime Trends (2020-2024)")
plt.xlabel("Year")
plt.ylabel("Number of Crimes")
plt.show()

# Generate Interactive Heatmap
india_map = folium.Map(location=[20.5937, 78.9629], zoom_start=5)
heat_data = df[['Latitude', 'Longitude']].to_pandas().to_numpy().tolist()
HeatMap(heat_data, radius=10).add_to(india_map)

# Save Heatmap
india_map.save("india_crime_heatmap.html")
print("\nCrime Heatmap Saved as 'india_crime_heatmap.html'")

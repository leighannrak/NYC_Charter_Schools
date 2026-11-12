"""
Filter for charter schools in the following counties:Bronx, Brooklyn, New York, Queens, and Richmond.
Join each school to its physical address using Institution ID.
Return a dataset containing NYC charter schools with: School name, Address, Latitude, Longitude.
Then create a map of NYC charter schools with markers for each.

Requirements:
    pip install pandas openpyxl folium
"""

import pandas as pd
import folium

# 1. Load datasets
df1 = pd.read_excel("NYC_Charter_Schools_Directory.xlsx", header=1, dtype=str)
print(df1.columns.tolist())
df2 = pd.read_csv("NYC_Charter_Schools_Address.csv", dtype=str)
print(df2.columns.tolist())

# 2. Filter for schools in the specified counties
counties = ["Bronx", "Brooklyn", "New York", "Queens", "Richmond"]
school_list = df1[df1["County"].isin(counties)]

# 3. Select key columns from both dataset
school_list = school_list[["Institution ID", "Charter School Name", "County"]]
df2 = df2[["Institution ID", "GIS Longitute (X)",  "GIS Latitude (Y)"]]


# 4. Merge datasets using Institution ID
merged = pd.merge(
    school_list,
    df2,
    on="Institution ID",
    how="inner"
)
print(merged.columns.tolist())

# 5. Check matching results
print("Total schools:", len(merged))

# 6. Export consolidated dataset
merged.drop(columns=["Institution ID", "Charter School Name", "County", "GIS Longitute (X)", "GIS Latitude (Y)"]).to_csv(
    "consolidated_schools.csv",
    index=False
)

print("Files successfully exported!")

# 8. Create NYC map
api_key = "cb1_57ro_1_3e9bacb7f11d8edc851444e6"
tiles = (
    f"https://basemaps.cartocdn.com/"
    f"rastertiles/light_all/{{z}}/{{x}}/{{y}}.png?key={api_key}"
)

m = folium.Map(
    location=[40.7128, -74.0060],
    zoom_start=11,
    tiles=tiles,
    attr="© OpenStreetMap contributors © CARTO"
)

# 9. Add school markers
for _, school in merged.iterrows():
    folium.Marker(
        location=[school["GIS Latitude (Y)"], school["GIS Longitute (X)"]],
        popup=f'{school["Charter School Name"]} - {school["County"]}',
        tooltip=school["Charter School Name"]
    ).add_to(m)

# Save interactive map
m.save("index.html")

print("Map created successfully!")


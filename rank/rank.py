import geopandas as gpd
import matplotlib.pyplot as plt

gdf = gpd.read_file('rank.geojson')

gdf = gdf[gdf['country'] == 'United States']
gdf = gdf.sort_values(by='national_rank')

top_10_us_universities = gdf.head(10)

top_10_us_universities = top_10_us_universities.to_crs('epsg:4326')

fig, ax = plt.subplots(figsize=(12, 6))
top_10_us_universities.plot(column='national_rank', cmap='coolwarm', linewidth=0.8, ax=ax, legend=True)

for x, y, label in zip(top_10_us_universities.geometry.centroid.x, top_10_us_universities.geometry.centroid.y, top_10_us_universities['university_name']):
    ax.text(x, y, label, fontsize=8, ha='left')

ax.set_title('Top 10 Universities in the USA by National Ranking')
plt.show()

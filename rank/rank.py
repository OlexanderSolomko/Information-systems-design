import geopandas as gpd
import matplotlib.pyplot as plt

def load_and_filter_data(file_path, country):
    gdf = gpd.read_file(file_path)
    return gdf[gdf['country'] == country]
#changes for commit
def plot_top_n_universities(gdf, n=10, crs='epsg:4326', figsize=(12, 6), cmap='coolwarm'):
    top_n_universities = gdf.sort_values(by='national_rank').head(n)
    top_n_universities = top_n_universities.to_crs(crs)

    fig, ax = plt.subplots(figsize=figsize)
    top_n_universities.plot(column='national_rank', cmap=cmap, linewidth=0.8, ax=ax, legend=True)

    for x, y, label in zip(top_n_universities.geometry.centroid.x, top_n_universities.geometry.centroid.y, top_n_universities['university_name']):
        ax.text(x, y, label, fontsize=8, ha='left')

    ax.set_title(f'Top {n} Universities in the USA by National Ranking')
    plt.show()

if __name__ == "__main__":
    file_path = 'rank.geojson'
    target_country = 'United States'

    universities_data = load_and_filter_data(file_path, target_country)
    plot_top_n_universities(universities_data)

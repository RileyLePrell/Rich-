import geopandas as gpd

# Load the shapefile
shapefile_path = "Parcel_TaxData.shp"  # Update with your file path
gdf = gpd.read_file(shapefile_path)

# View all column names
print(gdf.columns)

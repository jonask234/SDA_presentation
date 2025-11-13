#!/usr/bin/env python3
"""
Interactive Web Map Creator for Hsinchu City
Creates an HTML map you can open in your browser and interact with!
"""

import sys
import subprocess

def install_packages():
    """Install required packages"""
    packages = ['geopandas', 'folium', 'mapclassify']
    print("Installing required packages for interactive map...")
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '-q'])
    print("✓ Packages ready!\n")

install_packages()

import geopandas as gpd
import folium
from folium import Choropleth, GeoJson
import json

print("=" * 60)
print("🗺️  INTERACTIVE MAP CREATOR - HSINCHU CITY")
print("=" * 60)

# Load shapefile
print("\n📂 Loading shapefile...")
gdf = gpd.read_file('Hsinchu_City.shp')

# Convert to WGS84 (required for web maps)
if gdf.crs != 'EPSG:4326':
    print("🔄 Converting to WGS84 coordinate system...")
    gdf = gdf.to_crs('EPSG:4326')

# Calculate derived variables
print("🔢 Calculating statistics...")
gdf['income_per_capita'] = gdf['INCOME'] / gdf['POPULATION']
gdf['education_rate'] = (gdf['TERTIARY'] / gdf['POPULATION']) * 100
gdf['indigenous_ratio'] = (gdf['INDIGENOUS'] / gdf['POPULATION']) * 100

# Create the base map centered on Hsinchu
center_lat = gdf.geometry.centroid.y.mean()
center_lon = gdf.geometry.centroid.x.mean()

print(f"🎯 Map center: ({center_lat:.4f}, {center_lon:.4f})")

# Create interactive map
print("\n🎨 Creating interactive map...")
m = folium.Map(
    location=[center_lat, center_lon],
    zoom_start=12,
    tiles='OpenStreetMap'
)

# Add different tile layers
folium.TileLayer('CartoDB positron', name='Light Mode').add_to(m)
folium.TileLayer('CartoDB dark_matter', name='Dark Mode').add_to(m)

# Create income choropleth
print("💰 Adding income layer...")
Choropleth(
    geo_data=gdf.to_json(),
    name='Income Per Capita',
    data=gdf,
    columns=['VILLCODE', 'income_per_capita'],
    key_on='feature.properties.VILLCODE',
    fill_color='RdYlGn',
    fill_opacity=0.7,
    line_opacity=0.5,
    legend_name='Income Per Capita (1000 TWD)',
    highlight=True
).add_to(m)

# Add tooltips with detailed information
print("📝 Adding village information tooltips...")
style_function = lambda x: {
    'fillColor': '#ffffff',
    'color': '#000000',
    'fillOpacity': 0.1,
    'weight': 0.5
}

highlight_function = lambda x: {
    'fillColor': '#000000',
    'color': '#000000',
    'fillOpacity': 0.3,
    'weight': 2
}

# Prepare tooltip fields
gdf['tooltip_html'] = gdf.apply(lambda row: f"""
<div style="font-family: Arial; font-size: 12px;">
    <b style="font-size: 14px; color: #2c3e50;">{row['VILLNAME']}</b><br>
    <b>District:</b> {row['TOWNNAME']}<br>
    <hr style="margin: 5px 0;">
    <b>Income/Capita:</b> {row['income_per_capita']:,.0f} TWD<br>
    <b>Population:</b> {row['POPULATION']:,.0f}<br>
    <b>Households:</b> {row['HOUSEHOLD']:,.0f}<br>
    <b>Education Rate:</b> {row['education_rate']:.1f}%<br>
    <b>Aging Index:</b> {row['AgingIndex']:.1f}<br>
    <b>Pop. Density:</b> {row['POP_DENS']:,.0f}/km²
</div>
""", axis=1)

# Add GeoJson layer with tooltips
tooltip_layer = folium.GeoJson(
    gdf,
    style_function=style_function,
    highlight_function=highlight_function,
    tooltip=folium.GeoJsonTooltip(
        fields=['VILLNAME', 'TOWNNAME', 'income_per_capita', 'POPULATION', 'education_rate', 'AgingIndex'],
        aliases=['Village:', 'District:', 'Income/Capita (1000 TWD):', 'Population:', 'Education Rate (%):', 'Aging Index:'],
        localize=True,
        sticky=True,
        labels=True,
        style="""
            background-color: white;
            border: 2px solid black;
            border-radius: 3px;
            box-shadow: 3px;
        """,
        max_width=300,
    ),
    name='Village Information'
)
tooltip_layer.add_to(m)

# Add markers for top/bottom income villages
print("📍 Adding markers for extreme values...")
top5 = gdf.nlargest(5, 'income_per_capita')
bottom5 = gdf.nsmallest(5, 'income_per_capita')

# High income markers
for idx, row in top5.iterrows():
    centroid = row.geometry.centroid
    folium.Marker(
        location=[centroid.y, centroid.x],
        popup=f"<b>{row['VILLNAME']}</b><br>Income: {row['income_per_capita']:,.0f} TWD",
        tooltip=f"HIGH: {row['VILLNAME']}",
        icon=folium.Icon(color='green', icon='arrow-up', prefix='fa')
    ).add_to(m)

# Low income markers
for idx, row in bottom5.iterrows():
    centroid = row.geometry.centroid
    folium.Marker(
        location=[centroid.y, centroid.x],
        popup=f"<b>{row['VILLNAME']}</b><br>Income: {row['income_per_capita']:,.0f} TWD",
        tooltip=f"LOW: {row['VILLNAME']}",
        icon=folium.Icon(color='red', icon='arrow-down', prefix='fa')
    ).add_to(m)

# Add layer control
folium.LayerControl().add_to(m)

# Add title
title_html = '''
<div style="position: fixed;
            top: 10px; left: 50px; width: 400px; height: 90px;
            background-color: white; border:2px solid grey; z-index:9999;
            font-size:14px; padding: 10px; opacity: 0.9;">
    <h3 style="margin: 0; color: #2c3e50;">Hsinchu City Income Analysis</h3>
    <p style="margin: 5px 0; font-size: 12px;">
        <b>🟢 Green markers:</b> Highest income villages<br>
        <b>🔴 Red markers:</b> Lowest income villages<br>
        <b>💡 Hover over villages</b> for detailed information
    </p>
</div>
'''
m.get_root().html.add_child(folium.Element(title_html))

# Save the map
output_file = 'hsinchu_interactive_map.html'
m.save(output_file)

print("\n" + "=" * 60)
print("✅ INTERACTIVE MAP CREATED!")
print("=" * 60)
print(f"\n📁 Saved as: {output_file}")
print("\n🌐 TO VIEW YOUR MAP:")
print(f"   Open '{output_file}' in your web browser")
print("\n✨ FEATURES:")
print("   • Hover over villages to see detailed information")
print("   • Click markers to see income values")
print("   • Use layer control (top-right) to switch views")
print("   • Zoom and pan to explore the data")
print("   • Green markers = highest income villages")
print("   • Red markers = lowest income villages")
print("\n🎉 Enjoy exploring your data interactively!")

# Print summary statistics
print("\n" + "=" * 60)
print("📊 QUICK STATISTICS")
print("=" * 60)
print(f"Villages: {len(gdf)}")
print(f"Districts: {', '.join(gdf['TOWNNAME'].unique())}")
print(f"Income Range: {gdf['income_per_capita'].min():.0f} - {gdf['income_per_capita'].max():.0f} TWD")
print(f"Average Income: {gdf['income_per_capita'].mean():.0f} TWD")

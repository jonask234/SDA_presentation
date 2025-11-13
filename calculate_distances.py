#!/usr/bin/env python3
"""
Calculate Distance Variables for Hsinchu Analysis
- Distance to Hsinchu Science Park
- Distance to Hsinchu Air Base

This script adds these spatial variables to your shapefile data
for regression analysis.
"""

import geopandas as gpd
import pandas as pd
import numpy as np
from shapely.geometry import Point

print("=" * 70)
print("CALCULATING DISTANCE VARIABLES FOR HSINCHU INCOME ANALYSIS")
print("=" * 70)

# Load the shapefile
print("\n📂 Loading Hsinchu_City.shp...")
gdf = gpd.read_file('Hsinchu_City.shp')
print(f"✓ Loaded {len(gdf)} villages")
print(f"✓ Current CRS: {gdf.crs}")

# Ensure we're in a projected CRS for accurate distance calculation
# TWD97 / TM2 zone 121 (EPSG:3826) is appropriate for Taiwan
if gdf.crs != 'EPSG:3826':
    print("\n🔄 Converting to TWD97 TM2 (EPSG:3826) for accurate distance calculation...")
    gdf = gdf.to_crs('EPSG:3826')
    print("✓ Conversion complete")

# Key locations in Hsinchu (coordinates in WGS84 - will be converted)

# 1. Hsinchu Science Park (Main Gate / Central Location)
# Located near East District, Hsinchu City
# Approximate coordinates: 24.7935° N, 120.9964° E
SCIENCE_PARK_LAT = 24.7935
SCIENCE_PARK_LON = 120.9964

# 2. Hsinchu Air Base (新竹空軍基地)
# Located in North District, Hsinchu City
# Approximate coordinates: 24.8180° N, 120.9394° E
AIRBASE_LAT = 24.8180
AIRBASE_LON = 120.9394

print("\n" + "=" * 70)
print("KEY LOCATIONS")
print("=" * 70)
print(f"Hsinchu Science Park: {SCIENCE_PARK_LAT}°N, {SCIENCE_PARK_LON}°E")
print(f"Hsinchu Air Base:     {AIRBASE_LAT}°N, {AIRBASE_LON}°E")

# Create Point geometries for key locations (in WGS84)
science_park_point_wgs = Point(SCIENCE_PARK_LON, SCIENCE_PARK_LAT)
airbase_point_wgs = Point(AIRBASE_LON, AIRBASE_LAT)

# Create GeoDataFrame for these points
locations_gdf = gpd.GeoDataFrame(
    {'name': ['Science Park', 'Airbase'],
     'geometry': [science_park_point_wgs, airbase_point_wgs]},
    crs='EPSG:4326'  # WGS84
)

# Convert to same CRS as villages
locations_gdf = locations_gdf.to_crs('EPSG:3826')
science_park_point = locations_gdf[locations_gdf['name'] == 'Science Park'].geometry.iloc[0]
airbase_point = locations_gdf[locations_gdf['name'] == 'Airbase'].geometry.iloc[0]

print("\n" + "=" * 70)
print("CALCULATING DISTANCES")
print("=" * 70)

# Calculate centroids for each village
print("\n📍 Calculating village centroids...")
gdf['centroid'] = gdf.geometry.centroid

# Calculate distances (in meters)
print("📏 Calculating distance to Science Park...")
gdf['dist_to_science_park_m'] = gdf['centroid'].distance(science_park_point)
gdf['dist_to_science_park_km'] = gdf['dist_to_science_park_m'] / 1000

print("📏 Calculating distance to Air Base...")
gdf['dist_to_airbase_m'] = gdf['centroid'].distance(airbase_point)
gdf['dist_to_airbase_km'] = gdf['dist_to_airbase_m'] / 1000

print("✓ Distance calculations complete")

# Calculate other derived variables
print("\n🔢 Calculating derived socioeconomic variables...")
gdf['income_per_capita'] = gdf['INCOME'] / gdf['POPULATION']
gdf['education_rate'] = (gdf['TERTIARY'] / gdf['POPULATION']) * 100
gdf['indigenous_ratio'] = (gdf['INDIGENOUS'] / gdf['POPULATION']) * 100

# Summary statistics
print("\n" + "=" * 70)
print("DISTANCE SUMMARY STATISTICS")
print("=" * 70)

print("\n📊 Distance to Hsinchu Science Park:")
print(f"   Mean:     {gdf['dist_to_science_park_km'].mean():6.2f} km")
print(f"   Median:   {gdf['dist_to_science_park_km'].median():6.2f} km")
print(f"   Min:      {gdf['dist_to_science_park_km'].min():6.2f} km")
print(f"   Max:      {gdf['dist_to_science_park_km'].max():6.2f} km")
print(f"   Std Dev:  {gdf['dist_to_science_park_km'].std():6.2f} km")

print("\n📊 Distance to Air Base:")
print(f"   Mean:     {gdf['dist_to_airbase_km'].mean():6.2f} km")
print(f"   Median:   {gdf['dist_to_airbase_km'].median():6.2f} km")
print(f"   Min:      {gdf['dist_to_airbase_km'].min():6.2f} km")
print(f"   Max:      {gdf['dist_to_airbase_km'].max():6.2f} km")
print(f"   Std Dev:  {gdf['dist_to_airbase_km'].std():6.2f} km")

# Identify closest villages
print("\n" + "=" * 70)
print("CLOSEST VILLAGES TO KEY LOCATIONS")
print("=" * 70)

print("\n🏢 Top 5 Villages Closest to Science Park:")
closest_sp = gdf.nsmallest(5, 'dist_to_science_park_km')[
    ['VILLNAME', 'TOWNNAME', 'dist_to_science_park_km', 'income_per_capita']
]
for idx, row in closest_sp.iterrows():
    print(f"   {row['VILLNAME']:15s} ({row['TOWNNAME']:5s}): {row['dist_to_science_park_km']:5.2f} km, "
          f"Income: {row['income_per_capita']:6.0f}")

print("\n✈️ Top 5 Villages Closest to Air Base:")
closest_ab = gdf.nsmallest(5, 'dist_to_airbase_km')[
    ['VILLNAME', 'TOWNNAME', 'dist_to_airbase_km', 'income_per_capita']
]
for idx, row in closest_ab.iterrows():
    print(f"   {row['VILLNAME']:15s} ({row['TOWNNAME']:5s}): {row['dist_to_airbase_km']:5.2f} km, "
          f"Income: {row['income_per_capita']:6.0f}")

# Correlation analysis
print("\n" + "=" * 70)
print("PRELIMINARY CORRELATION ANALYSIS")
print("=" * 70)

corr_vars = ['income_per_capita', 'dist_to_science_park_km', 'dist_to_airbase_km',
             'education_rate', 'AgingIndex', 'POP_DENS', 'indigenous_ratio']

corr_matrix = gdf[corr_vars].corr()
income_corr = corr_matrix['income_per_capita'].sort_values(ascending=False)

print("\n📈 Correlations with Income Per Capita:")
for var, corr in income_corr.items():
    if var != 'income_per_capita':
        symbol = "✓" if abs(corr) > 0.3 else "~"
        direction = "positive" if corr > 0 else "negative"
        print(f"   {symbol} {var:30s}: {corr:7.3f} ({direction})")

# Check if hypotheses are preliminarily supported
print("\n" + "=" * 70)
print("PRELIMINARY HYPOTHESIS CHECK")
print("=" * 70)

dist_sp_corr = income_corr['dist_to_science_park_km']
dist_ab_corr = income_corr['dist_to_airbase_km']
edu_corr = income_corr['education_rate']
aging_corr = income_corr['AgingIndex']

print("\nH1 (Education → Income): Expected POSITIVE")
print(f"   → Correlation: {edu_corr:.3f}")
print(f"   → {'✓ SUPPORTED' if edu_corr > 0 else '✗ NOT SUPPORTED'} in bivariate analysis")

print("\nH2 (Distance to Science Park → Income): Expected NEGATIVE")
print(f"   → Correlation: {dist_sp_corr:.3f}")
print(f"   → {'✓ SUPPORTED' if dist_sp_corr < 0 else '✗ NOT SUPPORTED'} in bivariate analysis")

print("\nH3 (Aging Index → Income): Expected NEGATIVE")
print(f"   → Correlation: {aging_corr:.3f}")
print(f"   → {'✓ SUPPORTED' if aging_corr < 0 else '✗ NOT SUPPORTED'} in bivariate analysis")

print("\nH4 (Distance to Airbase → Income): Expected POSITIVE")
print(f"   → Correlation: {dist_ab_corr:.3f}")
print(f"   → {'✓ SUPPORTED' if dist_ab_corr > 0 else '✗ NOT SUPPORTED'} in bivariate analysis")

print("\n⚠️ NOTE: These are bivariate correlations. Multivariate regression needed for full test!")

# Save enhanced dataset
print("\n" + "=" * 70)
print("SAVING ENHANCED DATASET")
print("=" * 70)

# Convert back to WGS84 for compatibility
gdf_output = gdf.to_crs('EPSG:4326')

# Drop the centroid column (not needed for output)
gdf_output = gdf_output.drop(columns=['centroid'])

# Save as new shapefile
output_path = 'Hsinchu_City_with_distances.shp'
gdf_output.to_file(output_path)
print(f"✓ Saved enhanced shapefile: {output_path}")

# Also save as CSV for easy viewing
csv_data = gdf_output.drop(columns=['geometry'])
csv_data.to_csv('Hsinchu_City_with_distances.csv', index=False)
print(f"✓ Saved as CSV: Hsinchu_City_with_distances.csv")

# Create summary report
print("\n" + "=" * 70)
print("CREATING SUMMARY REPORT")
print("=" * 70)

report = []
report.append("=" * 70)
report.append("HSINCHU DISTANCE VARIABLE CALCULATION REPORT")
report.append("=" * 70)
report.append("")
report.append("KEY LOCATIONS:")
report.append(f"  Hsinchu Science Park: {SCIENCE_PARK_LAT}°N, {SCIENCE_PARK_LON}°E")
report.append(f"  Hsinchu Air Base:     {AIRBASE_LAT}°N, {AIRBASE_LON}°E")
report.append("")
report.append("DISTANCE STATISTICS:")
report.append("")
report.append("Distance to Science Park (km):")
report.append(f"  Mean: {gdf['dist_to_science_park_km'].mean():.2f}, Median: {gdf['dist_to_science_park_km'].median():.2f}")
report.append(f"  Range: {gdf['dist_to_science_park_km'].min():.2f} - {gdf['dist_to_science_park_km'].max():.2f}")
report.append("")
report.append("Distance to Air Base (km):")
report.append(f"  Mean: {gdf['dist_to_airbase_km'].mean():.2f}, Median: {gdf['dist_to_airbase_km'].median():.2f}")
report.append(f"  Range: {gdf['dist_to_airbase_km'].min():.2f} - {gdf['dist_to_airbase_km'].max():.2f}")
report.append("")
report.append("CORRELATIONS WITH INCOME PER CAPITA:")
for var, corr in income_corr.items():
    if var != 'income_per_capita':
        report.append(f"  {var:30s}: {corr:7.3f}")
report.append("")
report.append("HYPOTHESIS PRELIMINARY SUPPORT:")
report.append(f"  H1 (Education positive): {'SUPPORTED' if edu_corr > 0 else 'NOT SUPPORTED'} (r={edu_corr:.3f})")
report.append(f"  H2 (Sci Park negative): {'SUPPORTED' if dist_sp_corr < 0 else 'NOT SUPPORTED'} (r={dist_sp_corr:.3f})")
report.append(f"  H3 (Aging negative): {'SUPPORTED' if aging_corr < 0 else 'NOT SUPPORTED'} (r={aging_corr:.3f})")
report.append(f"  H4 (Airbase positive): {'SUPPORTED' if dist_ab_corr > 0 else 'NOT SUPPORTED'} (r={dist_ab_corr:.3f})")
report.append("")
report.append("OUTPUT FILES:")
report.append(f"  - {output_path} (shapefile with distance variables)")
report.append(f"  - Hsinchu_City_with_distances.csv (CSV format)")
report.append(f"  - distance_calculation_report.txt (this report)")
report.append("")
report.append("NEXT STEPS:")
report.append("  1. Use Hsinchu_City_with_distances.shp for your analysis")
report.append("  2. Run regression with all variables")
report.append("  3. Create distance decay plots")
report.append("  4. Test for spatial autocorrelation")
report.append("")

report_text = "\n".join(report)
with open('distance_calculation_report.txt', 'w', encoding='utf-8') as f:
    f.write(report_text)

print(report_text)

print("=" * 70)
print("✅ DISTANCE CALCULATION COMPLETE!")
print("=" * 70)
print("\n📁 Generated Files:")
print("   1. Hsinchu_City_with_distances.shp - Enhanced shapefile")
print("   2. Hsinchu_City_with_distances.csv - CSV for easy viewing")
print("   3. distance_calculation_report.txt - Summary report")
print("\n🎯 New Variables Added:")
print("   - dist_to_science_park_km : Distance to Science Park (km)")
print("   - dist_to_airbase_km      : Distance to Air Base (km)")
print("   - income_per_capita       : Income per capita")
print("   - education_rate          : Tertiary education rate (%)")
print("   - indigenous_ratio        : Indigenous population ratio (%)")
print("\n🚀 Next: Use these variables in your regression analysis!")

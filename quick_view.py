#!/usr/bin/env python3
"""
Quick Shapefile Viewer - View your Hsinchu data instantly!
Usage: python3 quick_view.py
"""

import sys

def install_packages():
    """Install required packages if missing"""
    import subprocess
    packages = ['geopandas', 'matplotlib', 'mapclassify']

    print("Installing required packages...")
    for package in packages:
        try:
            __import__(package)
        except ImportError:
            print(f"Installing {package}...")
            subprocess.check_call([sys.executable, '-m', 'pip', 'install', package, '-q'])
    print("✓ All packages ready!\n")

# Install packages first
install_packages()

import geopandas as gpd
import matplotlib.pyplot as plt
import numpy as np

print("=" * 60)
print("HSINCHU CITY SHAPEFILE QUICK VIEWER")
print("=" * 60)

# Load the shapefile
print("\n📂 Loading Hsinchu_City.shp...")
gdf = gpd.read_file('Hsinchu_City.shp')

print(f"✓ Loaded {len(gdf)} villages")
print(f"✓ Coordinate System: {gdf.crs}")
print(f"✓ Geometry Type: {gdf.geometry.type.unique()[0]}")

# Calculate derived variables
print("\n🔢 Calculating income per capita...")
gdf['income_per_capita'] = gdf['INCOME'] / gdf['POPULATION']

# Display basic statistics
print("\n" + "=" * 60)
print("📊 BASIC STATISTICS")
print("=" * 60)
print(f"Total Population:  {gdf['POPULATION'].sum():>12,.0f}")
print(f"Total Households:  {gdf['HOUSEHOLD'].sum():>12,.0f}")
print(f"Average Income/capita: {gdf['income_per_capita'].mean():>8,.0f} TWD (1000s)")
print(f"Income Range:      {gdf['income_per_capita'].min():>8,.0f} - {gdf['income_per_capita'].max():.0f}")

# Print top 5 richest and poorest villages
print("\n" + "=" * 60)
print("💰 TOP 5 HIGHEST INCOME VILLAGES")
print("=" * 60)
top5 = gdf.nlargest(5, 'income_per_capita')
for idx, row in top5.iterrows():
    print(f"{row['VILLNAME']:15s} ({row['TOWNNAME']:5s}): {row['income_per_capita']:>8,.0f} TWD")

print("\n" + "=" * 60)
print("📉 TOP 5 LOWEST INCOME VILLAGES")
print("=" * 60)
bottom5 = gdf.nsmallest(5, 'income_per_capita')
for idx, row in bottom5.iterrows():
    print(f"{row['VILLNAME']:15s} ({row['TOWNNAME']:5s}): {row['income_per_capita']:>8,.0f} TWD")

# Create visualizations
print("\n" + "=" * 60)
print("🎨 CREATING VISUALIZATIONS...")
print("=" * 60)

# Create a comprehensive view
fig, axes = plt.subplots(2, 2, figsize=(16, 14))
fig.suptitle('Hsinchu City - Quick Overview', fontsize=18, fontweight='bold')

# 1. Basic map with village boundaries
gdf.boundary.plot(ax=axes[0, 0], edgecolor='black', linewidth=0.5)
gdf.plot(ax=axes[0, 0], color='lightblue', alpha=0.6, edgecolor='black', linewidth=0.5)
axes[0, 0].set_title('Village Boundaries', fontsize=14, fontweight='bold')
axes[0, 0].axis('off')

# Add district labels
for district in gdf['TOWNNAME'].unique():
    district_center = gdf[gdf['TOWNNAME'] == district].geometry.unary_union.centroid
    axes[0, 0].annotate(district, xy=(district_center.x, district_center.y),
                       ha='center', fontsize=12, fontweight='bold',
                       bbox=dict(boxstyle='round,pad=0.5', facecolor='yellow', alpha=0.7))

# 2. Income per capita map
gdf.plot(column='income_per_capita', ax=axes[0, 1],
         legend=True, cmap='RdYlGn',
         edgecolor='black', linewidth=0.5,
         legend_kwds={'label': 'Income Per Capita (1000 TWD)', 'shrink': 0.8})
axes[0, 1].set_title('Income Per Capita Distribution', fontsize=14, fontweight='bold')
axes[0, 1].axis('off')

# 3. Education rate map
gdf['education_rate'] = (gdf['TERTIARY'] / gdf['POPULATION']) * 100
gdf.plot(column='education_rate', ax=axes[1, 0],
         legend=True, cmap='Blues',
         edgecolor='black', linewidth=0.5,
         legend_kwds={'label': 'Tertiary Education Rate (%)', 'shrink': 0.8})
axes[1, 0].set_title('Tertiary Education Rate', fontsize=14, fontweight='bold')
axes[1, 0].axis('off')

# 4. Population density map
gdf.plot(column='POP_DENS', ax=axes[1, 1],
         legend=True, cmap='YlOrRd',
         edgecolor='black', linewidth=0.5,
         legend_kwds={'label': 'Population per km²', 'shrink': 0.8})
axes[1, 1].set_title('Population Density', fontsize=14, fontweight='bold')
axes[1, 1].axis('off')

plt.tight_layout()
plt.savefig('hsinchu_quick_view.png', dpi=300, bbox_inches='tight')
print("✓ Saved: hsinchu_quick_view.png")

# Create a detailed income map
fig, ax = plt.subplots(1, 1, figsize=(14, 12))
gdf.plot(column='income_per_capita', ax=ax,
         legend=True, cmap='RdYlGn',
         edgecolor='black', linewidth=0.8,
         legend_kwds={'label': 'Income Per Capita (1000 TWD)', 'shrink': 0.7})

# Add labels for extreme values
high_income = gdf.nlargest(3, 'income_per_capita')
low_income = gdf.nsmallest(3, 'income_per_capita')

for idx, row in high_income.iterrows():
    centroid = row.geometry.centroid
    ax.annotate(f"{row['VILLNAME']}\n{row['income_per_capita']:.0f}",
               xy=(centroid.x, centroid.y),
               fontsize=8, ha='center',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='lightgreen', alpha=0.8))

for idx, row in low_income.iterrows():
    centroid = row.geometry.centroid
    ax.annotate(f"{row['VILLNAME']}\n{row['income_per_capita']:.0f}",
               xy=(centroid.x, centroid.y),
               fontsize=8, ha='center',
               bbox=dict(boxstyle='round,pad=0.3', facecolor='lightcoral', alpha=0.8))

ax.set_title('Hsinchu City - Income Per Capita by Village\n(Top 3 Highest and Lowest Labeled)',
            fontsize=16, fontweight='bold', pad=20)
ax.axis('off')

plt.tight_layout()
plt.savefig('hsinchu_income_detailed.png', dpi=300, bbox_inches='tight')
print("✓ Saved: hsinchu_income_detailed.png")

# Create district comparison
fig, ax = plt.subplots(1, 1, figsize=(10, 6))
district_income = gdf.groupby('TOWNNAME')['income_per_capita'].agg(['mean', 'median', 'std'])
district_income = district_income.sort_values('mean', ascending=False)

x = range(len(district_income))
ax.bar(x, district_income['mean'], alpha=0.7, label='Mean', color='steelblue')
ax.errorbar(x, district_income['mean'], yerr=district_income['std'],
            fmt='none', ecolor='black', capsize=5, alpha=0.5)

ax.set_xlabel('District', fontsize=12, fontweight='bold')
ax.set_ylabel('Income Per Capita (1000 TWD)', fontsize=12, fontweight='bold')
ax.set_title('Average Income Per Capita by District', fontsize=14, fontweight='bold')
ax.set_xticks(x)
ax.set_xticklabels(district_income.index, rotation=45, ha='right')
ax.legend()
ax.grid(True, alpha=0.3)

plt.tight_layout()
plt.savefig('hsinchu_district_comparison.png', dpi=300, bbox_inches='tight')
print("✓ Saved: hsinchu_district_comparison.png")

print("\n" + "=" * 60)
print("✅ VISUALIZATION COMPLETE!")
print("=" * 60)
print("\nGenerated files:")
print("  1. hsinchu_quick_view.png - 4-panel overview")
print("  2. hsinchu_income_detailed.png - Detailed income map with labels")
print("  3. hsinchu_district_comparison.png - District comparison chart")
print("\nYou can now:")
print("  • Open these PNG files to see your data visually")
print("  • Use them in your presentation")
print("  • Run the full analysis: python3 hsinchu_income_analysis.py")
print("\n🎉 Your shapefile is ready for analysis!")

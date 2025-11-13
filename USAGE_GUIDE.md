# Quick Start Guide: Visualizing Your Hsinchu Shapefile

## What Are Those 5 Files?

Your shapefile consists of 5 files that work together as ONE dataset:

```
Hsinchu_City.shp  ← Main file (geometries/shapes)
Hsinchu_City.dbf  ← Data table (income, population, etc.)
Hsinchu_City.shx  ← Index (links shapes to data)
Hsinchu_City.prj  ← Coordinate system
Hsinchu_City.cpg  ← Text encoding
```

**Important:** You must keep ALL 5 files together. They work as a unit!

---

## 3 Ways to View Your Data

### Option 1: Quick Static Maps (Easiest!)

**Best for:** Quick viewing, presentation slides, reports

```bash
python3 quick_view.py
```

**What you get:**
- `hsinchu_quick_view.png` - 4-panel overview
- `hsinchu_income_detailed.png` - Detailed income map
- `hsinchu_district_comparison.png` - Bar chart comparison

**Time:** ~30 seconds

---

### Option 2: Interactive Web Map (Most Fun!)

**Best for:** Exploring data, finding patterns, presentations

```bash
python3 interactive_map.py
```

**What you get:**
- `hsinchu_interactive_map.html` - Open in any web browser!

**Features:**
- 🖱️ **Hover** over villages → See detailed info
- 🔍 **Zoom/Pan** → Explore the map
- 📍 **Markers** → Highest/lowest income areas
- 🎨 **Color-coded** → Income distribution
- 🗺️ **Multiple layers** → Switch between different map styles

**Time:** ~30 seconds

**To view:** Just double-click the HTML file or open it in Chrome/Firefox/Safari

---

### Option 3: Full Spatial Analysis (Most Comprehensive!)

**Best for:** Academic presentations, research, statistical analysis

```bash
python3 hsinchu_income_analysis.py
```

**What you get:**
- All statistical analyses
- Moran's I (spatial autocorrelation)
- LISA cluster maps
- Hot spot analysis
- Regression results
- 10+ visualization files

**Time:** ~1-2 minutes

---

## Software You Can Use

### Free GIS Software (No coding!)

1. **QGIS** (Recommended!)
   - Download: https://qgis.org
   - Free and powerful
   - Just drag the `.shp` file into QGIS
   - Right-click layer → Properties → Symbology → Choose color scheme

2. **ArcGIS Online**
   - Upload the shapefile (zip all 5 files first)
   - Create web maps

### Python Libraries (For coding)

```python
import geopandas as gpd

# Load the shapefile
gdf = gpd.read_file('Hsinchu_City.shp')

# See the data
print(gdf.head())

# Make a simple map
gdf.plot()

# Color by income
gdf.plot(column='INCOME', legend=True, cmap='RdYlGn')
```

### R Libraries (For R users)

```r
library(sf)

# Load shapefile
hsinchu <- st_read("Hsinchu_City.shp")

# View data
head(hsinchu)

# Plot
plot(hsinchu["INCOME"])
```

---

## What Can You Visualize?

Using your data, you can create maps showing:

### Economic Variables
- ✅ **Income per capita** - Who earns more/less?
- ✅ **Total income** - Which villages have highest total income?
- ✅ **Income inequality** - Spatial distribution of wealth

### Demographic Variables
- ✅ **Population density** - Where do people live?
- ✅ **Aging index** - Where are elderly populations?
- ✅ **Sex ratio** - Gender distribution
- ✅ **Household size** - Family structure

### Education Variables
- ✅ **Education rate** - Percentage with university degrees
- ✅ **Tertiary education** - Absolute numbers

### Spatial Patterns
- ✅ **Hot spots** - Where are income clusters?
- ✅ **Cold spots** - Where are low-income clusters?
- ✅ **Spatial autocorrelation** - Is income clustered or random?

---

## Quick Commands Cheat Sheet

```bash
# View your data quickly
python3 quick_view.py

# Create interactive map
python3 interactive_map.py

# Full analysis (spatial stats)
python3 hsinchu_income_analysis.py

# Just examine the data
python3 examine_data.py

# Install dependencies
pip install -r requirements.txt
```

---

## Common Tasks

### Task: "I want to see the map NOW!"

```bash
python3 quick_view.py
```
Open the PNG files that get created.

### Task: "I want to explore interactively"

```bash
python3 interactive_map.py
```
Open `hsinchu_interactive_map.html` in your browser.

### Task: "I need statistics for my presentation"

```bash
python3 hsinchu_income_analysis.py
```
Check the `analysis_report.txt` and all the PNG files.

### Task: "I want to use QGIS"

1. Download QGIS: https://qgis.org
2. Open QGIS
3. Drag `Hsinchu_City.shp` into QGIS window
4. Right-click layer → Properties → Symbology
5. Choose "Graduated" and select a variable (e.g., INCOME)
6. Click "Classify" → OK

---

## Troubleshooting

### Error: "Module not found"

**Solution:**
```bash
pip install geopandas matplotlib folium
```

### Error: "File not found"

**Solution:** Make sure you're in the correct directory
```bash
cd /home/user/SDA_presentation
ls  # Should see all 5 shapefile components
```

### Error: "Cannot read shapefile"

**Solution:** Make sure ALL 5 files are in the same folder

---

## File Formats Explained

| Extension | Purpose | Can I delete it? |
|-----------|---------|------------------|
| `.shp` | Geometry (shapes) | ❌ NO - Essential |
| `.dbf` | Attributes (data) | ❌ NO - Essential |
| `.shx` | Index | ❌ NO - Essential |
| `.prj` | Coordinate system | ⚠️ Not recommended |
| `.cpg` | Encoding | ⚠️ Not recommended |

**Rule:** Keep all files together, always!

---

## Next Steps

1. **Start Simple:**
   ```bash
   python3 quick_view.py
   ```

2. **Explore Interactively:**
   ```bash
   python3 interactive_map.py
   ```

3. **Read the Plan:**
   Open `PRESENTATION_PLAN.md` for your presentation structure

4. **Run Full Analysis:**
   ```bash
   python3 hsinchu_income_analysis.py
   ```

5. **Prepare Presentation:**
   Use the generated images and statistics in your slides

---

## Tips for Your Presentation

1. **Start with the interactive map** - Show it live to your audience
2. **Use the static maps** - Put them in PowerPoint/Google Slides
3. **Reference statistics** - Use numbers from `analysis_report.txt`
4. **Tell a story** - Don't just show maps, explain what they mean
5. **Connect to theory** - Link visual patterns to theoretical frameworks

---

## Resources

- **QGIS Tutorials:** https://www.qgistutorials.com
- **GeoPandas Docs:** https://geopandas.org
- **Shapefile Format:** https://en.wikipedia.org/wiki/Shapefile

---

**Need help?** Check `PRESENTATION_PLAN.md` for the complete analysis framework!

🎉 **Happy Mapping!**

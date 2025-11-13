# Hsinchu City Income Inequality Analysis
### Spatial Distribution and Influencing Factors

This repository contains a comprehensive spatial analysis of income inequality in Hsinchu City, Taiwan, examining the spatial distribution patterns and factors that influence income disparities at the village level.

---

## 📁 Repository Contents

- **`Hsinchu_City.shp`** (+ .dbf, .shx, .prj, .cpg) - Shapefile with village-level data
- **`PRESENTATION_PLAN.md`** - Detailed presentation structure and analysis framework
- **`hsinchu_income_analysis.py`** - Main analysis script
- **`requirements.txt`** - Python dependencies
- **`examine_data.py`** - Data exploration utility

---

## 🚀 Getting Started

### 1. Install Dependencies

```bash
# Create virtual environment (recommended)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate

# Install required packages
pip install -r requirements.txt
```

### 2. Run the Analysis

```bash
python3 hsinchu_income_analysis.py
```

This will generate:
- Descriptive statistics (CSV)
- Distribution plots
- Correlation matrix
- Choropleth maps
- Spatial autocorrelation analysis (Moran's I)
- LISA cluster maps
- Hot spot analysis (Getis-Ord Gi*)
- Regression analysis
- Summary report

### 3. Review the Outputs

All outputs will be saved in the current directory:
- `descriptive_statistics.csv`
- `distributions.png`
- `correlation_matrix.png`
- `choropleth_maps.png`
- `income_map_detailed.png`
- `morans_i_scatterplot.png`
- `lisa_cluster_map.png`
- `hotspot_analysis.png`
- `regression_scatter.png`
- `analysis_report.txt`

---

## 📊 Data Description

### Available Variables

| Variable | Description |
|----------|-------------|
| `VILLCODE` | Village ID number |
| `COUNTYNAME` | County name (新竹市) |
| `TOWNNAME` | District name (北區/東區/香山區) |
| `VILLNAME` | Village name |
| `HOUSEHOLD` | Number of households |
| `POPULATION` | Total population |
| `SEX_RATIO` | Sex ratio (males per 100 females) |
| `POP_DENS` | Population density (per km²) |
| `AgingIndex` | (Population 65+) / (Population 0-14) × 100 |
| `INDIGENOUS` | Indigenous population |
| `TERTIARY` | Population with tertiary education |
| `INCOME` | Total income (1,000 TWD) |

### Derived Variables

The analysis script calculates additional variables:
- `income_per_capita` - Income / Population
- `income_per_household` - Income / Household
- `education_rate` - (Tertiary / Population) × 100
- `indigenous_ratio` - (Indigenous / Population) × 100
- `household_size` - Population / Household

---

## 🔍 Analysis Methods

### 1. Descriptive Statistics
- Summary statistics for all variables
- Distribution analysis
- Outlier detection

### 2. Correlation Analysis
- Pearson correlation coefficients
- Heatmap visualization
- Identification of key relationships

### 3. Spatial Analysis
- **Choropleth Mapping**: Visual representation of variable distributions
- **Global Moran's I**: Measure of overall spatial autocorrelation
- **Local Moran's I (LISA)**: Identification of local clusters
  - HH: High-income surrounded by high-income (hot spots)
  - LL: Low-income surrounded by low-income (cold spots)
  - HL/LH: Spatial outliers
- **Getis-Ord Gi***: Hot spot analysis with statistical significance

### 4. Regression Analysis
- Ordinary Least Squares (OLS) regression
- Dependent variable: Income per capita
- Independent variables: Education rate, Aging Index, Population Density, etc.

---

## 🎯 Research Questions

1. **What is the spatial distribution of income inequality in Hsinchu City?**
   - Are there spatial clusters of high/low income?
   - Which areas are hot spots vs. cold spots?

2. **What factors influence income inequality?**
   - Education level
   - Aging population
   - Population density
   - Indigenous population ratio

3. **Can spatial patterns be explained by theoretical frameworks?**
   - Human Capital Theory
   - Spatial Mismatch Theory
   - Urban Economics
   - Agglomeration Economics

---

## 🎓 Theoretical Framework

### 1. Human Capital Theory
Education increases productivity and income. We expect a **positive correlation** between tertiary education rate and income.

### 2. Spatial Mismatch Theory
Geographic distance between workers and jobs affects income. Proximity to Hsinchu Science Park should correlate with higher income.

### 3. Urban Economics (Bid-Rent Theory)
Central locations with better access to jobs have higher land values and economic activity. Urban core areas should have higher incomes.

### 4. Demographic Transition Theory
Aging populations have different income structures. Areas with higher aging index may have lower active income.

### 5. Agglomeration Economics
Clustering of high-tech industries creates knowledge spillovers and network effects, increasing local incomes.

---

## 📈 Expected Findings

### Hypotheses:
1. Villages closer to Hsinchu Science Park have higher incomes
2. Higher education rate → higher income (positive correlation)
3. Higher aging index → lower income (negative correlation)
4. Income shows positive spatial autocorrelation (clustering)
5. East District (urban core) has higher income than North District

---

## 🗺️ Hsinchu City Context

**"Taiwan's Silicon Valley"**
- Home to Hsinchu Science Park (high-tech hub)
- Major universities: National Tsing Hua University, National Yang Ming Chiao Tung University
- Mix of high-tech workers and traditional residents
- Significant income disparities between tech-centered and traditional areas

---

## 📝 Presentation Tips

1. **Start with a compelling map** showing income inequality
2. **Tell a story** - frame as investigating the causes of inequality
3. **Visual first** - use maps and charts, support with statistics
4. **Connect to theory** - explicitly link findings to theoretical frameworks
5. **Policy implications** - what do findings mean for urban planning?
6. **Be honest** - acknowledge limitations and data constraints

---

## 📚 Additional Resources

### Extending the Analysis

**Additional variables to consider:**
- Distance to Hsinchu Science Park (calculate using GIS)
- Distance to city center
- Distance to universities
- Public transportation access
- Housing prices (if available)

**Advanced spatial models:**
- Spatial Lag Model (accounts for spatial dependence)
- Spatial Error Model (accounts for spatial error)
- Geographically Weighted Regression (GWR)

---

## 🤝 Contributing

This is an educational project for spatial data analysis. Feel free to:
- Extend the analysis
- Add new variables
- Try different spatial models
- Create interactive visualizations

---

## 📧 Contact

**Team Member**: [Your Name]
**Course**: Spatial Data Analysis
**Focus Area**: Hsinchu City

---

## 📄 License

This project is for educational purposes.

---

## 🙏 Acknowledgments

- Data source: [Specify your data source]
- Course instructor: [Instructor name]
- Python libraries: GeoPandas, PySAL, Matplotlib, Seaborn

---

**Good luck with your presentation! 🎉**
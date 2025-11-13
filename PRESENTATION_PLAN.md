# Hsinchu City Income Inequality Analysis
## Spatial Distribution and Influencing Factors

---

## Presentation Structure

### 1. Introduction & Background (3-4 minutes)
**Slide Content:**
- **Research Question**: What is the spatial distribution of income inequality in Hsinchu City, and what factors influence this inequality?
- **Study Area**: Hsinchu City - known as "Taiwan's Silicon Valley"
  - High-tech industry hub (Science Park)
  - Mix of urban and residential areas
  - Significant economic disparities
- **Data Overview**: 122 villages in Hsinchu City with socio-economic indicators

**Key Points to Mention:**
- Hsinchu's unique position as a technology hub
- Expected income disparities between areas near Science Park vs. traditional residential areas
- Importance of understanding spatial inequality for policy making

---

### 2. Data Description & Methodology (4-5 minutes)

**Slide Content:**

**Available Variables:**
- **Demographic**: Population, Household, Sex Ratio, Population Density
- **Social Structure**: Aging Index, Indigenous Population, Tertiary Education
- **Economic**: Total Income (per village)

**Derived Variables (to calculate):**
- Income per capita: INCOME / POPULATION
- Income per household: INCOME / HOUSEHOLD
- Education rate: TERTIARY / POPULATION
- Aging rate: Related to AgingIndex

**Spatial Analysis Methods:**
1. Choropleth mapping (income distribution)
2. Spatial autocorrelation (Moran's I)
3. Hot spot analysis (Getis-Ord Gi*)
4. Regression analysis (OLS & Spatial)

---

### 3. Descriptive Statistics (3-4 minutes)

**Slide Content:**
- Summary statistics table for all variables
- Distribution plots (histograms/boxplots) for:
  - Income per capita
  - Population density
  - Education rate
  - Aging index
- Identify outliers and data quality issues

**Key Insights to Look For:**
- Range of income inequality
- Which villages are extremely high/low income
- Relationship between variables (correlation matrix)

---

### 4. Spatial Distribution Analysis (5-6 minutes)

**Maps to Create:**

a) **Income Distribution Map**
   - Income per capita by village (choropleth)
   - Color scheme: low (red) to high (green/blue)
   - Identify spatial clusters

b) **Key Demographic Maps**
   - Population density
   - Education rate (tertiary education)
   - Aging index

c) **Spatial Autocorrelation**
   - Moran's I scatter plot
   - LISA cluster map (High-High, Low-Low, High-Low, Low-High)

**Analysis Points:**
- Are high-income areas clustered?
- Where are the low-income clusters?
- Is there a north-south or east-west gradient?

---

### 5. Factor Analysis - Identifying Influences (6-7 minutes)

**A. Statistical Relationships**

**Correlation Analysis:**
- Income vs. Education rate (expected: positive)
- Income vs. Aging Index (expected: negative)
- Income vs. Population Density (expected: positive in urban areas)

**Regression Model:**
```
Income_per_capita ~ Education_rate + Aging_Index + Pop_Density + Indigenous_ratio
```

**B. Spatial Context Factors**

**Historical & Economic Factors:**
1. **Hsinchu Science Park Effect**
   - Proximity to Science Park → Higher income
   - Technology industry employment
   - Map distance from Science Park

2. **Urban-Rural Divide**
   - Central urban areas (East District) vs. peripheral areas (North District)
   - Better infrastructure and services

3. **Education Infrastructure**
   - Proximity to universities (National Tsing Hua University, National Chiao Tung University)
   - Educated population attracts high-income jobs

4. **Aging Society Impact**
   - Old residential areas with aging population
   - Lower income due to retirees
   - Less economic activity

**C. Additional Variables to Consider:**
- Distance to Science Park (calculate using GIS)
- Distance to city center
- District classification (North vs. East)
- Housing age/development period

---

### 6. Theoretical Framework (3-4 minutes)

**Theories to Apply:**

**1. Human Capital Theory**
- Education (tertiary education rate) increases productivity and income
- Explains positive correlation between education and income

**2. Spatial Mismatch Theory**
- Geographic distance between workers and jobs affects income
- Proximity to employment centers (Science Park) matters

**3. Urban Economics - Bid-Rent Theory**
- Central locations with better access to jobs command higher value
- Population density reflects land value and economic activity

**4. Demographic Transition Theory**
- Aging populations have different income structures
- Elderly areas may have lower active income but higher wealth accumulation

**5. Agglomeration Economics**
- Clustering of high-tech industries in Science Park area
- Knowledge spillovers and network effects increase local incomes

---

### 7. Expected Findings & Hypotheses (2-3 minutes)

**Hypotheses:**
1. **H1**: Villages closer to Hsinchu Science Park have higher average incomes
2. **H2**: Higher education rate positively correlates with income
3. **H3**: Higher aging index negatively correlates with income
4. **H4**: Income inequality shows spatial clustering (positive spatial autocorrelation)
5. **H5**: East District (urban core) has higher income than North District

---

### 8. Results Presentation (5-6 minutes)

**Key Results to Show:**
1. **Spatial Pattern**:
   - Clear map showing income clusters
   - Moran's I value and significance

2. **Statistical Results**:
   - Regression coefficients table
   - R-squared value
   - Significant predictors

3. **Hot Spot Analysis**:
   - Where are the income hot spots?
   - Where are the cold spots?

4. **Model Comparison**:
   - OLS vs. Spatial Lag Model
   - Which model fits better?

---

### 9. Discussion & Interpretation (4-5 minutes)

**Key Discussion Points:**

**A. Policy Implications**
- Need for balanced regional development
- Investment in education infrastructure in low-income areas
- Support for aging communities
- Public transportation to connect peripheral areas to Science Park

**B. Limitations**
- Income data is total income, not individual income
- No data on housing costs, cost of living
- No temporal dimension (cross-sectional only)
- Missing variables: employment rate, industry composition

**C. Future Research**
- Time series analysis to track changes
- Detailed industry employment data
- Housing market analysis
- Qualitative interviews with residents

---

### 10. Conclusion (2-3 minutes)

**Summary:**
- Hsinchu City shows clear spatial patterns of income inequality
- Key factors identified: education, aging, proximity to economic centers
- Spatial clustering confirms need for place-based policies
- Theoretical frameworks successfully explain observed patterns

**Recommendations:**
1. Enhance public transportation connectivity
2. Invest in lifelong learning programs in low-income areas
3. Support aging-in-place programs
4. Encourage mixed-use development to reduce spatial mismatch

---

## Technical Requirements

### Software & Packages Needed:
- **Python**: geopandas, matplotlib, seaborn, pandas, numpy, scipy, scikit-learn
- **Spatial Analysis**: PySAL (spatial statistics and econometrics)
- **Visualization**: folium (interactive maps), plotly

### Deliverables:
1. Presentation slides (PowerPoint/PDF)
2. Analysis script (Python .py or Jupyter notebook)
3. Maps (high-resolution PNG/PDF)
4. Statistical output tables
5. (Optional) Interactive web map

---

## Time Management
- **Total Presentation Time**: 35-40 minutes
- **Q&A**: 5-10 minutes

---

## Tips for Strong Presentation

1. **Start Strong**: Hook audience with compelling map showing inequality
2. **Tell a Story**: Frame as detective work - finding clues about inequality
3. **Visual First**: Lead with maps and visualizations, support with statistics
4. **Theory Connection**: Explicitly link findings to theories
5. **So What?**: Always explain why findings matter for policy/society
6. **Honest About Limitations**: Shows critical thinking
7. **Practice**: Rehearse transitions between sections

---

## Data Analysis Workflow

```
1. Data Preparation
   ├── Load shapefile
   ├── Calculate derived variables
   ├── Data cleaning and outlier check
   └── Exploratory data analysis

2. Descriptive Analysis
   ├── Summary statistics
   ├── Distribution plots
   └── Correlation matrix

3. Spatial Analysis
   ├── Create choropleth maps
   ├── Calculate Moran's I
   ├── LISA analysis
   └── Hot spot analysis (Getis-Ord Gi*)

4. Statistical Modeling
   ├── OLS regression
   ├── Spatial diagnostics
   ├── Spatial lag/error model
   └── Model comparison

5. Visualization & Reporting
   ├── Final maps
   ├── Results tables
   ├── Interpretation
   └── Presentation slides
```

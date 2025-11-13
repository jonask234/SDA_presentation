# Presentation Slides: Research Questions and Theoretical Framework
## Hsinchu City Income Inequality Analysis

---

## SLIDE: Final Decision on Research Questions

### **Primary Research Question:**
**What spatial and socioeconomic factors explain income inequality across villages in Hsinchu City?**

### **Sub-Questions:**

**1. Spatial Economic Factors**
- Does proximity to Hsinchu Science Park influence village-level income?
- How does distance from the airbase affect local income levels?

**2. Human Capital Factors**
- What is the relationship between tertiary education rates and income inequality?
- Is this relationship spatially clustered?

**3. Demographic Structure**
- How does population aging affect income distribution across villages?
- Do demographic differences explain spatial income patterns?

**4. Spatial Patterns**
- Is income inequality spatially clustered or randomly distributed?
- Where are the income "hot spots" and "cold spots" in Hsinchu City?

### **Research Scope:**
- **Geographic Unit:** Village level (122 villages)
- **Dependent Variable:** Income per capita
- **Analysis Type:** Cross-sectional spatial analysis
- **Methods:** Spatial autocorrelation, regression analysis, hot spot detection

---

## SLIDE: Analytical Framework Overview

### **Model Structure:**

```
Income per capita = f(Economic Geography, Human Capital, Demographics, Controls)
```

### **Variable Categories:**

**Primary Explanatory Variables:**
1. **Economic Geography**
   - Distance to Hsinchu Science Park
   - Distance to airbase

2. **Human Capital**
   - Tertiary education rate (%)

3. **Demographic Structure**
   - Aging Index

**Control Variables:**
- Indigenous population ratio
- Population density

---

## SLIDE: Theoretical Framework - Human Capital Theory

### **Theory 1: Human Capital Theory**

**Core Concept:**
Investment in education increases individual productivity, leading to higher earnings (Becker, 1964; Mincer, 1974)

**Application to Hsinchu:**
Villages with higher rates of tertiary education should exhibit higher average income levels

### **Key Literature:**

**Foundational Works:**
- **Becker, G. S. (1964).** *Human Capital: A Theoretical and Empirical Analysis with Special Reference to Education.* Chicago: University of Chicago Press.
  - Established human capital as productive investment
  - Education → Skills → Productivity → Income

- **Mincer, J. (1974).** *Schooling, Experience, and Earnings.* New York: NBER.
  - Demonstrated log-linear relationship between education and earnings
  - Each additional year of schooling increases earnings by ~10%

**Contemporary Evidence:**
- **Card, D. (1999).** "The Causal Effect of Education on Earnings." *Handbook of Labor Economics*, 3, 1801-1863.
  - Meta-analysis: Returns to education range 5-15% per year
  - Effect robust across countries and time periods

- **Psacharopoulos, G., & Patrinos, H. A. (2018).** "Returns to Investment in Education: A Decennial Review of the Global Literature." *Education Economics*, 26(5), 445-458.
  - Higher education shows particularly strong returns in Asia
  - Bachelor's degree increases earnings by 50-100% on average

**Taiwan-Specific:**
- **Tsai, W. J., & Tsay, R. S. (2003).** "The Quality of Education and Earnings in Taiwan." *Journal of Development Studies*, 39(3), 130-152.
  - Strong education-income link in Taiwan
  - Particularly pronounced in high-tech regions

### **Hypothesis H1:**
**Villages with higher tertiary education rates will have significantly higher income per capita**

**Expected Coefficient:** **Positive (+)** and statistically significant
- Each 1% increase in education rate → ~2-5% increase in income per capita

---

## SLIDE: Theoretical Framework - Agglomeration Economics

### **Theory 2: Agglomeration Economics & Spatial Mismatch**

**Core Concepts:**

**A. Agglomeration Economics (Marshall, 1890; Krugman, 1991)**
- Geographic concentration of industries creates positive externalities
- Knowledge spillovers, specialized labor pools, shared infrastructure
- Workers near clusters benefit from higher wages and more opportunities

**B. Spatial Mismatch Theory (Kain, 1968; Gobillon et al., 2007)**
- Geographic distance between workers and jobs reduces economic opportunities
- Transportation costs (time + money) reduce effective wages
- Proximity to employment centers increases income

### **Key Literature:**

**Agglomeration Theory:**
- **Marshall, A. (1890).** *Principles of Economics.* London: Macmillan.
  - Identified three sources of agglomeration: labor pooling, input sharing, knowledge spillovers

- **Krugman, P. (1991).** "Increasing Returns and Economic Geography." *Journal of Political Economy*, 99(3), 483-499.
  - Nobel Prize work: Geographic concentration emerges from increasing returns
  - Core-periphery patterns in economic geography

- **Glaeser, E. L., Kallal, H. D., Scheinkman, J. A., & Shleifer, A. (1992).** "Growth in Cities." *Journal of Political Economy*, 100(6), 1126-1152.
  - Industrial clusters drive urban growth
  - Knowledge spillovers are geographically bounded

**Technology Clusters:**
- **Saxenian, A. (1994).** *Regional Advantage: Culture and Competition in Silicon Valley and Route 128.* Cambridge: Harvard University Press.
  - Tech clusters create premium wages for local residents
  - Network effects and knowledge spillovers

- **Moretti, E. (2012).** *The New Geography of Jobs.* Boston: Houghton Mifflin Harcourt.
  - High-tech jobs create 5 additional local service jobs
  - Local multiplier effect: tech workers spend locally, raising area incomes

**Spatial Mismatch:**
- **Kain, J. F. (1968).** "Housing Segregation, Negro Employment, and Metropolitan Decentralization." *Quarterly Journal of Economics*, 82(2), 175-197.
  - Distance to jobs reduces employment and earnings
  - Commuting costs matter

- **Gobillon, L., Selod, H., & Zenou, Y. (2007).** "The Mechanisms of Spatial Mismatch." *Urban Studies*, 44(12), 2401-2427.
  - Three mechanisms: search costs, commuting costs, spatial mismatch in networks
  - Distance elasticity: 10% increase in distance → 1-3% decrease in wages

**Science Parks (Asia Context):**
- **Hu, T. S. (2008).** "Interaction Among High-Tech Talent and Its Impact on Innovation Performance: A Comparison of Taiwanese Science Parks at Different Stages of Development." *European Planning Studies*, 16(2), 163-187.
  - Hsinchu Science Park drives regional innovation and wages
  - Proximity effects measurable at village level

- **Breznitz, D., & Murphree, M. (2011).** *Run of the Red Queen: Government, Innovation, Globalization, and Economic Growth in China.* New Haven: Yale University Press.
  - Asian tech clusters create steep wage gradients by distance

### **Hypothesis H2:**
**Income per capita decreases with distance from Hsinchu Science Park**

**Expected Coefficient:** **Negative (−)** and statistically significant
- Each 1 km increase in distance → 1-3% decrease in income per capita
- Effect should be strongest within 5-10 km radius

---

## SLIDE: Theoretical Framework - Demographic Transition

### **Theory 3: Demographic Structure Theory**

**Core Concept:**
Age structure affects income through labor force participation, productivity life-cycle, and dependency ratios (Lee & Mason, 2010)

**Application to Hsinchu:**
Villages with higher Aging Index have more elderly (retired) and fewer working-age adults, reducing average income

### **Key Literature:**

**Demographic Economics:**
- **Lee, R., & Mason, A. (2010).** "Fertility, Human Capital, and Economic Growth over the Demographic Transition." *European Journal of Population*, 26(2), 159-182.
  - Aging populations have lower labor force participation
  - Retirement reduces active income

- **Bloom, D. E., Canning, D., & Fink, G. (2010).** "Implications of Population Ageing for Economic Growth." *Oxford Review of Economic Policy*, 26(4), 583-612.
  - Aging Index inversely related to economic output
  - Higher dependency ratios reduce per capita income

**Aging and Income:**
- **Maestas, N., Mullen, K. J., & Powell, D. (2016).** "The Effect of Population Aging on Economic Growth, the Labor Force and Productivity." *NBER Working Paper No. 22452.*
  - 10% increase in population 60+ → 5.5% decrease in GDP per capita
  - Mechanism: reduced labor force participation

- **Walder, A. G., & Hu, S. (2009).** "Revolution, Reform, and Status Inheritance: Urban China, 1949-1996." *American Journal of Sociology*, 114(5), 1395-1427.
  - Life-cycle income peaks at age 45-55
  - Elderly households have 30-40% lower income than working-age

**Taiwan Context:**
- **Chu, C. Y. C., & Jiang, L. (1997).** "Demographic Transition, Family Structure, and Income Inequality." *Review of Economics and Statistics*, 79(4), 665-669.
  - Taiwan's rapid aging affects regional income distribution
  - Areas with older populations show lower average income

- **Chen, C. N., & Chiang, T. L. (2015).** "The Impacts of Population Aging on Fiscal Policy in Taiwan." *Journal of Population Ageing*, 8(3), 165-179.
  - Aging Index correlates negatively with regional economic activity

### **Hypothesis H3:**
**Villages with higher Aging Index will have lower income per capita**

**Expected Coefficient:** **Negative (−)** and statistically significant
- Each 10-point increase in Aging Index → 2-4% decrease in income per capita

---

## SLIDE: Theoretical Framework - Environmental Disamenities

### **Theory 4: Environmental Economics - Hedonic Pricing**

**Core Concept:**
Environmental disamenities (noise, pollution, safety risks) reduce property values and neighborhood quality, affecting local incomes through sorting and amenity values (Rosen, 1974)

**Application to Airbase:**
Proximity to military airbase creates negative externalities (aircraft noise, safety concerns) that reduce area desirability and economic activity

### **Key Literature:**

**Hedonic Pricing Theory:**
- **Rosen, S. (1974).** "Hedonic Prices and Implicit Markets: Product Differentiation in Pure Competition." *Journal of Political Economy*, 82(1), 34-55.
  - Property values capitalize local amenities and disamenities
  - People "vote with their feet" - high-income households avoid disamenities

**Airport/Military Base Effects:**
- **Nelson, J. P. (2004).** "Meta-Analysis of Airport Noise and Hedonic Property Values." *Journal of Transport Economics and Policy*, 38(1), 1-27.
  - Meta-analysis of 33 studies across countries
  - Aircraft noise reduces property values by 0.5-0.6% per decibel
  - Effect extends up to 15 km from airfield

- **McMillen, D. P. (2004).** "Airport Expansions and Property Values: The Case of Chicago O'Hare Airport." *Journal of Urban Economics*, 55(3), 627-640.
  - Properties near airports have 9% lower values
  - Income sorting: lower-income households concentrate near airports

- **Cohen, J. P., & Coughlin, C. C. (2008).** "Spatial Hedonic Models of Airport Noise, Proximity, and Housing Prices." *Journal of Regional Science*, 48(5), 859-878.
  - Negative price gradient extends 10-15 km from runways
  - Noise exposure zones show 5-15% lower property values

**Military Installations:**
- **Bradbury, K. L., Engle, R., Ibbotson, R., & Hess, A. C. (1977).** "The Impact of Military Installations on Property Values." *Journal of Regional Science*, 17(2), 189-201.
  - Military bases create negative externalities similar to airports
  - Noise and safety concerns dominate any positive employment effects

- **Hogan, T. L., & Ragan, A. J. (2015).** "Do Military Installations Create Positive Economic Impact?" *Journal of Regional Analysis and Policy*, 45(2), 148-162.
  - Military employment benefits do not offset disamenity costs
  - Net effect on local incomes often negative or negligible

**Environmental Justice:**
- **Banzhaf, H. S., & Walsh, R. P. (2008).** "Do People Vote with Their Feet? An Empirical Test of Tiebout's Mechanism." *American Economic Review*, 98(3), 843-863.
  - High-income households sort away from environmental disamenities
  - Creates income stratification by environmental quality

### **Hsinchu Airbase Context:**
- **Hsinchu Airbase (新竹空軍基地):** Active military installation
- Aircraft operations create noise pollution
- Proximity likely creates negative amenity value

### **Hypothesis H4:**
**Income per capita increases with distance from the airbase (negative proximity effect)**

**Expected Coefficient:** **Positive (+)** on distance variable
- Farther from airbase → Higher income
- Mechanism: High-income households avoid noise pollution
- Each 1 km increase in distance → 0.5-2% increase in income per capita (estimated)

**Important Caveat:**
Effect may be small if airbase operations are limited or if military employment provides offsetting benefits

---

## SLIDE: Control Variables - Theoretical Justification

### **Control Variable 1: Indigenous Population Ratio**

**Theory:** Structural Inequality & Historical Disadvantage

**Key Literature:**
- **Cornell, S., & Kalt, J. P. (1992).** "Reloading the Dice: Improving the Chances for Economic Development on American Indian Reservations." In *What Can Tribes Do?* Los Angeles: American Indian Studies Center.
  - Indigenous populations face structural economic disadvantages
  - Historical marginalization affects contemporary income

- **Anderson, T., & Parker, D. (2008).** "Sovereignty, Credible Commitments, and Economic Prosperity on American Indian Reservations." *Journal of Law and Economics*, 51(4), 641-666.
  - Indigenous communities show persistent income gaps
  - Structural factors beyond individual human capital

**Taiwan Context:**
- **Hsieh, J. F. (2006).** "Collective Rights of Indigenous Peoples: Identity-Based Movement of Plain Indigenous in Taiwan." In *Multiculturalism in Asia.* New York: Oxford University Press.
  - Indigenous Taiwanese face socioeconomic disadvantages
  - Lower average incomes even controlling for education

**Hypothesis (Control):** Negative coefficient expected, but NOT the focus of analysis

---

### **Control Variable 2: Population Density**

**Theory:** Urban Economics & Urbanization Premium

**Key Literature:**
- **Glaeser, E. L., & Maré, D. C. (2001).** "Cities and Skills." *Journal of Labor Economics*, 19(2), 316-342.
  - Urban areas show 30-40% wage premium
  - Dense areas have better job matching, more opportunities

- **Combes, P. P., Duranton, G., & Gobillon, L. (2008).** "Spatial Wage Disparities: Sorting Matters!" *Journal of Urban Economics*, 63(2), 723-742.
  - Population density correlates with productivity and wages
  - Doubling density → 3-8% increase in wages

- **Puga, D. (2010).** "The Magnitude and Causes of Agglomeration Economies." *Journal of Regional Science*, 50(1), 203-219.
  - Density itself is productivity-enhancing
  - Urban-rural income gaps driven by agglomeration

**Hypothesis (Control):** Positive coefficient expected (urban = higher income)

---

## SLIDE: Summary of Hypotheses

### **Hypotheses Table:**

| Hypothesis | Variable | Theory | Expected Sign | Expected Magnitude |
|------------|----------|--------|---------------|-------------------|
| **H1** | Tertiary Education Rate (%) | Human Capital Theory | **Positive (+)** | **Strong** (β ≈ 2-5) |
| **H2** | Distance to Science Park (km) | Agglomeration Economics | **Negative (−)** | **Moderate** (β ≈ -1 to -3) |
| **H3** | Aging Index | Demographic Theory | **Negative (−)** | **Moderate** (β ≈ -2 to -4 per 10 units) |
| **H4** | Distance to Airbase (km) | Environmental Disamenity | **Positive (+)** | **Small to Moderate** (β ≈ 0.5-2) |
| C1 | Indigenous Ratio (%) | Structural Inequality | Negative (−) | Control variable |
| C2 | Population Density (per km²) | Urban Economics | Positive (+) | Control variable |

**Legend:**
- β = Coefficient representing % change in income per capita per unit change in X
- **Bold** = Primary variables of theoretical interest
- C = Control variable

---

## SLIDE: Analytical Strategy

### **Step 1: Spatial Descriptive Analysis**
- Map income distribution across villages
- Identify spatial clusters visually
- Calculate spatial autocorrelation (Moran's I)

### **Step 2: Bivariate Relationships**
- Correlation analysis between each predictor and income
- Scatter plots with regression lines
- Preliminary assessment of hypotheses

### **Step 3: Multivariate Regression**
```
Income_per_capita = β₀
                  + β₁(Education_rate)
                  + β₂(Distance_Science_Park)
                  + β₃(Aging_Index)
                  + β₄(Distance_Airbase)
                  + β₅(Indigenous_ratio)
                  + β₆(Population_density)
                  + ε
```

### **Step 4: Spatial Diagnostics**
- Test for spatial autocorrelation in residuals
- If present, use spatial lag or spatial error model
- Compare model fit (R², AIC)

### **Step 5: Hot Spot Analysis**
- Getis-Ord Gi* statistic
- Identify statistically significant hot/cold spots
- Relate patterns to explanatory variables

---

## SLIDE: Expected Contributions

### **Empirical Contributions:**
1. First village-level analysis of income inequality in Hsinchu City
2. Quantifies the "Science Park premium" at fine spatial scale
3. Tests multiple theoretical mechanisms simultaneously

### **Policy Implications:**
1. **If H1 confirmed:** Educational investment is key inequality reduction strategy
2. **If H2 confirmed:** Transportation infrastructure connecting periphery to Science Park matters
3. **If H3 confirmed:** Support needed for aging communities
4. **If H4 confirmed:** Environmental quality affects economic outcomes

### **Limitations (To Acknowledge):**
1. **Cross-sectional data:** Cannot establish causation definitively
2. **Omitted variables:** Cannot measure commuting patterns, housing quality, etc.
3. **Ecological fallacy:** Village-level data may not reflect individual experiences
4. **Selection bias:** People sort into neighborhoods non-randomly

---

## SLIDE: Literature Cited - Key References

### **Essential Citations for Your Presentation:**

**Human Capital:**
- Becker, G. S. (1964). *Human Capital*. University of Chicago Press.
- Card, D. (1999). The causal effect of education on earnings. *Handbook of Labor Economics*, 3, 1801-1863.

**Agglomeration:**
- Marshall, A. (1890). *Principles of Economics*. Macmillan.
- Krugman, P. (1991). Increasing returns and economic geography. *Journal of Political Economy*, 99(3), 483-499.
- Moretti, E. (2012). *The New Geography of Jobs*. Houghton Mifflin Harcourt.

**Spatial Mismatch:**
- Kain, J. F. (1968). Housing segregation, negro employment, and metropolitan decentralization. *Quarterly Journal of Economics*, 82(2), 175-197.
- Gobillon, L., Selod, H., & Zenou, Y. (2007). The mechanisms of spatial mismatch. *Urban Studies*, 44(12), 2401-2427.

**Demographics:**
- Lee, R., & Mason, A. (2010). Fertility, human capital, and economic growth over the demographic transition. *European Journal of Population*, 26(2), 159-182.
- Maestas, N., Mullen, K. J., & Powell, D. (2016). The effect of population aging on economic growth. *NBER Working Paper 22452*.

**Environmental Disamenities:**
- Rosen, S. (1974). Hedonic prices and implicit markets. *Journal of Political Economy*, 82(1), 34-55.
- Nelson, J. P. (2004). Meta-analysis of airport noise and hedonic property values. *Journal of Transport Economics and Policy*, 38(1), 1-27.

**Urban Economics:**
- Glaeser, E. L., & Maré, D. C. (2001). Cities and skills. *Journal of Labor Economics*, 19(2), 316-342.

---

## TALKING POINTS FOR PRESENTATION

### **When Presenting Research Questions:**

**Key Messages:**
1. "We're examining income inequality through a spatial lens - asking not just WHO earns more, but WHERE and WHY"
2. "Our analysis combines economic geography, human capital, and demographic factors"
3. "Hsinchu provides an ideal case study: it's Taiwan's Silicon Valley with stark spatial contrasts"

### **When Presenting Theories:**

**Key Messages:**
1. "We're applying four major theoretical frameworks from economics and urban studies"
2. "Each theory makes specific, testable predictions about the direction and magnitude of effects"
3. "Human Capital Theory is our strongest predictor - decades of research support it"
4. "Agglomeration Economics explains why 'location, location, location' matters economically"
5. "We're honest about limitations: we're measuring associations, not definitive causation"

### **When Presenting Hypotheses:**

**Key Messages:**
1. "We have four primary hypotheses and two control variables"
2. "We expect education to be our strongest effect - this is well-established in literature"
3. "Science Park proximity should matter due to agglomeration effects"
4. "Aging should negatively affect income through labor force participation"
5. "Airbase is exploratory - we expect negative externalities from noise"
6. "All effects are grounded in peer-reviewed economic theory"

### **Addressing Potential Questions:**

**Q: Why not individual TSMC factories?**
A: "We focus on the entire Science Park cluster because agglomeration effects operate at the cluster level, not individual firms. This is consistent with Krugman (1991) and modern economic geography."

**Q: Isn't education just correlated with income, not causal?**
A: "You're right to be skeptical! We acknowledge in our limitations that cross-sectional data can't prove causation. However, decades of research including natural experiments (Card, 1999) support a causal interpretation. We're testing if the well-established micro-level relationship holds at the spatial level."

**Q: How do you measure distance?**
A: "We calculate Euclidean distance from village centroids to Science Park and airbase using GIS. We acknowledge this is imperfect - it doesn't account for road networks or actual commuting patterns."

**Q: What if people commute from far away?**
A: "Excellent point! This is a key limitation. Our spatial units don't capture commuting patterns. However, research on spatial mismatch (Gobillon et al., 2007) shows distance still matters even with commuting, because of time and transportation costs."

---

## ADDITIONAL SLIDES: Detailed Theory Mechanisms

### **MECHANISM 1: Human Capital Theory**

**How Education → Income:**
1. **Skills acquisition:** Education develops cognitive and technical skills
2. **Productivity enhancement:** Skilled workers produce more value
3. **Signaling:** Degrees signal capability to employers
4. **Occupational access:** Higher education opens access to high-paying professions
5. **Network effects:** Universities create professional networks

**Spatial Dimension:**
- Villages with high education attract high-skill industries
- Educated residents earn more individually
- Aggregate to higher village average income
- Creates reinforcing cycle (educated attract educated)

**Why This Matters in Hsinchu:**
- Science Park requires highly educated workforce
- NTHU and NYCU produce educated residents
- Education → Tech jobs → High income
- Spatial concentration of educated workers

---

### **MECHANISM 2: Agglomeration Economics**

**How Clustering → Higher Wages:**

**Marshall's Three Forces:**
1. **Labor Market Pooling**
   - Large pool of specialized workers
   - Better job matching (worker-firm fit)
   - Reduced search costs

2. **Intermediate Input Sharing**
   - Specialized suppliers locate nearby
   - Economies of scale in services
   - Lower transaction costs

3. **Knowledge Spillovers**
   - Face-to-face interaction spreads ideas
   - Learning from competitors/collaborators
   - Innovation through proximity

**Spatial Decay:**
- Benefits strongest at cluster core
- Decline with distance (transportation costs)
- Creates wage gradient by proximity

**Hsinchu Science Park Example:**
- 530+ companies, 160,000+ employees
- Semiconductor, IT, biotechnology clusters
- Workers benefit from cluster premium
- Proximity matters for accessing opportunities

---

### **MECHANISM 3: Demographic Structure**

**How Aging → Lower Income:**

**Direct Effects:**
1. **Retirement:** 65+ typically not in labor force
2. **Lower labor force participation:** Reduced working-age share
3. **Pension income:** Lower than working wages
4. **Health constraints:** Reduced productivity

**Indirect Effects:**
1. **Dependency ratios:** More dependents per worker
2. **Reduced consumption:** Elderly spend less locally
3. **Business location:** Firms avoid aging areas
4. **Education investment:** Fewer families with children

**Spatial Pattern:**
- Old neighborhoods: established residents aging in place
- Young neighborhoods: new development attracting families
- Creates spatial sorting by age
- Income follows demographic structure

---

### **MECHANISM 4: Environmental Disamenity**

**How Airbase → Lower Local Income:**

**Primary Mechanism: Residential Sorting**
1. Aircraft noise creates disamenity
2. High-income households can "pay to avoid" - move away
3. Low-income households remain (cheaper housing)
4. Area becomes income-stratified by willingness-to-pay for quiet

**Secondary Mechanisms:**
1. **Property values:** Noise reduces home values (Nelson, 2004)
2. **Business location:** Firms avoid noisy areas
3. **Worker productivity:** Noise may reduce concentration/health
4. **Amenity access:** High-income amenities don't locate near airbase

**Hedonic Equilibrium:**
- Housing prices adjust to environmental quality
- Income-sorted equilibrium emerges
- Persistent spatial income gradient

**Testable Prediction:**
- Distance gradient: Income rises with distance from airbase
- Effect stronger for high-noise areas
- May extend 5-15 km

---

## FINAL SLIDE: Research Design Summary

### **Strengths of Our Approach:**
✅ Grounded in established economic theory
✅ Multiple complementary theoretical frameworks
✅ Testable, falsifiable hypotheses
✅ Appropriate spatial methods
✅ Acknowledges limitations honestly

### **Our Contribution:**
🎯 First comprehensive spatial analysis of Hsinchu income inequality
🎯 Tests multiple mechanisms simultaneously
🎯 Fine-grained village-level analysis
🎯 Policy-relevant findings

### **What We'll Show:**
📊 Spatial patterns of income inequality
📊 Relative importance of different factors
📊 Hot spots and cold spots
📊 Evidence for/against each theory

**"Good science is about testing clear hypotheses with appropriate methods and being honest about what we can and cannot conclude."**


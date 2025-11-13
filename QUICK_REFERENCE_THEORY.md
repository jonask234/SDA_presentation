# Quick Reference: Theories and Hypotheses

## One-Page Summary for Your Presentation

---

## Research Question
**What spatial and socioeconomic factors explain income inequality across villages in Hsinchu City?**

---

## Theoretical Framework & Hypotheses

| Variable | Theory | Key Citation | Expected Effect | Mechanism |
|----------|--------|--------------|-----------------|-----------|
| **Tertiary Education Rate** | Human Capital Theory | Becker (1964); Card (1999) | ✅ **Positive (+)** | Education → Skills → Productivity → Higher wages |
| **Distance to Science Park** | Agglomeration Economics | Krugman (1991); Moretti (2012) | ❌ **Negative (−)** | Proximity to tech cluster → Knowledge spillovers → Wage premium |
| **Aging Index** | Demographic Theory | Lee & Mason (2010); Maestas et al. (2016) | ❌ **Negative (−)** | More elderly → Lower labor force participation → Lower income |
| **Distance to Airbase** | Environmental Disamenity | Rosen (1974); Nelson (2004) | ✅ **Positive (+)** | Noise pollution → High-income households sort away → Income gradient |
| Indigenous Ratio (Control) | Structural Inequality | Cornell & Kalt (1992) | ❌ Negative (−) | Historical disadvantage |
| Population Density (Control) | Urban Economics | Glaeser & Maré (2001) | ✅ Positive (+) | Urban agglomeration premium |

---

## Key Talking Points

### **For Slide 1: Research Questions**
- "We're examining WHERE income inequality exists and WHY"
- "Combining economic geography, human capital, and demographics"
- "Hsinchu is ideal: Taiwan's Silicon Valley with spatial contrasts"

### **For Slide 2: Theories**

**Human Capital (STRONGEST):**
- "60+ years of research: education is the most robust predictor of income"
- "Each additional year of education → 10% higher earnings (Mincer, 1974)"
- "We expect this to be our strongest effect"

**Agglomeration Economics:**
- "Location matters economically - Nobel Prize work (Krugman)"
- "Tech clusters create wage premiums through knowledge spillovers"
- "Hsinchu Science Park is the economic engine - proximity should matter"

**Demographics:**
- "Aging populations have lower labor force participation"
- "Areas with more elderly → lower average income"
- "Taiwan is rapidly aging - this is policy-relevant"

**Environmental Disamenity:**
- "High-income households 'vote with their feet' - avoid noise pollution"
- "Airbase creates negative externality"
- "Meta-analysis: airports reduce nearby property values by 5-15% (Nelson, 2004)"

### **For Slide 3: Hypotheses**
- "Four primary hypotheses, each grounded in established theory"
- "We expect education to dominate - strongest effect"
- "All predictions are directional and testable"
- "We acknowledge limitations: this is spatial association, not definitive causation"

---

## Regression Model

```
Income_per_capita = β₀
                  + β₁(Education_rate)              [H1: β₁ > 0, STRONG]
                  + β₂(Distance_to_Science_Park)   [H2: β₂ < 0]
                  + β₃(Aging_Index)                 [H3: β₃ < 0]
                  + β₄(Distance_to_Airbase)         [H4: β₄ > 0]
                  + β₅(Indigenous_ratio)            [Control]
                  + β₆(Population_density)          [Control]
                  + ε
```

---

## Essential Citations (Memorize These!)

**Must-cite for each theory:**

1. **Human Capital:**
   - Becker, G. S. (1964). *Human Capital*. University of Chicago Press.

2. **Agglomeration:**
   - Krugman, P. (1991). Increasing returns and economic geography. *Journal of Political Economy*, 99(3), 483-499.

3. **Demographics:**
   - Lee, R., & Mason, A. (2010). Fertility, human capital, and economic growth. *European Journal of Population*, 26(2), 159-182.

4. **Environmental:**
   - Nelson, J. P. (2004). Meta-analysis of airport noise and hedonic property values. *Journal of Transport Economics and Policy*, 38(1), 1-27.

---

## Anticipated Questions & Answers

**Q: Why not causation?**
**A:** "Cross-sectional data limits causal inference. We're testing if patterns are consistent with theory. Card (1999) shows education is causal in micro data; we test if this holds spatially."

**Q: Why not individual TSMC factories?**
**A:** "Agglomeration effects operate at cluster level (Krugman, 1991). Science Park is the relevant economic unit."

**Q: What about commuting?**
**A:** "Good point - this is a limitation. Gobillon et al. (2007) show distance matters even with commuting due to time/cost."

**Q: Expected effect sizes?**
**A:** "Education should dominate (β ≈ 2-5%). Science Park distance moderate (β ≈ -1 to -3%). Aging moderate (β ≈ -2 to -4% per 10 units). Airbase smaller (β ≈ 0.5-2%)."

---

## Key Locations in Hsinchu

**Hsinchu Science Park (新竹科學工業園區):**
- Location: East District, near National Chiao Tung University
- Established: 1980
- 530+ companies, 160,000+ employees
- Focus: Semiconductors (TSMC), IT, biotech
- Taiwan's highest concentration of engineers/PhDs

**Hsinchu Air Base (新竹空軍基地):**
- Location: North District
- Active military installation (ROCAF)
- Fighter aircraft operations
- Noise exposure area extends several kilometers

**Major Universities:**
- National Tsing Hua University (NTHU) - East District
- National Yang Ming Chiao Tung University (NYCU) - East District
- Both produce highly educated workforce for Science Park

---

## Expected Patterns (Before Analysis)

**Based on theory, we predict:**

📍 **Highest income villages:** East District, near Science Park
- High education rates
- Close to Science Park
- Low aging index
- High population density
- Far from airbase

📍 **Lowest income villages:** Xiangshan District, peripheral areas
- Lower education rates
- Far from Science Park
- High aging index
- Low population density
- Possibly near airbase

**If findings match predictions → Theories supported**
**If not → Need to explain why (important for discussion!)**

---

## Limitations to Acknowledge

**Be proactive about these:**

1. **Cross-sectional:** Cannot prove causation
2. **Omitted variables:** Can't measure commuting, housing quality
3. **Ecological fallacy:** Village averages may not reflect individuals
4. **Selection bias:** People sort non-randomly into neighborhoods
5. **Measurement error:** Euclidean distance approximates but doesn't capture actual commuting
6. **Static snapshot:** No temporal dynamics

**Frame positively:**
"Despite limitations, our analysis provides valuable evidence about spatial patterns consistent with established theory, with clear policy implications."

---

## Policy Implications (Preview)

**If hypotheses supported:**

✅ **Education Investment:** Strongest lever for reducing inequality
- Improve educational access in peripheral areas
- Support lifelong learning programs

✅ **Transportation Infrastructure:** Connect periphery to Science Park
- Reduce effective distance through better transit
- Address spatial mismatch

✅ **Aging Support:** Policies for aging communities
- Active aging programs
- Economic development for areas with high aging index

✅ **Environmental Quality:** Address disamenity exposure
- Noise mitigation near airbase
- Compensation or development incentives

---

## Confidence Levels (What to Emphasize)

**High confidence (emphasize these):**
- ✅ Education → Income relationship (60+ years of research)
- ✅ Spatial clustering exists (we can show this definitively)

**Moderate confidence:**
- ⚠️ Science Park proximity matters (good theory, need to show empirically)
- ⚠️ Aging affects income (well-established, but complex mechanism)

**Lower confidence (exploratory):**
- ❓ Airbase effect (plausible but less studied in Taiwan context)
- Acknowledge this as exploratory

**Strategy:** Lead with strong findings, acknowledge uncertainty on weaker ones

---

## Presentation Flow

1. **Problem:** Income inequality exists spatially in Hsinchu
2. **Question:** What factors explain this pattern?
3. **Theory:** Four established theoretical frameworks make predictions
4. **Hypotheses:** Specific, testable predictions
5. **Methods:** Spatial analysis + regression
6. **Results:** [Your empirical findings]
7. **Discussion:** What do findings mean for theory and policy?
8. **Limitations:** Honest about what we can/cannot conclude
9. **Conclusion:** Evidence supports [X, Y, Z] theories

---

## Visual Summary

```
INCOME INEQUALITY IN HSINCHU
         ↓
    WHY? WHERE?
         ↓
┌────────────────────────────────┐
│  FOUR THEORETICAL MECHANISMS:  │
├────────────────────────────────┤
│ 1. HUMAN CAPITAL (Education)   │ ← STRONGEST
│ 2. AGGLOMERATION (Sci Park)    │
│ 3. DEMOGRAPHICS (Aging)         │
│ 4. DISAMENITY (Airbase)        │ ← EXPLORATORY
└────────────────────────────────┘
         ↓
   TEST WITH DATA
         ↓
    RESULTS → POLICY
```

---

**Print this page and keep it with you during the presentation!**

# Three-Slide Summary: Research Questions, Theory & Hypotheses
## Hsinchu City Income Inequality Analysis

---

## SLIDE 1: Research Question and Reasoning

### **Main Research Question**
**What spatial and socioeconomic factors explain income inequality across villages in Hsinchu City?**

### **Why This Matters**

**1. Geographic Context:**
- Hsinchu = Taiwan's "Silicon Valley" (Science Park, TSMC, 160,000+ tech workers)
- Stark spatial contrasts: High-tech core vs. traditional periphery
- 122 villages, income range: 138,000 - 1,202,000 TWD per capita (8.7x difference!)

**2. Policy Relevance:**
- Identify specific factors driving inequality → Target interventions
- Guide urban planning and infrastructure investment
- Address aging society challenges

**3. Scientific Contribution:**
- First village-level spatial analysis of Hsinchu income
- Tests multiple economic theories simultaneously
- Fine-grained spatial resolution reveals local patterns

### **Analytical Approach**
```
Income Inequality = f(Human Capital + Economic Geography + Demographics + Controls)
```

---

## SLIDE 2: Theoretical Background

### **Four Theoretical Frameworks**

| Theory | Core Mechanism | Key Citation | Application to Hsinchu |
|--------|----------------|--------------|------------------------|
| **1. Human Capital Theory** | Education → Skills → Productivity → Higher Income | Becker (1964); Card (1999) | Villages with higher tertiary education rates should have higher income |
| **2. Agglomeration Economics** | Geographic clustering → Knowledge spillovers → Wage premium | Krugman (1991); Moretti (2012) | Proximity to Science Park → Access to high-wage opportunities |
| **3. Demographic Theory** | Population aging → Lower labor force participation → Reduced income | Lee & Mason (2010); Maestas et al. (2016) | Villages with higher Aging Index → Lower average income |
| **4. Environmental Disamenity** | Noise pollution → Residential sorting → Income stratification | Rosen (1974); Nelson (2004) | Airbase proximity → Negative externality → Lower local income |

### **Why These Theories?**

**Empirical Support:**
- Human Capital: 60+ years of consistent findings (10% wage return per education year)
- Agglomeration: Tech clusters create 30-40% wage premiums (Glaeser & Maré, 2001)
- Aging: 10% increase in 60+ population → 5.5% GDP decrease (Maestas et al., 2016)
- Disamenity: Airports reduce property values 5-15% within 10km (Nelson, 2004)

**Spatial Applicability:**
- All theories predict spatial patterns testable with village-level data
- Complementary mechanisms (not competing explanations)
- Policy-relevant if confirmed

---

## SLIDE 3: Hypotheses

### **Regression Model**
```
Income_per_capita = β₀ + β₁(Education) + β₂(Dist_SciPark) + β₃(Aging) + β₄(Dist_Airbase) + β₅(Indigenous) + β₆(PopDensity) + ε
```

### **Testable Hypotheses**

| H# | Variable | Theory | Expected Sign | Expected Magnitude | Rationale |
|----|----------|--------|---------------|-------------------|-----------|
| **H1** | **Tertiary Education Rate (%)** | Human Capital | **Positive (+)** | **Strong** (β ≈ 2-5) | Each 1% increase in education → 2-5% higher income. Strongest predictor in literature. |
| **H2** | **Distance to Science Park (km)** | Agglomeration | **Negative (−)** | **Moderate** (β ≈ -1 to -3) | Each 1km farther → 1-3% lower income. Proximity captures cluster benefits. |
| **H3** | **Aging Index** | Demographics | **Negative (−)** | **Moderate** (β ≈ -0.2 to -0.4 per unit) | Higher aging → More retirees → Lower average income. |
| **H4** | **Distance to Airbase (km)** | Environmental | **Positive (+)** | **Small** (β ≈ 0.5-2) | Farther from noise → Higher income. High-income households sort away. |
| C1 | Indigenous Ratio (%) | Structural Inequality | Negative (−) | Control | Historical disadvantage |
| C2 | Population Density (per km²) | Urban Economics | Positive (+) | Control | Urban wage premium |

### **Key Points**

**Emphasis:**
- **H1 (Education)** is our strongest hypothesis - most robust in literature
- **H2 (Science Park)** directly tests Hsinchu's tech cluster effect
- **H3 (Aging)** is policy-relevant for Taiwan's demographic transition
- **H4 (Airbase)** is exploratory - testing environmental justice hypothesis

**Limitations Acknowledged:**
- Cross-sectional data → Cannot prove causation (association only)
- Commuting not observed → Distance proxies may underestimate effects
- Omitted variables → Results suggestive, not definitive
- Ecological fallacy → Village averages may not reflect individuals

---

## TALKING POINTS FOR EACH SLIDE

### **Slide 1 - What to Say (60 seconds):**

"Our research question asks: What factors explain income inequality in Hsinchu City? This matters for three reasons:

First, Hsinchu is Taiwan's Silicon Valley with extreme spatial contrasts - the richest village earns 8.7 times more than the poorest.

Second, understanding these patterns has direct policy implications for urban planning and addressing inequality.

Third, scientifically, this is the first fine-grained spatial analysis at the village level, testing multiple economic theories simultaneously.

We're examining how human capital, economic geography, and demographics shape income patterns across 122 villages."

---

### **Slide 2 - What to Say (90 seconds):**

"We apply four major theoretical frameworks from economics:

First, Human Capital Theory - pioneered by Nobel laureate Gary Becker - predicts education increases income through skill development. This is the most robust finding in labor economics with 60 years of evidence.

Second, Agglomeration Economics - Paul Krugman's Nobel Prize work - explains why tech clusters create wage premiums through knowledge spillovers. Proximity to Hsinchu Science Park should matter.

Third, Demographic Theory predicts aging populations have lower income due to retirement and reduced labor force participation. This is especially relevant as Taiwan rapidly ages.

Fourth, Environmental Economics predicts that disamenities like noise create income stratification as high-income households avoid them.

Each theory makes specific, testable spatial predictions we can evaluate with our data."

---

### **Slide 3 - What to Say (90 seconds):**

"We test four primary hypotheses, each grounded in established theory:

H1: Education shows a strong positive effect. We expect each 1% increase in tertiary education rate to raise income by 2-5%. This is our strongest prediction based on six decades of research.

H2: Distance to Science Park shows a negative effect. Villages farther from the tech cluster should have 1-3% lower income per kilometer, due to reduced access to high-wage opportunities.

H3: Aging Index shows a negative effect. Areas with more elderly residents should have lower average income due to retirement.

H4: Distance to the airbase shows a positive effect - farther from aircraft noise should correlate with higher income as wealthy households sort away.

We control for indigenous population and urban density.

Importantly, we acknowledge our cross-sectional data limits causal inference - we're testing if spatial patterns are consistent with theory, which provides suggestive evidence for mechanisms."

---

## VISUAL LAYOUT SUGGESTIONS

### **Slide 1 Layout:**
```
┌─────────────────────────────────────────┐
│  RESEARCH QUESTION & REASONING          │
├─────────────────────────────────────────┤
│  Main Question: [bold, large font]      │
│                                          │
│  Why This Matters:                      │
│  ┌───────────────────────────────────┐  │
│  │ 🗺️  Geographic: Hsinchu context   │  │
│  │ 📊 Policy: Target interventions   │  │
│  │ 🔬 Science: First village analysis│  │
│  └───────────────────────────────────┘  │
│                                          │
│  Analytical Approach: [formula]         │
└─────────────────────────────────────────┘
```

### **Slide 2 Layout:**
```
┌─────────────────────────────────────────┐
│  THEORETICAL BACKGROUND                 │
├─────────────────────────────────────────┤
│  Four Frameworks: [table format]        │
│  ┌─────────────────────────────────┐   │
│  │ Theory | Mechanism | Citation   │   │
│  │ [Human Capital] ✅ STRONGEST    │   │
│  │ [Agglomeration]                 │   │
│  │ [Demographics]                  │   │
│  │ [Environmental]                 │   │
│  └─────────────────────────────────┘   │
│                                          │
│  Why These? Empirical support + Spatial │
└─────────────────────────────────────────┘
```

### **Slide 3 Layout:**
```
┌─────────────────────────────────────────┐
│  HYPOTHESES                             │
├─────────────────────────────────────────┤
│  Model: [equation at top]               │
│                                          │
│  Hypotheses: [table with 4 rows]       │
│  ┌─────────────────────────────────┐   │
│  │ H1: Education (+) ✅ STRONG      │   │
│  │ H2: Sci Park (-)                 │   │
│  │ H3: Aging (-)                    │   │
│  │ H4: Airbase (+)                  │   │
│  └─────────────────────────────────┘   │
│                                          │
│  Note: Cross-sectional → Association    │
└─────────────────────────────────────────┘
```

---

## KEY CITATIONS TO INCLUDE ON SLIDES

### **Slide 2 (References):**
- Becker, G. S. (1964). *Human Capital*. Univ. Chicago Press.
- Krugman, P. (1991). Increasing returns and economic geography. *JPE*, 99(3).
- Lee, R., & Mason, A. (2010). Fertility and economic growth. *Eur J Population*, 26(2).
- Nelson, J. P. (2004). Airport noise and hedonic property values. *JTEP*, 38(1).

### **Slide 3 (Reference note):**
"All hypotheses grounded in peer-reviewed literature. See full references in appendix."

---

## COLOR CODING SUGGESTION

**Use consistent colors across slides:**
- 🟢 **Green** = Positive expected effects (H1, H4)
- 🔴 **Red** = Negative expected effects (H2, H3)
- ⚫ **Gray** = Control variables
- 🟡 **Yellow highlight** = Strongest effect (H1: Education)

---

## FONT SIZE RECOMMENDATIONS

**For 3-slide limit (needs to be readable!):**
- Slide titles: **32-36pt bold**
- Main headers: **24-28pt bold**
- Body text: **18-20pt** (no smaller!)
- Table text: **16-18pt**
- Citations: **14pt**

**Less is more** - Use bullet points, not paragraphs!

---

## WHAT TO CUT (Too detailed for slides)

❌ **DO NOT include on slides:**
- Detailed mechanisms (save for verbal explanation)
- Multiple citations per theory (just 1 key citation each)
- Effect size ranges (just say "strong/moderate/small")
- Long explanations of limitations (mention briefly)
- Literature review details (save for Q&A)

✅ **DO include on slides:**
- Core concepts only
- Key citations (1 per theory)
- Clear hypothesis directions
- Expected relative magnitudes
- Visual table format

---

## BACKUP SLIDE (Optional 4th slide for Q&A)

**If allowed, prepare this for questions:**

### **Detailed Literature Support**

**Human Capital:**
- Mincer (1974): 10% wage return per education year
- Card (1999): Causal evidence, 5-15% returns
- Psacharopoulos & Patrinos (2018): 50-100% bachelor's premium in Asia

**Agglomeration:**
- Glaeser et al. (1992): Industrial clusters drive growth
- Moretti (2012): 5 service jobs per tech job
- Saxenian (1994): Silicon Valley regional advantage

**Demographics:**
- Maestas et al. (2016): 10% aging → 5.5% GDP decrease
- Bloom et al. (2010): Dependency ratios reduce income

**Environmental:**
- McMillen (2004): 9% property value decrease near airports
- Cohen & Coughlin (2008): 10-15km effect radius

---

## FINAL CHECKLIST

**Before presenting, verify slides have:**
- ✅ Clear research question (Slide 1)
- ✅ Four theories with 1 citation each (Slide 2)
- ✅ Four hypotheses with expected signs (Slide 3)
- ✅ Acknowledgment of limitations (Slide 3 bottom)
- ✅ Consistent visual formatting
- ✅ No text smaller than 16pt
- ✅ Professional color scheme
- ✅ Tables for easy scanning

**Verbal presentation should:**
- ✅ Take 3-4 minutes total (60-90 sec per slide)
- ✅ Emphasize education as strongest predictor
- ✅ Explain WHY each theory matters
- ✅ Acknowledge cross-sectional limitations
- ✅ Connect to Hsinchu context throughout

---

## EMERGENCY ANSWER FOR TOUGH QUESTIONS

**Q: "How can you claim causation?"**
**A:** "We don't claim definitive causation - our cross-sectional design limits this. However, we test if spatial patterns are *consistent* with causal theories that have been established using experimental and quasi-experimental methods in other contexts, like Card's (1999) natural experiments on education."

**Q: "Why not [other variable]?"**
**A:** "Good suggestion! We're constrained by available data. Our framework captures the major theoretical mechanisms in the literature, but future work could incorporate [housing prices/commuting patterns/etc.] if data become available."

**Q: "What if people commute far?"**
**A:** "This is a key limitation we acknowledge. Distance-to-opportunity measures like ours are imperfect proxies. However, research on spatial mismatch (Gobillon et al., 2007) shows that even with commuting, distance still matters due to time and transportation costs."

---

**Print this document and practice presenting from it!**

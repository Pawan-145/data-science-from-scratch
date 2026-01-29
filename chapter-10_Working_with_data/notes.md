# 📘 Chapter 10 — Working with Data (Notes)

This chapter explains how to explore, visualize, clean, transform, and reduce data using Python.
All techniques are implemented from scratch to understand real data science workflows.

---

## ✅ 1. One-Dimensional Data

### ▶ Bucketization

Bucketization groups continuous values into fixed-size intervals.

Formula:
bucket = bucket_size × floor(point / bucket_size)

Purpose:
- Helps convert continuous data into frequency counts.

---

### ▶ Histogram

Histogram shows how many values fall into each bucket.

Steps:
1. Bucketize each data point
2. Count frequencies using Counter
3. Plot using bar graph

Used to compare:
- Uniform distribution
- Normal distribution

---

### ▶ Uniform Distribution

Generated using:
random.random()

Range:
-100 to +100

Properties:
- All values equally likely
- Flat histogram

---

### ▶ Normal Distribution

Generated using inverse CDF method.

Normal CDF Formula:
CDF(x) = (1 + erf((x − μ) / (√2 σ))) / 2

Inverse CDF:
Found using binary search.

Properties:
- Bell-shaped curve
- Most values near mean

---

## ✅ 2. Two-Dimensional Data

Purpose:
Study how two variables behave together.

Examples:
ys1 = x + noise → positive correlation  
ys2 = -x + noise → negative correlation

Even if histograms look similar,
scatter plots show very different relationships.

Tool:
Scatter plot using matplotlib.

---

## ✅ 3. Statistical Functions

### ▶ Mean
Average of values.

### ▶ Variance
Measures spread of data.

Variance = sum((x − mean)²) / (n − 1)

---

### ▶ Standard Deviation
Square root of variance.

Shows typical distance from mean.

---

### ▶ Covariance

Measures how two variables move together.

Positive:
Both increase together.

Negative:
One increases, other decreases.

---

### ▶ Correlation

Normalized covariance.

Range:
-1 to +1

Meaning:
+1 → perfect positive relation  
-1 → perfect negative relation  
0 → no relation

---

## ✅ 4. Many-Dimensional Data

### ▶ Correlation Matrix

Matrix where:
Entry (i, j) = correlation between dimension i and j.

Purpose:
- Detect related features
- Understand high-dimensional relationships

---

### ▶ Scatter Plot Matrix

Grid of scatter plots between every pair of variables.

Diagonal:
Shows series labels.

Used for:
Visual inspection of correlations.

---

## ✅ 5. Structured Data Representation

### ▶ Dictionary

Stores data as:
key → value

Example:
Stock data using keys like symbol, date, price.

---

### ▶ NamedTuple

Advantages:
- Immutable
- Access using dot notation
- Can have methods

Used for:
Safe data storage.

---

### ▶ Dataclass

Advantages:
- Mutable
- Cleaner syntax
- Can modify fields

Used when:
Data values can change (stock split).

---

## ✅ 6. Data Cleaning and Parsing

Real-world data often contains:

- Wrong symbols
- Invalid dates
- Missing numbers

---

### ▶ Safe Parsing Strategy

Steps:
1. Validate symbol using regex
2. Parse date using dateutil
3. Convert price to float
4. Use try/except

If any step fails → return None

Prevents:
Crashes and wrong analysis.

---

### ▶ CSV Data Handling

Steps:
1. Read rows from CSV
2. Validate each row
3. Skip invalid rows
4. Store only valid stock prices

---

## ✅ 7. Data Manipulation

### ▶ Maximum Price Per Stock

Find highest closing price for each company.

Uses:
defaultdict

---

### ▶ Daily Percent Change

Formula:
(today − yesterday) / yesterday

Purpose:
Measure daily stock movement.

---

### ▶ Best and Worst Trading Days

From daily changes:
- Max change → best day
- Min change → worst day

---

### ▶ Monthly Investment Analysis

Steps:
1. Group daily changes by month
2. Compute average monthly change
3. Best month = highest average

Used to detect seasonal trends.

---

## ✅ 8. Data Rescaling

Problem:
Different features may have different units.

Solution:
Standardization

Goal:
Each feature should have:
- Mean = 0
- Standard deviation = 1

Formula:
z = (x − mean) / std

Benefits:
- Fair comparison
- Required for ML algorithms

---

## ✅ 9. tqdm Progress Bar

Used when loops take long time.

Shows:
- Percentage complete
- Speed
- Time remaining

Used in:
- Large loops
- Prime number generation

Helps track slow computations.

---

## ✅ 10. Principal Component Analysis (PCA)

Purpose:
Reduce dimensions while keeping maximum information.

Example:
2D → 1D

---

### ▶ PCA Steps

1. Compute mean of each dimension
2. Subtract mean from all data points
3. Find direction of maximum variance
4. Use gradient ascent to optimize direction
5. Project data onto that direction

---

### ▶ Principal Component

Direction where:
Variance of projected data is maximum.

Represents:
Most informative axis.

---

### ▶ Result

Data is compressed into fewer dimensions
without losing major patterns.

Used in:
- Visualization
- Noise reduction
- Feature compression

---

## ✅ Final Learning Summary

This chapter teaches that:

✔ Data visualization is essential  
✔ Cleaning data is unavoidable in real projects  
✔ Correlation reveals hidden relationships  
✔ Scaling improves model performance  
✔ PCA reduces complexity effectively  

Strong data understanding is the foundation of Machine Learning.

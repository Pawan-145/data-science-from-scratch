# 📈 Chapter 10 Results & Observations

## ✔ Distribution Analysis

### Uniform Distribution
- Values evenly spread
- Histogram shows flat structure

### Normal Distribution
- Bell-shaped curve
- High concentration near mean

Even though both had:
- Mean ≈ 0
- Std Dev ≈ 58

Their distributions were very different.

---

## ✔ Joint Distributions

### ys1 = x + noise
- Strong positive correlation

### ys2 = -x + noise
- Strong negative correlation

Histograms of ys1 and ys2 looked similar,
but scatter plots showed completely different relationships.

➡ Shows why joint visualization is important.

---

## ✔ Correlation Matrix

Example:

A and B:
- Strong positive correlation

A and C:
- Strong negative correlation

Matrix helps detect:
- Redundant features
- Opposite trends

---

## ✔ Data Cleaning Results

Invalid rows were skipped:
- Wrong symbols
- Invalid dates
- Non-numeric prices

Only valid rows were used for analysis.

This prevents:
- Model errors
- False results

---

## ✔ Stock Analysis

### Maximum Price
Computed highest closing price per company.

### Daily Change
Found:
- Best trading day
- Worst trading day

### Monthly Performance
Identified best month to invest in tech stocks.

---

## ✔ Rescaling Results

Before scaling:
- Features had different ranges

After scaling:
- Mean ≈ 0
- Std Dev ≈ 1

This prepares data for:
- Machine learning
- PCA
- Gradient-based models

---

## ✔ PCA Output

Original Data:
- 2D scatter plot

After PCA:
- Data projected onto 1D line
- Direction captures maximum variance

Red line shows:
First Principal Component direction

Meaning:
Most information preserved in single dimension.

---

## 🎯 Final Conclusion

This chapter demonstrated that:

✔ Data understanding is more important than algorithms  
✔ Visualization reveals hidden patterns  
✔ Cleaning is critical for real-world datasets  
✔ Scaling is necessary before ML  
✔ PCA reduces complexity without losing meaning  

This chapter builds strong foundations for Machine Learning.

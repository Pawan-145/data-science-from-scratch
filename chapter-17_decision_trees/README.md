# 🌳 Chapter 17 — Decision Trees & Random Forests

## 📌 Overview

This notebook implements **Decision Trees from scratch** using entropy and the **ID3 algorithm**, followed by a conceptual deep dive into **Random Forests** and ensemble learning.

The goal is to understand how machines make structured decisions by repeatedly splitting data into smaller subsets.

---

# 🎯 Objectives

✔ Understand entropy and information gain  
✔ Learn how datasets are partitioned  
✔ Build a decision tree classifier  
✔ Handle unknown attribute values  
✔ Explore overfitting  
✔ Understand Random Forest and bagging  

---

#  Concepts Covered

## Decision Trees
- Tree-based supervised learning
- Recursive splitting
- Leaf vs Split nodes

## Entropy
Measures impurity in data.

## Partition Entropy
Helps select the best feature for splitting.

## ID3 Algorithm
Builds trees by minimizing entropy.

## Overfitting
Major weakness of single trees.

## Random Forest
An ensemble technique that combines multiple trees to improve performance.

---

# ⚙ Implementation Highlights

The notebook includes:

-  Entropy computation  
-  Partitioning functions  
-  Recursive tree builder  
-  Classification logic  
-  Default handling for unseen values  

Assertions ensure correctness throughout.

---

# 🏗 Project Structure

- `chapter-17_decision_trees.ipynb`
- `notes.md`
- `results.md`

  
---

#  Key Learnings

- Lower entropy → better splits.
- Trees are interpretable but unstable.
- Random Forest dramatically improves reliability.

---

#  When to Use Decision Trees?

✔ When interpretability matters  
✔ When features are categorical  
✔ When preprocessing should be minimal  

---

# ⚠ When to Prefer Random Forest?

✔ When accuracy is critical  
✔ When dataset is noisy  
✔ When overfitting is likely  

---

#  Conclusion

This chapter demonstrates how powerful tree-based models are and why ensemble methods like Random Forest are widely used in production ML systems.

Understanding Decision Trees builds a strong foundation for advanced models such as:

- Gradient Boosting  
- XGBoost  
- LightGBM  

---




# 🌳 Chapter 17 — Decision Trees & Random Forests

## 📌 What is a Decision Tree?

A **Decision Tree** is a supervised machine learning algorithm that uses a tree-like structure to make decisions.

Each internal node represents a question about a feature, each branch represents an answer, and each leaf node represents the final prediction.

Think of it like a flowchart:

Start → Ask Question → Follow Branch → Reach Decision.

---

# 🔥 Entropy

Entropy measures the **uncertainty or impurity** in a dataset.

### Key Idea:
- If all samples belong to one class → **Entropy = 0 (Pure)**
- If classes are evenly mixed → **Entropy = 1 (Maximum randomness)**

---

## 📐 Entropy Formula

`H(S) = − Σ pi log₂(pi)`


Where:

- `pi` = probability of class *i*
- `log₂` = logarithm base 2

---

## ❗ Special Rule

`0 log(0) = 0`


Why?

Because mathematically:

`lim (p → 0) p log p = 0`


If a class never occurs, it adds **no uncertainty**.

---

# ✅ Computing Entropy in Code

The notebook implements entropy using:

- `class_probabilities()` → calculates label probabilities
- `data_entropy()` → computes dataset entropy

Assertions verify correctness:
- Pure dataset → entropy = 0
- Balanced dataset → entropy = 1

---

# 🔀 Entropy of a Partition

When a dataset is split, we compute **weighted entropy**.

### Formula:

`H = q1H(S1) + q2H(S2) + ... + qmH(Sm)`


Where `qi` is the proportion of each subset.

Lower entropy after splitting = **better feature**.

---

# 🧠 Building a Decision Tree (ID3 Algorithm)

Steps followed in the notebook:

### 1️⃣ Compute label counts  
Find the most common label.

### 2️⃣ Check stopping conditions:
- Only one label → create a Leaf.
- No attributes left → return majority label.

### 3️⃣ Choose best split  
Select the attribute with **minimum partition entropy**.

### 4️⃣ Recursively build subtrees.

---

## Tree Structure

The tree is defined using two objects:

### Leaf
Returns a prediction.

### Split
Contains:
- attribute to split on
- subtrees
- default value (for unknown attributes)

---

# ⚠ Handling Unknown Values

If a new data point has an unseen attribute (example: `"Intern"` level),

the model returns the **most common label** using `default_value`.

This prevents crashes and improves robustness.

---

#  Classification

Prediction is done recursively:

If Leaf → return value
Else → follow subtree based on attribute
If missing → return default value



Assertions confirm correct predictions for:
- Known inputs
- Unknown attribute values

---

# ❗ Problem with Decision Trees — Overfitting

Decision Trees often **memorize training data** instead of learning patterns.

Result:

✔ Excellent training accuracy  
❌ Poor generalization  

This is called **high variance**.

---

# 🌲 Random Forest — The Solution

Instead of one tree → build **many trees** and combine predictions.

This technique is called **Ensemble Learning**.

Think of it as consulting multiple experts instead of trusting one.

---

#  Where Does Randomness Come From?

##  Bootstrapping (Random Data Sampling)

- Sample data **with replacement**
- Some rows repeat
- Some rows are missing

Each tree gets a different dataset → trees become diverse.

---

##  Out-of-Bag Data

Unused samples act as a **built-in validation set**.

No need for separate test data!

---

# 📦 Bagging (Bootstrap Aggregating)

Steps:

1. Create multiple bootstrap datasets.
2. Train a tree on each.
3. Combine predictions.

Result → **Lower variance + Higher stability**

---

# 🎲 Random Feature Selection

Instead of evaluating every feature at each split:

 Choose a **random subset of features**.

Why?

If every tree selects the same strong feature → trees become identical.

Randomness ensures diversity → better ensemble performance.

---

#  Ensemble Learning

### Weak Learner:
- Slightly better than guessing.
- High bias.

### Strong Learner:
Created by combining many weak models.

Errors cancel out → accuracy improves.

---

#  Why Random Forest Works

Single Tree:
- Sensitive to noise
- High variance

Random Forest:

✔ Reduces overfitting  
✔ Improves stability  
✔ Produces better predictions  

---

#  Final Summary

- Decision Trees split data using **entropy**.
- ID3 selects features with **lowest partition entropy**.
- Trees are powerful but prone to **overfitting**.
- Random Forest solves this using:
  - Bootstrapping
  - Feature randomness
  - Ensemble learning

 **Random Forest = Random Data + Random Features + Many Trees**




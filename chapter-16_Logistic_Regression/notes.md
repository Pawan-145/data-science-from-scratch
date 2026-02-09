# Chapter 16 — Logistic Regression & Support Vector Machines

## Why Logistic Regression?

Linear regression predicts continuous values.

But in many real-world problems, we need to predict **categories**, such as:

- Spam vs Not Spam  
- Fraud vs Legit  
- Premium vs Free User  

These are **binary classification problems**, where the output is either:

0 → No
1 → Yes


---

# Problem Statement

Predict whether a DataSciencester user purchases a **premium account** based on:

- Experience  
- Salary  

---

## Why Not Linear Regression?

A linear model can produce impossible probabilities like:

-2.3 or 4.7


But probabilities must always lie between:

0 ≤ P ≤ 1


👉 Solution: Use the **Sigmoid (Logistic) Function**

---

# The Logistic Function

### Formula:

`σ(x) = 1 / (1 + e^(-x))`


### Properties:

✔ Always outputs values between **0 and 1**  
✔ Large positive input → close to **1**  
✔ Large negative input → close to **0**

---

## Derivative of Sigmoid

`σ'(x) = σ(x)(1 - σ(x))`


This elegant derivative makes gradient-based optimization efficient.

---

# Logistic Regression Model

Instead of:

`y = βx + ε`


We model probability as:

P(y=1 | x) = σ(βx)


Where:

- βx → linear combination of inputs  
- σ → logistic function  

---

# Maximum Likelihood Estimation (MLE)

### Why not minimize squared error?

For logistic regression:

> Minimizing squared error ≠ maximizing probability.

Instead, we **maximize likelihood**.

---

## Probability Formula

`P(yi | xi, β) = σ(xiβ)^yi * (1 - σ(xiβ))^(1 - yi)`


This single equation handles both cases:

- If `yi = 1` → probability becomes σ(xβ)  
- If `yi = 0` → probability becomes 1 − σ(xβ)

---

# Log-Likelihood

Multiplying many probabilities causes numerical instability.

So we take the logarithm.

### Log-Likelihood:

log L = yi log(σ(xβ)) + (1-yi) log(1-σ(xβ))


Since gradient descent **minimizes**, we instead minimize:

## Negative Log-Likelihood (Loss Function)

Also called **Binary Cross Entropy**.

---

# Training the Model

### Steps:

1. Rescale features  
   (Important because salary is much larger than experience)

2. Initialize random beta values

3. Compute gradients of the negative log-likelihood

4. Update parameters using gradient descent

5. Repeat until loss decreases

---

# Train-Test Split

To evaluate real performance:

- Training Set → teach the model  
- Test Set → evaluate predictions  

This prevents **overfitting**.

---

# Model Evaluation

Using a threshold of **0.5**:

| Prediction | Actual | Outcome |
|------------|---------|------------|
| Paid | Paid | True Positive |
| Paid | Unpaid | False Positive |
| Unpaid | Paid | False Negative |
| Unpaid | Unpaid | True Negative |

---

## Visualization

A scatter plot of:

Predicted Probability vs Actual Outcome

helps visually confirm model behavior.

---

# Support Vector Machines (SVM)

Logistic regression predicts probabilities.

SVM takes a different approach.

👉 It directly finds the **best boundary** between classes.

---

## Decision Boundary

Defined by:

`dot(β, x) = 0`


This boundary separates:

- Above → Paid  
- Below → Unpaid  

---

## What is a Hyperplane?

A **hyperplane** is a geometric boundary that splits feature space into classes.

- In 2D → line  
- In 3D → plane  
- Higher dimensions → hyperplane  

---

# Maximum Margin Principle

SVM chooses the boundary that maximizes the distance from the nearest data points.

These closest points are called:

## Support Vectors

They determine the position of the hyperplane.

### Key Idea:

SVM = Hyperplane + Maximum Margin



---

# Non-Linearly Separable Data

Sometimes no straight line can separate classes.

### Solution → Map to Higher Dimensions.

Example:

Transform:

x → (x, x²)


Suddenly separable!

---

# Kernel Trick

Instead of explicitly transforming data:

👉 Kernels compute dot products in higher dimensions efficiently.

### Popular Kernels:

- Polynomial  
- Radial Basis Function (RBF / Gaussian)  
- Sigmoid  

---

# Logistic Regression vs SVM

| Logistic Regression | SVM |
|---------------------|--------|
| Predicts probabilities | Finds optimal boundary |
| Uses likelihood | Uses margin maximization |
| Easier to interpret | Often higher accuracy |
| Works well for large datasets | Powerful in high dimensions |

---

# Key Takeaways

✔ Logistic regression is foundational for classification.  
✔ Sigmoid converts linear output into probability.  
✔ Negative log-likelihood drives optimization.  
✔ Feature scaling is critical.  
✔ Train-test split prevents overfitting.  
✔ SVM focuses on geometric separation.  
✔ Kernels enable complex boundaries.  

---

# Chapter 8 — Results & Observations

## 🎯 Task

Use Gradient Descent to fit a linear regression model:

y = slope * x + intercept

It is same as y = mx + c,   here m = slope and c = intercept

---

## 🔢 Initialization

Parameters initialized randomly:
- slope
- intercept

---

## ✅ Final Learned Parameters

After training:

- slope converged close to true value
- intercept converged close to true value

Loss function reduced steadily during training.

---

## 📉 Behavior of Algorithms

### Batch Gradient Descent
- Smooth convergence
- Predictable updates
- Computationally heavy

### Mini-Batch Gradient Descent
- Faster convergence
- Balanced randomness

### Stochastic Gradient Descent
- Highly noisy path
- Fast learning
- Reaches acceptable solution quickly

---

## 🧠 Key Understanding

Even without knowing correct parameters,
gradient descent can discover them
just by minimizing error.

This proves how learning happens in ML.

---

## 🚀 Improvement Ideas

- Add plotting of loss vs iterations
- Try different learning rates
- Apply to non-linear functions

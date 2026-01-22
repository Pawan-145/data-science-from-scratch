# Chapter 8 — Notes (Gradient Descent)

## 🔹 What is Optimization?

Optimization means finding values of parameters that minimize
(or maximize) a function called the loss or cost function.

---

## 🔹 Difference Quotient

Used to estimate derivative when formula is unknown:

f'(x) ≈ (f(x + h) - f(x)) / h

Smaller h gives better approximation.

---

## 🔹 Partial Derivatives

For multivariable functions, we calculate derivative
with respect to one variable at a time.

Used to build the gradient vector.

---

## 🔹 Gradient

Gradient is a vector of partial derivatives:

∇f = [∂f/∂x₁, ∂f/∂x₂, ..., ∂f/∂xₙ]

It points in direction of steepest increase.

To minimize:
new_point = old_point - learning_rate × gradient

---

## 🔹 Gradient Descent Algorithm

1. Start with random parameters
2. Compute gradient of loss function
3. Move opposite to gradient
4. Repeat until convergence

---

## 🔹 Learning Rate

Controls size of update step.

- Too large → overshoots minimum
- Too small → very slow learning

Choosing learning rate is critical.

---

## 🔹 Types of Gradient Descent

### Batch GD
- Uses full dataset
- Stable but slow

### Mini-Batch GD
- Uses small data chunks
- Faster and stable

### SGD
- Uses single sample
- Very fast but noisy

---

## 🔹 Why Noise in SGD is Useful

Noise helps escape local minima
and explore better solutions.

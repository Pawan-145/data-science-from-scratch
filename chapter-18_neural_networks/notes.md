#  Chapter 18 — Neural Networks

## 📌 Overview

Neural Networks are powerful machine learning models inspired by the human brain. They are capable of solving complex problems such as:

- Handwriting recognition
- Face detection
- Speech processing
- Pattern recognition

However, neural networks are often considered **black boxes** because it is difficult to interpret exactly how they arrive at their predictions.

---

# 🔹 Perceptrons — The Simplest Neural Network

A **Perceptron** models a single artificial neuron.

It:

1. Takes multiple binary inputs  
2. Computes a weighted sum  
3. Adds a bias  
4. Applies an activation function  
5. Produces an output (fire or not fire)

---

## Mathematical Representation

`z = w₁x₁ + w₂x₂ + ... + wₙxₙ + b`


Where:

- `w` → weights  
- `x` → inputs  
- `b` → bias  

This is similar to the line equation:

`y = mx + c`


### Role of Bias
Bias acts like an **intercept**, allowing the decision boundary to shift freely instead of being forced through the origin.

Think of bias as giving the neuron a **starting opinion**.

---

## Activation — Step Function

if z >= 0 → output = 1 (Neuron fires)
else → output = 0


A perceptron separates data using a **hyperplane**:

`dot(weights, x) + bias = 0`


---

## ⚠ Limitation of Perceptrons

Single perceptrons can solve **linearly separable problems**:

✅ AND  
✅ OR  
✅ NAND  
✅ NOR  

But cannot solve:

❌ XOR  

Because XOR is **not linearly separable**.

This leads to multi-layer neural networks.

---

# 🔹 Feed-Forward Neural Networks

A Feed-Forward Neural Network consists of stacked neuron layers:

### Architecture:

### ✅ Input Layer
Receives features.

### ✅ Hidden Layers
Perform transformations and learn patterns.

### ✅ Output Layer
Produces the final prediction.

Information flows strictly **forward** — no loops.

---

## Why Use Sigmoid Instead of Step?

The step function is not differentiable.

Neural networks require calculus for optimization.

### Sigmoid Function:

`σ(t) = 1 / (1 + e⁻ᵗ)`


### Benefits:

✔ Smooth  
✔ Differentiable  
✔ Output between 0 and 1  
✔ Enables gradient descent  

---

# 🔹 Feed Forward Process

Steps:

1. Multiply inputs by weights  
2. Add bias  
3. Apply activation  
4. Pass output to next layer  

This produces predictions.

---

# 🔹 Backpropagation — How Networks Learn

Backpropagation is the core training algorithm used to minimize prediction error.

---

## Two Phases:

### ✅ Forward Pass
Input → Prediction

### ✅ Backward Pass
Error → Gradients → Weight Updates

---

## Gradient Formula

`Gradient = Delta × Input`


Where:

- **Delta** → neuron error signal  
- **Gradient** → how much a weight should change  

Weights are updated using **Gradient Descent**.

---

# 🔹 Training Example — XOR

The notebook trains a neural network to learn the XOR function.

### Dataset:

| Input | Output |
|--------|---------|
| 0,0 | 0 |
| 0,1 | 1 |
| 1,0 | 1 |
| 1,1 | 0 |

---

## Network Architecture:

- 2 inputs  
- 2 hidden neurons  
- 1 output neuron  

After training (~20,000 epochs), the network successfully learns XOR.

### Learned Behavior:

Hidden neurons approximate:

- OR  
- AND  

Output neuron computes:

(OR) AND NOT(AND)


Which equals XOR.

✅ This demonstrates how hidden layers enable learning non-linear patterns.

---

# 🔹 Gradient Descent

Weights are updated using:

`new_weight = old_weight - learning_rate × gradient`


A higher learning rate speeds up training but may cause instability.

---

# 🔹 Example — FizzBuzz with Neural Networks

FizzBuzz is a classic programming challenge:

- Divisible by 3 → Fizz  
- Divisible by 5 → Buzz  
- Divisible by 15 → FizzBuzz  
- Else → Number  

---

## Encoding Strategy

### Binary Encoding
Numbers are converted into **10-bit binary vectors**.

This allows the network to detect numerical patterns.

---

### One-Hot Encoding (Targets)

| Label | Vector |
|--------|---------|
| Number | [1,0,0,0] |
| Fizz | [0,1,0,0] |
| Buzz | [0,0,1,0] |
| FizzBuzz | [0,0,0,1] |

---

## Network Design

- **10 input features**
- **25 hidden neurons**
- **4 output neurons**

The network is trained on numbers **101–1023** and tested on **1–100**.

This ensures the model learns patterns rather than memorizing answers.

---

# 🔹 Argmax — Choosing Predictions

The output layer returns probabilities.

`argmax()` selects the index of the largest probability as the prediction.

---

# 🚀 Key Insights

✔ Hidden layers unlock non-linear learning  
✔ Backpropagation powers neural network training  
✔ Encoding strategies strongly impact performance  
✔ Neural networks generalize patterns when trained correctly  

---

# ⚠ Challenges of Neural Networks

- Require large datasets  
- Computationally expensive  
- Hard to interpret  
- Sensitive to hyperparameters  

---

# ✅ Final Summary

This chapter demonstrated:

✔ Perceptron fundamentals  
✔ Feed-forward networks  
✔ Sigmoid activation  
✔ Backpropagation  
✔ Gradient descent  
✔ XOR learning  
✔ FizzBuzz classification  


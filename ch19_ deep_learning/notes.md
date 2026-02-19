# 🧠 Chapter 19 — Deep Learning

## 📌 Overview

Deep Learning refers to neural networks with multiple hidden layers.

These deeper architectures allow models to learn:

- Complex patterns
- Hierarchical representations
- High-level abstractions

In modern frameworks, data structures used in neural networks are called **Tensors**.

In this chapter, we simplified:

Tensor = list  
Tensor = Union[float, List[Tensor]]

---

# 🔹 Understanding Tensors

A tensor can be:

- A scalar (float)
- A vector
- A matrix
- A higher dimensional structure

## Helper Functions Implemented

### ✔ shape(tensor)
Returns the dimensions of a tensor.

Example:

[1,2,3] → [3]
[[1,2],[3,4]] → [2,2]


---

### ✔ is_1d(tensor)
Checks if tensor is a vector.

---

### ✔ tensor_sum(tensor)
Recursively sums all elements.

---

### ✔ tensor_apply(f, tensor)
Applies function elementwise.

---

### ✔ zeros_like(tensor)
Creates zero tensor with same shape.

---

### ✔ tensor_combine(f, t1, t2)
Combines two tensors elementwise.

---

# 🔹 Layer Abstraction

A Layer:

- forward(input)
- backward(gradient)
- params()
- grads()

This abstraction makes networks modular and extensible.

---

# 🔹 Sigmoid Layer

Applies sigmoid activation:

σ(x) = 1 / (1 + e⁻ˣ)

Backward uses derivative:

σ'(x) = σ(x)(1 − σ(x))

---

# 🔹 Linear Layer

Represents:

y = Wx + b

Includes:

- Weight initialization (Uniform, Normal, Xavier)
- Forward pass
- Backward gradient computation
- Parameter tracking

---

## Weight Initialization Methods

1️⃣ Uniform  
2️⃣ Normal  
3️⃣ Xavier ⭐

Xavier prevents:

- Exploding gradients  
- Vanishing gradients  

Variance:

2 / (input_dim + output_dim)


---

# 🔹 Sequential Model

Chains multiple layers together.

Forward → pass through layers  
Backward → reverse through layers  

---

# 🔹 Loss Functions

## SSE (Sum of Squared Errors)

Loss:

`(predicted - actual)²`

Gradient:

`2 * (predicted - actual)`

---

# 🔹 Optimizers

## Gradient Descent

Updates:

`param = param - learning_rate * gradient`


---

## Momentum Optimizer

Maintains running average of gradients.

Prevents:
- Oscillation
- Overreaction to noisy gradients

Update rule:

v = momentum * v + (1 - momentum) * grad
param = param - lr * v


---

# 🔹 Modern Activation Functions

## 🔹 Sigmoid
- Output range: (0,1)
- Saturates at extremes

---

## 🔹 Tanh
- Output range: (-1,1)
- Zero-centered
- Derivative: 1 - tanh²(x)

---

## 🔹 ReLU (Rectified Linear Unit)

`f(x) = max(0, x)`


Advantages:
- Simple
- Efficient
- Reduces vanishing gradients

---

# 🔹 Softmax & Cross Entropy

## Softmax

Converts logits to probabilities:


$$[
\text{softmax}(z_i) =
\frac{e^{z_i - \max(z)}}
{\sum_{j} e^{z_j - \max(z)}}
]$$


Ensures:
- All outputs sum to 1
- Probabilistic interpretation

---

## Softmax + Cross Entropy

Loss:

Σ actual_i * log(predicted_i)


Gradient simplifies to:

`predicted - actual`



Very efficient for classification.

---

# 🔹 Dropout (Regularization)

During training:

- Randomly turn off neurons with probability p

Prevents:
- Overfitting
- Co-adaptation of neurons

During evaluation:

- Scale outputs instead of dropping neurons

---

# 🔹 MNIST Example (Real Deep Learning)

Dataset:
- 60,000 training images
- 10,000 test images
- 28x28 grayscale digits

Model:

1. Flatten Layer (784 inputs)
2. Dense (128 neurons, ReLU)
3. Dense (10 neurons, Softmax)

Optimizer: Adam  
Loss: Sparse Categorical Crossentropy  

---

# 🔹 Saving and Loading Models

Weights are saved as JSON.

Process:
1. Extract parameters
2. Store in file
3. Reload and assign

Ensures reproducibility.

---

# 🚀 Key Takeaways

-  Built tensor system from scratch  
-  Designed modular neural network layers  
-  Implemented optimizers  
-  Implemented modern activations  
-  Built softmax classifier  
-  Applied dropout  
-  Trained real MNIST model  









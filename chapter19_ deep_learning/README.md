# 🧠 Chapter 19 — Deep Learning

## 📌 Overview

This chapter implements core deep learning concepts from scratch and applies them to a real-world dataset (MNIST).

We move beyond basic neural networks and explore:

- Tensor abstractions
- Modular layer design
- Advanced optimizers
- Modern activation functions
- Softmax classification
- Dropout regularization
- Real dataset training

---

# 🎯 Objectives

✔ Understand tensor operations  
✔ Design reusable neural network layers  
✔ Implement optimizers  
✔ Learn modern activation functions  
✔ Apply Softmax + Cross Entropy  
✔ Train model on MNIST  

---

# 🏗 Architecture Built

## Core Components

- Tensor utilities
- Layer abstraction
- Linear layer
- Sigmoid / Tanh / ReLU
- Sequential model
- Loss functions
- Optimizers (GD + Momentum)
- Dropout layer

---

# 🧪 Real Example: MNIST

Dataset:
- 28x28 grayscale digit images
- 10 output classes

Model:
Flatten → Dense(128, ReLU) → Dense(10, Softmax)


Optimizer:
Adam

Loss:
Sparse Categorical Crossentropy

---

# 📊 Results

✔ Model trained successfully  
✔ Achieved high test accuracy  
✔ Demonstrated deep learning pipeline  

---

# 🚀 Why This Chapter Matters

This chapter bridges:

Neural Network Theory → Practical Deep Learning

You now understand:

- How frameworks like PyTorch & TensorFlow are structured internally
- How optimizers work
- How regularization is applied
- Why activation functions matter

---

# 📁 Project Structure

- `ch19_deep_learning.ipynb`
- `notes.md`
- `results.md`

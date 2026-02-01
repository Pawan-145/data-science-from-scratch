# 📘 Chapter 11 — Machine Learning

This chapter introduces the foundational concepts of Machine Learning and explains how models learn patterns from data to make predictions.

Rather than focusing on complex algorithms, this chapter builds strong conceptual clarity — which is critical before implementing real-world ML systems.

---

## 🎯 Objectives

- Understand what a model is
- Learn different types of machine learning
- Identify overfitting vs underfitting
- Perform proper train-test splits
- Evaluate models using performance metrics
- Understand bias–variance tradeoff
- Learn the importance of features

---

## 🧠 Key Concepts Covered

### ✔️ Modeling
A model represents a mathematical relationship between input variables (features) and output variables (targets).

### ✔️ Types of Machine Learning
- Supervised Learning
- Unsupervised Learning
- Semi-supervised Learning
- Online Learning
- Reinforcement Learning

### ✔️ Overfitting vs Underfitting
- **Overfitting:** Learns noise → performs poorly on new data  
- **Underfitting:** Too simple → fails even on training data  

The goal is to find the **balance**.

---

## 🔀 Dataset Splitting

Implemented:

- `split_data()` → randomly splits dataset
- `train_test_split()` → preserves (x, y) pairing

Why important?

Because evaluating a model on training data gives **false confidence**.

---

## 📊 Evaluation Metrics Implemented

- Accuracy  
- Precision  
- Recall  
- F1 Score  

These metrics help measure model effectiveness beyond just correctness.

---

## ⚖️ Bias-Variance Tradeoff

One of the MOST important ML ideas.

| High Bias | High Variance |
|--------|-------------|
| Model too simple | Model too complex |
| Underfits | Overfits |

The goal is to find the **sweet spot** where the model generalizes well.

---

## 🧾 What I Practiced

✔️ Writing data splitting functions  
✔️ Preserving feature-target relationships  
✔️ Implementing evaluation metrics from scratch  
✔️ Understanding model generalization  

---

## 🚀 Why This Chapter Matters

Machine Learning is NOT about immediately jumping into libraries like Scikit-Learn.

Strong fundamentals make you:

✅ Better at debugging models  
✅ Strong in interviews  
✅ Able to design real ML systems  
✅ Different from tutorial-followers  

---


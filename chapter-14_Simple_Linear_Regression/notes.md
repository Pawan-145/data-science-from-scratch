# Chapter 14 – Simple Linear Regression

## What is Simple Linear Regression?

Simple Linear Regression is a statistical technique used to model the relationship between two variables:

- **Independent Variable (X)** → Predictor (e.g., number of friends)
- **Dependent Variable (Y)** → Target (e.g., daily minutes spent on a platform)

It assumes a **linear relationship** between the variables.

---

## Linear Equation

The regression line is represented as:

y = βx + α

Where:

- **β (beta)** → slope of the line  
  - Represents how much `y` changes when `x` increases by 1.
- **α (alpha)** → intercept  
  - Value of `y` when `x = 0`.

---

## Goal of Regression

Find values of **alpha** and **beta** that minimize prediction error.

---

## Error Function

The error for each data point:
`error = predicted_y - actual_y`


Squared error is used to avoid negative values:
(error)<sup>2</sup>


Total loss:

Sum of Squared Errors (SSE)


Minimizing SSE gives the best-fit regression line.

---

## Analytical Solution

Instead of guessing parameters, we can compute them directly using statistics.

### Beta (Slope)

`beta = correlation(x, y) * (std_y / std_x)`


### Alpha (Intercept)

`alpha = mean_y - beta * mean_x`


---

## R-squared (Coefficient of Determination)

Measures how well the regression line fits the data.

`R² = 1 - (SSE / Total Variation)`


### Interpretation:

| R² Value | Meaning |
|--------|---------|
| 0      | Model explains nothing |
| 0.5    | Moderate fit |
| 1      | Perfect prediction |

---

## Gradient Descent for Regression

Instead of using formulas, parameters can be learned using **Gradient Descent**.

### Steps:

1. Start with random alpha and beta.
2. Compute gradients (partial derivatives).
3. Update parameters using:

`new_param = old_param - learning_rate * gradient`


4. Repeat until loss stops decreasing.

---

## Partial Derivatives

For alpha:

grad_a = 2 * error


For beta:

grad_b = 2 * error * x


---

## Learning Rate

Controls step size during optimization.

- Too large → overshooting
- Too small → slow learning

---
### Maximum Likelihood Estimation (MLE)

Maximum Likelihood Estimation is a method used to estimate model parameters by choosing values that make the observed data most probable.

In short:
Pick parameters that best explain the data.

---
## Observations

- Regression captures linear patterns in data.
- Both analytical and gradient methods should give similar results.
- Minimizing squared error improves predictions.
- Gradient Descent is useful when datasets are large.
- Maximum Likelihood Estimation

---

## When to Use Simple Linear Regression?

Use it when:

✅ Relationship between variables is roughly linear  
✅ You want interpretable results  
✅ Dataset is not extremely complex  

Avoid when:

❌ Relationship is nonlinear  
❌ Many features are involved (use multiple regression)

---

## Key Takeaways

✔ Simple Linear Regression predicts numeric values.  
✔ Uses slope and intercept to form a line.  
✔ Goal is minimizing squared error.  
✔ R² measures model quality.  
✔ Gradient Descent can learn parameters iteratively.  
✔ Foundational algorithm for Machine Learning.
✔ Maximum Likelihood Estimation



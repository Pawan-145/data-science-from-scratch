# Chapter 15 – Multiple Regression

## What is Multiple Regression?

Multiple Regression is an extension of Simple Linear Regression that models the relationship between **one dependent variable** and **multiple independent variables**.

### Model Equation:

y = α + β₁x₁ + β₂x₂ + ... + βₖxₖ + ε

Where:

- **α (alpha)** → intercept  
- **β₁, β₂ … βₖ** → coefficients for each feature  
- **ε** → error term  

The objective is to find beta values that minimize prediction error.

---

## Example Model

minutes = α + β₁(friends) + β₂(work_hours) + β₃(phd)

This predicts how many minutes a user spends on a platform based on multiple factors.

---

## Dummy Variables

A dummy variable converts categorical data into numeric form.

Example:

phd = 1 → user has a PhD
phd = 0 → user does not have a PhD


### Interpretation:
β₃ represents how much additional time is expected for users with a PhD compared to those without one.

---

## Vector Representation

Instead of writing long equations, regression is expressed using vectors.

beta = [α, β₁, β₂, ... βₖ]
x = [1, x₁, x₂, ... xₖ]


The leading `1` allows the intercept to be included.

### Prediction Function:

prediction = dot(x, beta)


---

## Fitting the Model

Unlike simple regression, analytical solutions become complex with many variables.

Therefore, **Gradient Descent** is used to minimize the **Sum of Squared Errors (SSE).**

### Steps:

1. Initialize beta with random values.
2. Compute prediction error.
3. Calculate gradients.
4. Update parameters.
5. Repeat until convergence.

---

## Error Function

error = predicted_y - actual_y
squared_error = error²

Gradient:

∂Loss/∂β = 2 * error * x

---

## Measuring Model Performance

### R-Squared (Coefficient of Determination)

R² = 1 - (Sum of Squared Errors / Total Sum of Squares)


### Interpretation:

| R² Value | Meaning |
|--------|---------|
| 0      | No explanatory power |
| 0.5    | Moderate fit |
| 1      | Perfect prediction |

⚠️ Adding more variables **always increases R²**, even if they are not useful.

---

## Bootstrap Sampling

Bootstrap is a statistical technique used to estimate uncertainty by repeatedly sampling the dataset **with replacement**.

### Why Use It?

- Estimate coefficient variability  
- Compute standard errors  
- Understand model stability  

---

## Standard Errors of Coefficients

Standard error measures how much a coefficient might vary across samples.

Lower standard error → more reliable coefficient.

---

## Hypothesis Testing

### t-statistic

t = estimated_coefficient / standard_error

Interpretation:

- **Large t-value** → strong evidence the variable matters  
- **Small t-value** → likely noise  

---

### p-value

Answers:

> "If the true coefficient were zero, how likely is this result?"

- Small p-value (< 0.05) → Reject null hypothesis  
- Large p-value → Fail to reject  

When datasets are large, the **t-distribution approximates the normal distribution.**

---

## F-Test

Used to evaluate multiple coefficients simultaneously.

- **t-test** → one variable  
- **F-test** → multiple variables  

Helps answer:

- Does at least one feature matter?
- Are groups of variables useful?

---

# Regularization

Regularization prevents **overfitting** by penalizing large coefficients.

---

## Ridge Regression (L2)

Adds squared magnitude of coefficients as a penalty.

### Loss Function:

Loss = Squared Error + α(β₁² + β₂² + ... + βₙ²)

Properties:

✅ Shrinks coefficients  
✅ Reduces variance  
❌ Does NOT eliminate features  

Gradient of ridge penalty: **2αβ**

---

## Lasso Regression (L1)

Uses absolute values instead of squares.

Penalty:

α(|β₁| + |β₂| + ... + |βₙ|)

### Key Advantage:

✔ Can force some coefficients to **exactly zero**  
✔ Performs automatic feature selection  

Challenge:

The absolute function is **not differentiable at 0**, making optimization harder.

---

## Ridge vs Lasso

| Ridge | Lasso |
|------|--------|
| Shrinks coefficients | Eliminates coefficients |
| Keeps all features | Performs feature selection |
| Stable | Sparse models |

---

## Key Takeaways

✔ Multiple regression models complex relationships.  
✔ Gradient descent is essential for parameter optimization.  
✔ Dummy variables allow categorical data usage.  
✔ R² measures model fit but must be interpreted carefully.  
✔ Bootstrap helps estimate coefficient reliability.  
✔ Regularization prevents overfitting.  
✔ Ridge shrinks — Lasso selects.  

Multiple Regression is a **core foundation** for advanced ML algorithms.

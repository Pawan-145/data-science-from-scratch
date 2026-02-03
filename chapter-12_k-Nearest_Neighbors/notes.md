# 📘 Chapter 12 – k-Nearest Neighbors (KNN)

## 🔹 Introduction to KNN

k-Nearest Neighbors (KNN) is a **supervised machine learning algorithm** used primarily for classification and regression tasks.

Unlike many ML algorithms, KNN has **no explicit training phase**. Instead, it stores the dataset and makes predictions based on similarity.

👉 This is why it is called a **lazy learning algorithm**.

---

## 🔹 How KNN Works

When a new data point appears:

1. Calculate the distance between the new point and all existing points.
2. Select the **k closest neighbors**.
3. Look at their labels.
4. Assign the most common label to the new data point.

---

## 🔹 Majority Voting

The predicted class is determined using a voting mechanism.

### Basic Majority Vote

```python
def raw_majority_vote(labels):
    votes = Counter(labels)
    winner, _ = votes.most_common(1)[0]
    return winner

### Handling Ties

Ties can occur when multiple labels receive the same number of votes.

Common strategies:

 - Reduce the value of k
 - Choose the label of the closest neighbor 
 - Use weighted voting based on distance

---
###🔹 Distance Metrics

Distance measures similarity between data points.
## Euclidean Distance
Most commonly used in KNN:
def distance(v, w):
    return math.sqrt(sum((v_i - w_i) ** 2 for v_i, w_i in zip(v, w)))

✔ Smaller distance → Higher similarity
✔ Larger distance → Lower similarity
---
###🔹 Representing Labeled Data
Each observation is stored with its features and label.

class LabeledPoint(NamedTuple):
    point: Vector
    label: str
---
###🔹 Building the KNN Classifier
Steps implemented:
- Sort points by distance
- Pick k nearest neighbors
- Extract labels
- Apply majority vote

def knn_classify(k, labeled_points, new_point):
    by_distance = sorted(
        labeled_points,
        key=lambda lp: distance(lp.point, new_point)
    )

    k_nearest_labels = [lp.label for lp in by_distance[:k]]

    return majority_vote(k_nearest_labels)
---

###🔹 Choosing the Right k

Selecting k is critical.

Small k:
✅ Captures fine patterns
❌ Sensitive to noise (high variance)

Large k:
✅ More stable predictions
❌ Can oversimplify the data (high bias)

👉 Odd values are often preferred to avoid ties.
---
###🔹 Working with the Iris Dataset

The Iris dataset is one of the most famous datasets in machine learning.

Features:
- Sepal length
- Sepal width
- Petal length
- Petal width

Classes:
- Setosa
- Versicolor
- Virginica

This dataset is ideal for learning classification techniques.
---
###🔹 Train-Test Split
To evaluate model performance properly:

- Training set → Used to build the model
- Test set → Used to evaluate generalization

Typical split:

`70% Training`
`30% Testing`

Key lesson:
Never evaluate a model on the data it was trained on.
---
###🔹 Curse of Dimensionality

As the number of dimensions increases:
- Data points spread farther apart.
- Distance becomes less meaningful.
- Nearest neighbors lose significance.

## Observation:
The difference between the nearest and farthest neighbor shrinks in high-dimensional space.

👉 This weakens distance-based algorithms like KNN.
---

###🔹 When to Use KNN
- Best suited for:
- Small datasets
- Low-dimensional data
- Pattern recognition tasks

## Avoid when:

- Dataset is very large
- Real-time prediction is required
- Feature space is high-dimensional

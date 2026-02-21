# 📘 Chapter 20 — Clustering

## 📌 Overview

Clustering is an example of **unsupervised learning**, where we work with completely unlabeled data.

Unlike supervised learning:
- There are no target labels.
- The algorithm must discover structure on its own.

Clusters do not label themselves — we must interpret them manually.

---

# 🔹 K-Means Clustering

One of the simplest and most widely used clustering algorithms.

## Goal

Given:
- n data points
- k clusters (chosen beforehand)

Divide the data into k groups such that:

- Points in each cluster are close to that cluster's mean.
- The total squared distance within clusters is minimized.

---

## Objective Function

Minimize:

Total Squared Error (SSE)

$\sum \text{distance}(\text{point}, \text{cluster\_mean})^2$


---

## K-Means Algorithm

1. Initialize k random cluster assignments.
2. Compute cluster means.
3. Assign each point to nearest mean.
4. Repeat until assignments stop changing.

This is an **iterative optimization process**.

---

## Core Components Implemented

### Vector Utilities

- dot()
- subtract()
- squared_distance()
- sum_of_squares()

---

### Cluster Mean Computation

Handles empty clusters by assigning a random point.

---

### KMeans Class

Methods:

- train(inputs)
- classify(input)

Training stops when cluster assignments stabilize.

Progress tracked using tqdm.

---

# 🔹 Choosing K — Elbow Method

We compute:

Total Squared Error vs Number of Clusters


Then plot:

- x-axis → k
- y-axis → total squared error

Look for a “bend” (elbow) in the curve.

This indicates diminishing returns beyond that k.

---

# 🔹 Example: Image Color Clustering

Images are represented as:

Height × Width × 3

Each pixel:

`[R, G, B]`


Steps:

1. Flatten image into list of RGB vectors
2. Apply K-Means
3. Replace each pixel with its cluster mean
4. Reconstruct image

Result:
- Reduced-color version of image
- Example used k = 5

This demonstrates real-world clustering.

---

# 🔹 Hierarchical Clustering (Bottom-Up)

Alternative clustering strategy.

Instead of dividing into k clusters:

We build clusters progressively.

---

## Algorithm

1. Start with each point as its own cluster.
2. Merge closest pair.
3. Repeat until one cluster remains.

This builds a tree (dendrogram).

---

## Cluster Types

Two representations:

### Leaf
Single data point.

### Merged
Contains:
- children clusters
- merge order

---

## Cluster Distance Methods

Distance between clusters can be defined using:

1. Single Linkage → minimum pairwise distance
2. Complete Linkage → maximum pairwise distance
3. Average Linkage → average pairwise distance

---

## Generating k Clusters

After full hierarchy is built:

- Perform “unmerges”
- Split based on merge order
- Generate desired number of clusters

---

# 🚀 Key Takeaways

✔ K-Means minimizes within-cluster variance  
✔ Choosing k is non-trivial  
✔ Elbow method helps selection  
✔ Clustering can be applied to images  
✔ Hierarchical clustering builds nested structures  
✔ Different linkage methods give different cluster shapes  

---

# ⚠ Limitations

- K-Means assumes spherical clusters
- Sensitive to initialization
- Requires k beforehand
- Hierarchical clustering is computationally expensive

---

# ✅ Summary

This chapter implemented:

- K-Means from scratch
- Error evaluation
- Elbow method visualization
- Image color compression
- Bottom-up hierarchical clustering

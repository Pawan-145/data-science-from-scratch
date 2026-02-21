# 📊 Chapter 20 — Results

## ✔ K-Means Convergence

The KMeans class successfully:

- Randomly initialized assignments
- Iteratively updated means
- Reassigned points
- Stopped when assignments stabilized

Training converged properly.

---

## ✔ Squared Error Behavior

As k increases:

- Total Squared Error decreases
- Improvement diminishes after certain k

Elbow method visualization confirmed:

✔ Optimal cluster count can be estimated visually

---

## ✔ Image Color Compression

Using k = 5:

- Original image flattened into RGB vectors
- Clustered pixels
- Reconstructed image with 5 dominant colors

Result:

✔ Reduced color palette
✔ Maintained overall visual structure
✔ Demonstrated real-world clustering application

---

## ✔ Hierarchical Clustering

Successfully:

- Built full cluster tree
- Stored merge order
- Computed cluster distances
- Generated arbitrary number of clusters

Single linkage used by default.

---

## ✔ Cluster Distance Validation

Distance metrics verified:

- Minimum linkage
- Maximum linkage
- Average linkage (optional)

All behaved correctly.

---

# 🔥 Observations

- K-Means is fast and practical
- Hierarchical clustering gives richer structure
- Linkage choice significantly affects cluster shape
- Clustering works well for image compression

---

# ✅ Final Outcome

Implemented from scratch:

✔ Vector math utilities  
✔ K-Means algorithm  
✔ Elbow method plotting  
✔ Image clustering  
✔ Bottom-up hierarchical clustering  

Status: ✅ Successfully Completed

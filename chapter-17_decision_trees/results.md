# 📊 Chapter 17 — Results

## ✔ Entropy Implementation Verified

Assertions confirmed:

| Dataset Type | Expected Entropy | Result |
|------------|----------------|--------|
| Pure dataset | 0 | ✅ Passed |
| Balanced dataset | 1 | ✅ Passed |
| Mixed dataset | ~0.81 | ✅ Passed |

---

## ✔ Best Split Selection

Entropy calculations showed:

| Attribute | Partition Entropy |
|------------|------------------|
| level | Lowest ✅ |
| lang | Higher |
| tweets | Higher |
| phd | Highest |

👉 **"level" selected as root node.**

---

## ✔ Tree Behavior

The constructed decision tree correctly predicted:

- Junior + No PhD → **True**
- Junior + PhD → **False**
- Senior + Tweets → **True**
- Senior + No Tweets → **False**

---

## ✔ Unknown Attribute Handling

Test case:

Candidate("Intern", "Java", True, True)


Prediction → **True**

✔ Default value successfully applied.

---

## ✔ Recursive Tree Construction

The `build_tree_id3()` function successfully:

- Selected optimal attributes
- Built subtrees
- Created leaf nodes
- Returned a working classifier

---

##  Key Observations

### Decision Trees:
✔ Interpretable  
✔ Fast  
✔ Require little preprocessing  

⚠ But prone to overfitting.

---

### Random Forest:

✔ Reduces variance  
✔ Improves accuracy  
✔ More robust  

---

##  Final Outcome

The notebook successfully demonstrates:

- Entropy calculation  
- Dataset partitioning  
- ID3 tree construction  
- Recursive classification  
- Handling missing values  
- Random Forest theory  

 **Status: Successfully Implemented**

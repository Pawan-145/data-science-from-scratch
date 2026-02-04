
# Results — Chapter 13 (Naive Bayes)

## Model Verification

The classifier was tested using sample messages.

### ✔ Tokens correctly identified:
{"spam", "ham", "hello", "rules"}


### ✔ Message counts:
- Spam messages → 1  
- Ham messages → 2  

---

## Dataset Used

SpamAssassin Public Corpus containing:

- Easy Ham  
- Hard Ham  
- Spam  

Subjects were extracted and labeled successfully.

---

## Word Probability Analysis

The classifier calculated:

P(spam | word)

---
### Output:

- **Spammiest words:**  
Words most strongly associated with spam emails.

- **Hammiest words:**  
Words commonly appearing in legitimate emails.

This confirms that the classifier successfully learned patterns from the dataset.

---

## Key Achievement

✅ Built a working spam detection system  
✅ Implemented Naive Bayes without external ML libraries  
✅ Processed real-world email data  
✅ Identified high-risk spam keywords  

---

## Conclusion

The Naive Bayes classifier performed effectively for text classification and demonstrated why it remains one of the most powerful baseline algorithms in machine learning.

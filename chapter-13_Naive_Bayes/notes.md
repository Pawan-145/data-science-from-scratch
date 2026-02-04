# Chapter 13 — Naive Bayes

## What is Naive Bayes?

Naive Bayes is a probabilistic machine learning algorithm based on **Bayes’ Theorem**.  
It is widely used for **text classification**, especially **spam detection**.

---

## Bayes' Theorem
s
P(S|B) = P(B|S)P(S)/P(B|S)P(S)+P(B|¬S)P(¬S)]
Where:

- **S** → Spam  
- **B** → Message contains the word "Bitcoin"  
- **¬S** → Not Spam  

👉 The numerator represents the probability that a message is spam AND contains the word.

👉 The denominator represents all emails containing that word — spam or not.

---

## Multiple Word Clues

Instead of checking one word, we check many:

Examples:

- bitcoin  
- rolex  
- free  
- offer  
- win  

Each word acts as a **signal**.

We define:

- **Xi** → Event that the message contains word *i*
- **P(Xi | S)** → Probability spam contains the word
- **P(Xi | ¬S)** → Probability normal mail contains the word

These probabilities are learned from historical data.

---

## Why "Naive"?

Naive Bayes assumes:

> **All features are independent.**

Meaning:

If an email contains “bitcoin”, it tells us NOTHING about whether it contains “rolex”.

Instead of calculating complex joint probabilities:

\[
P(X_1, X_2,...,X_n | S)
\]

We simply multiply individual probabilities.

This assumption makes Naive Bayes:

✅ Fast  
✅ Memory efficient  
✅ Great for text problems  

---

## Tokenization

Tokenization converts raw text into meaningful words.

### Steps:

1. Convert text to lowercase  
2. Extract words using regex  
3. Store unique tokens  

Example:

```python
tokenize("Data Science is Science")
```
Output
```python
{"data", "science", "is"}
```
## Training Data Structure

We define a message format:
```python
class Message(NamedTuple):
    text: str
    is_spam: bool
```
This allows us to label emails clearly.

---
Naive Bayes Classifier

The classifier:

- Counts word occurrences
- Separates spam vs ham
- Applies smoothing (k value)
- Computes probabilities

Key Concepts:
✔ Laplace Smoothing

Prevents zero probabilities.
P=count+k/(total+2k)

---
### Testing the Model

Example training messages:
- "spam rules" → Spam
- "ham rules" → Not spam
- "hello ham" → Not spam

After training:
- Tokens detected correctly
- Spam/Ham counts verified​

----
Real Dataset — SpamAssassin

Dataset downloaded from:
`https://spamassassin.apache.org/old/publiccorpus`

Includes:
- Easy Ham
- Hard Ham
- Spam

Emails were extracted from `.tar.bz2` files.

---
#### Data Processing
Steps performed:
- Read email files
- Extract subject lines
- Label spam vs ham
- Store as Message objects
---
#### Spam Probability per Word
We compute:
`P(spam | token)`

This tells us which words are strong spam indicators.

---
Example outputs:
- Spammiest words → Highly associated with spam
- Hammiest words → Common in normal emails

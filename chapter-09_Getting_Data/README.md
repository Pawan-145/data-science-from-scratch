# 📘 Chapter 9 — Getting Data   

This chapter focuses on how to **collect, read, and process data** from multiple real-world sources using Python.  
Before building any machine learning model, data must be gathered and cleaned — this chapter builds that foundation.

---

## 🎯 Objectives of This Chapter

- Learn how command-line data tools work
- Read and write files safely
- Process CSV and delimited files
- Scrape data from web pages
- Parse JSON and XML-style data
- Use public APIs to collect datasets

---

## 📂 Files in This Folder

- `getting_data.py` → Practice code
- `README.md` → Chapter overview
- `notes.md` → Theory + explanations
- `results.md` → Outcomes and learnings
- `stock_prices.txt` → Tab-delimited file of stock prices
- `comma_delimated_stock_prices.txt` → Colon-delimited file of stock prices with headers
- `secrets_template.json` → copy this template and paste in "secrets.json" file to store keys and token

---

## 🛠 Libraries Used

- `sys`, `re`
- `csv`
- `json`
- `requests`
- `bs4 (BeautifulSoup)`
- `collections.Counter`
- `dateutil.parser`
- `twython` (conceptual API example)

---

## 📌 Important Note

Some API examples (especially Twitter/X) no longer work with free accounts due to updated policies.  
These examples are kept for **learning API concepts**, not production use.

---


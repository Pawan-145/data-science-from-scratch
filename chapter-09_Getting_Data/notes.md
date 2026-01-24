# 📒 Chapter 9 Notes — Getting Data

## 1. Command-Line Arguments

Python scripts can receive inputs using:

sys.argv

- sys.argv[0] → script name
- sys.argv[1], sys.argv[2] → user inputs

Used for:
- regex filters
- number of words
- filenames

---

## 2. Standard Input and Output

UNIX-style pipelines:

cat file.txt | python script.py

- sys.stdin → reads input line by line
- sys.stdout → writes output

Useful for building data-processing tools.

---

## 3. Regular Expressions

Used to match patterns in text:

re.search(pattern, text)

Applications:
- filtering logs
- searching keywords
- validating formats

---

## 4. File Handling in Python

Open modes:
- "r" → read
- "w" → write
- "a" → append

Best practice:

with open(filename) as f:
    for line in f:
        ...

Automatically closes file.

---

## 5. Email Domain Extraction

Split string:

email.lower().split("@")[-1]

Used with Counter to count domains in files.

---

## 6. Delimited Files (CSV)

Delimiter = character separating data.

Examples:
- "," comma
- "\t" tab
- ":" colon

Reading:

csv.reader(file, delimiter="\t")

With headers:

csv.DictReader(file, delimiter=":")

Writing:

csv.writer(file).writerow([...])

---

## 7. Web Scraping

HTML parsing using BeautifulSoup:

soup = BeautifulSoup(html, "html5lib")

Find elements:
- soup.find("p")
- soup.find_all("a")
- soup("p", {"class":"important"})

CSS selectors:

soup.select("div span")

Used for structured extraction.

---

## 8. JSON Data

JSON → structured text format.

Deserialize:
json.loads(string)
json.load(file)

Access fields like dictionary.

---

## 9. APIs and Endpoints

API endpoint = URL providing data.

Example:
GitHub Repositories API

Used to:
- get creation dates
- count by month
- check activity

---

## 10. Date Parsing

API dates are strings.

Use:
dateutil.parser.parse()

Then extract:
- month
- weekday

---

## 11. Twitter API (Concept)

Earlier:
OAuth 1.0 PIN-based login

Now:
Free accounts do not allow search access.

Lesson:
APIs change — code must adapt.

---

## 🔑 Key Concept of Chapter

Before machine learning:
✔ collect  
✔ clean  
✔ structure  

Data engineering is the first step of data science.

---

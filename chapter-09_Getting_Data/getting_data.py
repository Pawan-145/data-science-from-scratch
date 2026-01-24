import sys,re

# sys.argv is the list of the command-line arguments
# sys.argv[0] is the name of the program itself
# sys.argv[1] will be the regex specified at command line 

regex= sys.argv[1] 
tgec = sys.argv[2]

print("REGEX =", regex)
print("tgec=",tgec)

# for every line passed into the script 
for line in sys.stdin:
    print("READ:", repr(line))
    ''' If matches the regex, write it to stdout '''
    if re.search(regex,line) and re.search(tgec,line):
        print("MATCH:", line, end="")
        sys.stdout.write(line)

""" Here id one that count the lines it receives and then writes out the count: """
# import sys
count = 0
for line in sys.stdin:
    count += 1

# print goes to sys.stdout
print(count)

""" Similarly, here's a script that counts the words in its input and writes out the most common ones """

from collections import Counter
#pass in number of word as first argument
try:
    num_words= int(sys.argv[1])
except:
    print("usage: ch9.py num_words")
    sys.exit(1)                # nonzero exit code indicates error

counter = Counter(word.lower()
                  for line in sys.stdin
                  for word in line.strip().split()
                  if word)

for word, count in counter.most_common(num_words):
    sys.stdout.write(str(count))
    sys.stdout.write("\t")
    sys.stdout.write(word)
    sys.stdout.write("\n")


# Reading Files

## The Basics of Text Files

""" First step to working with text file is to obtain a file object using open """
# 'r' means read-only, it's assumed if you leave it out
file_for_reading = open('reading_file.txt','r')
file_for_reading2 = open('reading_file.txt')

file_for_writing = open('writing_file.txt','w')          # Here, w = write
 
file_for_appending = open('writing_file.txt','a')    # 'a' is append -- for adding to end of the file

# To close your file, when you are done
file_for_writing.close()

''' sometime we forget to close files, so use then with block to close automatically '''
filename = 'sample.txt'
with open(filename) as f:
    data = function_that_gets_data_from(f)

""" To read a whole text file, you can just iterate over the lines of the file """

starts_with_hash = 0
with open(filename) as f:
    for line in f:                              # look at each line in the file
        if re.match("^#",line):                 # use a regex to see if it starts with '#'
            starts_with_hash +=1                # If it does, add 1 to the count


def get_domain(email_address: str) -> str:
    """ split on '@' and return the last piece """
    return email_address.lower().split("@")[-1]

assert get_domain('ursusmaritimus@gmail.com') == 'gmail.com'
assert get_domain('ursusmaritimus@mail.articcicle.com') == 'mail.arcticcircle.com'

from collections import Counter
with open('email_address.txt','r') as f:
    domain_count = Counter(get_domain(line.strip())
                           for line in f    # In generators we don't use colon(:) at end of for loop
                            if "@"  in line)
    
    
# Delimited files
"""
Delimited basically means:

something is separated by a specific character (the delimiter)

The delimiter is the character used to separate pieces of data.

Common delimiters: , (comma), \t (tab), | (pipe), ; (semicolon)

"""

# A delimited file is a text file where data fields are separated by a delimiter.

""" process() is just a function that does something with the stock data """

import csv

with open('stock_prices.txt') as f:
    tab_reader = csv.reader(f,delimiter='\t')
    for row in tab_reader:
        date = row[0]
        symbol  = row[1]
        closing_price = float(row[2])
        process(date,symbol,closing_price)              # process is some function that will do operation using these variables

""" If your file has headers """
# you can either skip the header row with an initial call to reader.next or get each row as dict(with headers as keys)

with open('colon_delimited_stock_prices.txt') as f:
    colon_reader  = csv.DictReader(f,delimiter=':')
    for dict_row in colon_reader:
        data = dict_row['data']
        symbol = dict_row['symbol']
        closing_price = float(dict_row['closing_price'])
        process(data,symbol,closing_price)             # process is some function that will do operation using these variables

""" If you file doesn't have headers, you can still use DictReader """

today_prices = {'AAPL':90.91,'MSFT': 41.68, 'FB':64.5}
with open('comma_delimated_stock_prices.txt','w') as f:
    csv_writer = csv.writer(f, delimiter=',')
    for stock,price in today_prices.items():
        csv_writer.writerow([stock,price])


# Scraping the Web

from bs4 import BeautifulSoup
import requests

html = """
<html>
  <head><title>Test Page</title></head>
  <body>
    <p id="first">First paragraph</p>
    <p class="important">Second paragraph</p>
    <p class="important highlight">Third paragraph</p>
    <a href="https://example.com">Example link</a>
  </body>
</html>
"""

# If you are using url then:
# url = ("https://democheck.com/")
# html = requests.get(url).text
# Then use html in Beautifulsoup function

soup = BeautifulSoup(html, "html5lib")

first = soup.find("p")
print(soup.p)  

# Get text
print(soup.p.text)
print(soup.p.text.split())

# Get Attributes
print(soup.p['id'])
print(soup.p.get('id'))

# Find all tags

print(soup.find_all("p"))
print(soup.find_all("a"))
print(soup("p"))

# Paragraphs with id
print(" Paragraphs with id ")
l = [p for p in soup("p") if p.get("id")]
print(l)

# Find my class
print(soup("p", {"class":"important"}))
print(soup("p","important"))

u = [p for p in soup("p") if "important" in p.get("class",[])]  
# If this tag does NOT have a class attribute, return an empty list instead of None
print(u)

# Find Links
for a in soup("a"):
    print(a.text, a.get("href"))

""" You can combine these methods to implement more elaborate logic. 
take example, if you want to find every <span> element that is contained inside a <div> element """

# Warning: will return the same <span> multiple times
# if it sits inside multiple <div>s
# Be more clear in that case 
"""
you can use this for this : 

   soup.select("div span")

This uses CSS selectors:
span inside div
No duplicates. Much cleaner
"""
spans_inside_divs = [span
                     for div in soup('div')                      # for each <div> on the page
                     for span in div('span')]                   # find each <span> inside it 


# Using APIs
""" 
Many websites and webservices provides application programming interfaces (APIs), which allows you to explicity request data in a structured format. This saves you the trouble of having to scrape them
"""

# JSON and XML
""" 
Because HTTP is a protocol for transferring text, the data you request through a web API needs to be serialized into a strong format. Often serialization uses Javascript Object Notation (JSON), It looks quite similar to python dicts
"""

{
    "title": "Avengers End Game",
    "Author": "Stan lee",
    "Characters": ["Iron Man","Captain America","Thor","Hulk"]
}

# We can parson JSON using python's json module
import json
serialized = """ {
    "title": "Avengers_End_Game",
    "Author": "Stan lee",
    "Characters": ["Iron Man","Captain America","Thor","Hulk"]
}"""


# Now we will use loads function to deserialize a string representing a JSON object
deserialized = json.loads(serialized)
assert deserialized["title"] == "Avengers_End_Game"
 

# Some times API provides responses in XML
"""
<Book> 
  <Title>Data Science Book</Title> 
  <Author>Joel Grus</Author> 
  <PublicationYear>2014</PublicationYear> 
  <Topics> 
    <Topic>data</Topic> 
    <Topic>science</Topic> 
    <Topic>data science</Topic> 
  </Topics>
</Book>

"""
# We can use Beautiful Soup to get data from XML similarly to how we used it to get data from HTML



# Unauthenticated API
import requests,json
from collections import Counter
from dateutil.parser import parse
github_user = "use_your_github_username"
endpoint = f"https://api.github.com/users/{github_user}/repos"
""" 
An API endpoint is a specific URL that serves as a unique access point or location where a client application sends requests and where the server receives and processes those requests
"""

repos  = json.loads(requests.get(endpoint).text)
for repo in repos:
    print(repo["name"],"=",repo["created_at"])

# Python doesn't come with great date parser, so we will install:
# python -m pip install python-dateutil

dates = [parse(repo["created_at"]) for repo in repos]
month_counts = Counter(date.month for date in dates)
weekday_counts = Counter(date.weekday() for date in dates)

print("By month:", month_counts)
print("By weekday:", weekday_counts)


# Languages of last 5 repositories
last_5_repositories = sorted(
    repos,
    key=lambda r:r["pushed_at"],
    reverse=True
)

last_5_languages = [repo["language"]
                    for repo in last_5_repositories]

print(last_5_languages)


# Using the Twitter APIs
# Twython
""" To install use:
python -m pip install twython 
"""

import json

with open("secrets.json", "r") as f:
    deserialized = json.load(f)
    
CONSUMER_KEY = deserialized['TWITTER_CONSUMER_KEY']
CONSUMER_SECRET = deserialized['TWITTER_CONSUMER_SECRET']


import webbrowser
from twython import Twython

# For authentication url, get a temporary client
temp_client = Twython(CONSUMER_KEY, CONSUMER_SECRET)
temp_creads = temp_client.get_authentication_tokens()
url =  temp_creads['auth_url']

# Now visit URL to authorize the application and get the pin



print(f"{url}")
webbrowser.open(url)
PIN_CODE = input("please enter the PIN code: ")

# Now we use that PIN_CODE to get the actual tokens
auth_client = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    temp_creads["oauth_token"],
    temp_creads["oauth_token_secret"])
final_step = auth_client.get_authorized_tokens(PIN_CODE)
ACCESS_TOKEN  = final_step['oauth_token']
ACCESS_TOKEN_SECRET  = final_step['oauth_token_secret']

# And get a new Twython instance using them
twitter = Twython(
    CONSUMER_KEY,
    CONSUMER_SECRET,
    ACCESS_TOKEN,
    ACCESS_TOKEN_SECRET
)

# search for tweets containing the phrase "data science"

for status in twitter.search(q='"data science"')["statuses"]:
    user = status["user"]["screen_name"]
    text = status["text"]
    print(f"{user}: {text}\n")



""" 
PIN-based authentication (OAuth 1.0a) is not available on free Twitter/X accounts as of now.
so this will not work.

⚠️ Important Reality

Even if your keys are correct, with a free developer plan on Twitter/X, PIN-based OAuth almost certainly won’t work anymore.

Many old Twython tutorials break for this reason.

Twitter/X now requires OAuth 2.0 Bearer token or paid plan for searching or reading tweets.

"""

import requests
from bs4 import BeautifulSoup

# Requests for a file at this URL
res = requests.get('https://news.ycombinator.com/news')


# Uses the text version of the response and parses it into html format
soup = BeautifulSoup(res.text, 'html.parser')
print(soup.a)  # Prints first a tag
# Output:
# <a href="https://news.ycombinator.com"><img height="18" src="y18.gif" style="border:1px white solid;" width="18"/></a>

print()

print(soup.body)  # Prints the body tag

print()

print(soup.find(id='score_21762640'))  # Returns the tag that has this id
# Output:
# <span class="score" id="score_21762640">223 points</span>


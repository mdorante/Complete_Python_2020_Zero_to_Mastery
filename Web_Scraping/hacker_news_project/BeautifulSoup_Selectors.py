import requests
from bs4 import BeautifulSoup

# Requests for a file at this URL
res = requests.get('https://news.ycombinator.com/news')

# Uses the text version of the response and parses it into html format
soup = BeautifulSoup(res.text, 'html.parser')

# CSS Selectors point to HTML elements
print(soup.select('#score_21762640'))
# Output:
# [<span class="score" id="score_21762640">374 points</span>]


# Returns all elements that are part of the 'storylink' class
links = soup.select('.storylink')
# Returns all the elements that have the 'score' class
votes = soup.select('.score')
# NOTE: These return lists

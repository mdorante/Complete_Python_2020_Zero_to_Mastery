import requests
from bs4 import BeautifulSoup
import pprint

# Requests for a file at this URL
res = requests.get('https://news.ycombinator.com/news')
# Uses the text version of the response and parses it into html format
soup = BeautifulSoup(res.text, 'html.parser')

# Returns all elements that are part of the 'storylink' class
links = soup.select('.storylink')
# Returns all the elements that have the 'subtext' class
subtext = soup.select('.subtext')
# NOTE: These return lists

# Requests file for page 2
page2 = requests.get('https://news.ycombinator.com/news?p=2')
soup2 = BeautifulSoup(page2.text, 'html.parser')

links2 = soup2.select('.storylink')
subtext2 = soup2.select('.subtext')


def sort_stories_by_votes(hnlist):
    return sorted(hnlist, key=lambda k: k['votes'], reverse=True)


def create_custom_hn(links, subtext):
    hn = []
    for idx, item in enumerate(links):
        title = item.getText()
        href = item.get('href', None)
        vote = subtext[idx].select('.score')
        if len(vote):
            points = int(vote[0].getText().replace(' points', ''))
            if points > 100:
                hn.append({'title': title, 'link': href, 'votes': points})
    return sort_stories_by_votes(hn)


# Using pretty print, we get a clean output
print('Page 1: \n')
pprint.pprint(create_custom_hn(links, subtext))

print('\nPage 2: \n')
pprint.pprint(create_custom_hn(links2, subtext2))

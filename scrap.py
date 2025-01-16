import requests
from bs4 import BeautifulSoup
import pandas as pd


url = 'https://www.nytimes.com/column/global-health'

response = requests.get(url)

if response.status_code == 200:
    print("Successfully fetched the web page!")
else:
    print(f"Failed to retrieve the page with status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

articles = soup.find_all('article')

headlines = []
summaries = []
links = []

print("Top Global Health News from The New York Times:")

for article in articles:
    headline_tag = article.find('h3')
    summary_tag = article.find('p')
    link_tag = article.find('a', href=True)

    if headline_tag and link_tag:
        headline = headline_tag.get_text(strip=True)
        link = "https://www.nytimes.com" + link_tag['href']
        summary = summary_tag.get_text(strip=True) if summary_tag else 'No summary available.'
        
        headlines.append(headline)
        summaries.append(summary)
        links.append(link)
        print("Headline:",headline, "Link: ", link, "Summary:", summary, "\n")
     
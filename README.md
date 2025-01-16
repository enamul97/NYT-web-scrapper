# NYT-web-scrapper
This repository contains Python scripts for scraping and searching articles from The New York Times website. 

## Features

### 1. `scrap.py`
- Scrapes the latest articles from the **Global Health** column of *The New York Times*.
- Extracts article headlines, summaries, and links.
- Displays the data directly in the terminal.

### 2. `article_search.py`
- Retrieves the top 10 news articles based on a specific keyword.
- Allows filtering articles within a custom date range (start date to end date).
- Outputs the headline, publication date, and URL in decreasing order of publication date.

---
## Requirements
To use the scripts, ensure you have the following:
1. Python 3.x
2. requests library
3. beautifulsoup4 library
4. pynytimes library
5. NY Times API: Create an API key by visiting: [The New York Times Developer Portal](https://developer.nytimes.com/apis)


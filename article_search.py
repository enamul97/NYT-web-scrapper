#!/usr/bin/python3.6
from datetime import datetime
from pynytimes import NYTAPI

class ArticleSearch:
    def printArticles(self, articles):
        i = 0
        for x in range(len(articles)):
            i += 1
            print(i,"HeadLine: "+articles[x]['headline']['main']
                +", Publication Date: "+articles[x]['pub_date'][0:11]
                +", Web URL: "+articles[x]['web_url'])
            print("\n\n") 

    def search(self,topic,startDate, endDate):
        nyt = NYTAPI("API_KEY")
        startDate=str(startDate)+" 00:00:00"
        endDate=str(endDate)+" 23:59:59"
        articles = nyt.article_search(
            query = topic,
            dates = {
                "begin": datetime.strptime(startDate,'%Y-%m-%d %H:%M:%S'),
                "end": datetime.strptime(endDate,'%Y-%m-%d %H:%M:%S')
            },
            options = {
                "sort": "relevance",
                "sources": [
                    "New York Times"
                ],

                "type_of_material": [
                    "News"
                ]
            }
        )
        sorted_articles = sorted(articles, key=lambda x: datetime.strptime(x['pub_date'][0:10], '%Y-%m-%d'), reverse=True)
        for x in range(len(sorted_articles)):
          sorted_articles[x]['pub_date']=datetime.strptime(sorted_articles[x]['pub_date'][0:10], '%Y-%m-%d').strftime('%d-%b-%Y')
        return sorted_articles


    def main(self):
        keyword = 'pandemic'
        startDate = '2025-1-1'
        endDate = '2025-1-15'
        results = self.search(keyword, startDate, endDate)
        self.printArticles(results)


# obj = ArticleSearch()
# obj.main()

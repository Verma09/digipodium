import requests
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text,'lxml')


def get_news():
    soup = get_soup('https://www.ndtv.com/latest')
    target = soup.find('div',attrs={'class':'lisingNews'})
    newslist = target.find_all('div',attrs= {'class','news_Itm'})
    data = []
    for news in newslist:
        title = news.find('h2',attrs = {'class' : 'newsHdng'})
        details = news.find('span',attrs = {'class': 'posted-by'})
        content = news.find('p', attrs = {'class' :'newsCont'})
        
        if title and details and content:
            data.append(title.text.strip())
        else:
            print('No data found') 
    return data
if __name__ == '__main__':
    print(get_news())    

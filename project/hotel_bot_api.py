import requests
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text,'lxml')


def get_news():
    soup = get_soup('https://www.booking.com/luxury/city/in/lucknow.en-gb.html?aid=375816&label=lucknow-gl2nNOqb%2AQ5ubriHBjQS5wS388159455975%3Apl%3Ata%3Ap1%3Ap2%3Aac%3Aap%3Aneg%3Afi%3Atikwd-3112543807%3Alp9303169%3Ali%3Adec%3Adm%3Appccp%3DUmFuZG9tSVYkc2RlIyh9YboIMJYQAPicNVDGWXPgwtU&sid=96e7fe69f3ec65251d0877510e2afa1c&keep_landing=1&gclid=CjwKCAiA7vWcBhBUEiwAXieItpzG7UPW8X0EGHz6M5FySPt8j-wDhPn2bUC6B_ENXk-amgHcsKMLSxoCcZUQAvD_BwE&')
    
    target = soup.find('div',attrs={'class':'content__col'})
    hotellist = target.find_all('div',attrs= {'class','sr__card_main'})
    data = []
    for news in hotellist:
        title = hotel.find('h2',attrs = {'class' : 'bui-spacer--smaller'})
        details = hotel.find('span',attrs = {'class': 'bui-card__title'})
        content = hotel.find('p', attrs = {'class' :'hotel-card__text bui-spacer--medium'})
        
        if title and details and content:
            data.append(title.text.strip())
        else:
            print('No data found') 
    return data
if __name__ == '__main__':
    print(get_hotel())    

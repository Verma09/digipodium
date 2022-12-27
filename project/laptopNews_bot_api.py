import requests
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'lxml')


def get_laptopNews():
    soup = get_soup('products wrapper grid products-grid')
    
    target = soup.find('div', attrs={'class':'class="products list items product-items"'})
    laptopNewslist = target.find_all('div', attrs={'class':'products list items product-items'})
    data = []
    for news in laptopNewslist:
        title = laptopNews.find('h2', attrs={'class':'a-size-mini a-spacing-none a-color-base s-line-clamp-2'})
        
        content = laptopNews.find('span', attrs={'class':'a-size-medium a-color-base a-text-normal'})
        if title and details and content:
            data.append(title.text.strip())
        else:
            print('no data found')
    return data

if __name__ == '__main__':
    print(get_laptopNews())
    

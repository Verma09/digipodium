import requests
from bs4 import BeautifulSoup

def get_soup(url):
    page = requests.get(url)
    return BeautifulSoup(page.text, 'lxml')


def get_weather():
    soup = get_soup('https://www.google.com/search?rlz=1C1JJTC_enIN992IN992&sxsrf=ALiCzsaSDX5U-m7-92suoAtLbPWW-T5SWg%3A1669048945269&lei=cap7Y-L9D9aXseMPjbCdqAc&q=weather%20today%20at%20my%20location&ved=2ahUKEwii-vrr27_7AhXWS2wGHQ1YB3UQsKwBKAN6BAhcEAQ&biw=1242&bih=597&dpr=1.1')
    target = soup.find('div', attrs={'class':'MjjYud'})
    newslist = target.find_all('div', attrs={'class':'KIy09e obcontainer wDYxhc'})
    data = []
    for weather in newslist:
        title = weather.find('h1', attrs={'class':'Weather result'})
        details = weather.find('span', attrs={'class':'aqi_hdr_tri'})
        
        if title and details and content:
            data.append(title.text.strip())
        else:
            print('no data found')
    return data

if __name__ == '__main__':
    print(get_weather())
    

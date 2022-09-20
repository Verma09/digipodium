from dputils import scrape
import pandas as pd
# step1 : get the data as soup
# step2 : create the setup dicitionaries
# step3 : pass the dictionaries (most important)
# step4 : repeat step 1 to step step3 until data keep coming
# step5 : check and save data into a file.

# understanding the url
def getdata(q):
    t = {'tag':'div', 'attrs':{'class':'_1yokD2_3Mn1Gg'}}
    rep_items = {'tag':'div', 'attrs':{'class':'_1AtVbE col-12-12'}}
    title = {'tag':'div', 'attrs':{'class':'_4rR01T'}}
    price = {'tag':'div', 'attrs':{'class': '_30jeq3 _1_WHN'}}
    link = {'tag':'a', 'attrs':{'class': '_1fQZEK'}, 'output':'href'}
# step1
   # query = 'laptop'
    pos = 1
    all_data = []
    while True:
        url = f'https://www.flipcart.com/search?q={laptops}&page={pos}'
        print(url)
        soup = scrape.get_webpage_data(url)
        data = scrape.extract_many(soup, target= t, items=trep_items, title = title, price = price, linl = link)
        if isinstance(data, list):
            if len(data) > 0:
                pos += 1
                all_data.extend(data)
            else:
                break
        else:
            break
        
    return all_data  

    # use  
# laptops = getdata('laptops')
 # pd.dataframe(laptops).to_csv('laptop_data.csv')




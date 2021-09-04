#This is web project

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import requests # allow us to download the desired HTML
from bs4 import BeautifulSoup
import pprint
#BeasutifulSoup allows to use the HTML and grab different data from HTML to scrap.

#for multiple pages use URL look at training.

def scrapper(weblink):
    """
    :rtype: html document - text only
    """
    resobject=requests.get(weblink)
    # print(resobject)
    if resobject:
        #print(resobject.text) # it gives html text not actual html
        soupobj=BeautifulSoup(resobject.text, 'html.parser') # This will convert text to html
        #Beautifulsoup allows various parsers go to the site and search for "installing a parser"
        #print(soupobj.body.contents)
        #print(soupobj.find_all('div'))  #all divs from page in list
        #print(soupobj.find_all('a')) #all links from page in list
        #print(soupobj.find('a')) #it finds the first link of the page.
        #print(soupobj.find(id='unv_27649123'))
        links=soupobj.select('.storylink')
        subtext=soupobj.select('.subtext')
        hackernews = create_custom_news(links,subtext)
        pprint.pprint(hackernews)

def create_custom_news(links, subtext):
    """ return hackernews links and votes"""
    hackernews=[]
    for indx,item in enumerate(links):
        title = links[indx].getText()
        href = links[indx].get('href', None)
        votes = subtext[indx].select('.score')
        if len(votes):
            points = int(votes[0].getText().replace(' points', ''))
            #print(points)
            if points >99:
                hackernews.append({'title': title, 'link': href, 'point': points})

    return sort_stories_by_points(hackernews)

def sort_stories_by_points(hackernewslst):
    return sorted(hackernewslst, key=lambda k:k['point'], reverse=True)







# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    weblink = 'https://news.ycombinator.com/'
    scrapper(weblink)



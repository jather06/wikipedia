import requests
from bs4 import BeautifulSoup
import webbrowser

while True:
    ranarticle = requests.get('https://en.wikipedia.org/wiki/Special:Random')
    soup = BeautifulSoup(ranarticle.content, 'html.parser')
    title = soup.find(class_="firstHeading").text
    print(f'{title} \nDo you want to read this? (Y/n)')
    ans = input('').lower()

    if ans == 'y':
        url='https://en.wikipedia.org/wiki/%s' %title
        webbrowser.open(url)
        break
    if ans == 'n':
        print('Ah I see you\'re quite the picky one, here\'s a new link\n-------------------------------')
        continue

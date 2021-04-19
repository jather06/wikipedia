import random
import webbrowser
import wikipedia
from time import sleep
links = []

articles = []
article_depth = 0
depth_input = int(input('how many layers do you want to search through?\n'))

for i in range(depth_input):
    # asks what page you want to go start with.
    if article_depth == 0:
        input_page = input('what page do you want to navigate to?\n')
        original_input_page = input_page.upper()
    # adds the current wiki link to the links list. 
    links = wikipedia.page(input_page).links
    
    # chooses a new article, adds it to the article list and makes it the new 'input page'
    # so that it can be used in the next iteration
    new_article = random.choice(links)
    articles.append(new_article)
    input_page = new_article
    article_depth += 1
webbrowser.open('https://en.wikipedia.org/wiki/' + (articles[-1]))
articleorder = '\n==> '.join(articles)
print('\n==> ' + original_input_page + '\n==> ' + articleorder)
sleep(2)
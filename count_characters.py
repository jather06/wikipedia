import matplotlib.pyplot as plt
import numpy as np
import wikipedia
import string
import random
import re
from time import sleep


def count_chars():
    global input_page
    input_page = input('what page do you want to search? \n')
    content_in_page = wikipedia.page(input_page).content.lower()
    content_in_page = re.sub(r'[^a-z]', '', content_in_page)
    global frequency
    global alphabet
    alphabet = list(string.ascii_lowercase)
    frequency = [0] * 26

    for c in content_in_page:
        index_alphabet = alphabet.index(c)
        frequency[index_alphabet] += 1
        

def bar_chart():
    plt.close()
    xpos = np.arange(len(alphabet))
    # frequency is initialized already

    plt.bar(xpos,frequency, label="freq", alpha=0.4)
    
    font1 = {'family':'serif','color':'darkred','size':15}
    font2 = {'family':'serif','color':'darkred','size':18}
    plt.xticks(xpos,alphabet)
    plt.ylabel("frequency", fontdict=font1)
    plt.title('character frequency in ' + input_page, fontdict=font2)
    plt.ioff()
    plt.show()
def main():
    count_chars()
    bar_chart()
    
    
again = 'y'
while again.lower() == 'y':
    main()
    again = input('want to do this for another page? (y/n)\n')
    sleep(0.5)
    
    
# Written by: Shruti Thakur
#To remove the URLs and special characters like emojis from the tweets

import re

def testing():
    with open("xyz.txt", "r") as ins: #xyz.txt is the file with all the tweets after automated classification
        for line in ins:
            x = re.sub(r"\\x\S+", "", line)
            y = re.sub(r"http\S+", "", x)
            fopen = open('abc.txt', 'a', encoding='utf-8')  #abc.txt is the file with all URLs and special characters removed
            fopen.write(y.lower())
            fopen.close()
testing()
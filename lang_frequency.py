     # -*- coding: utf-8 -*- 
from collections import Counter

def load_data(filepath):
    with open(filepath,'r') as file:
     data = file.read() 
     file.close()
    return data
   

def get_most_frequent_words(text):
    textlist = text.split()
    out_put = Counter(textlist).most_common(10)
    return out_put


if __name__ == '__main__':
    filepath = input ("Enter path to file")
    text = load_data(filepath) 
    print (get_most_frequent_words(text))

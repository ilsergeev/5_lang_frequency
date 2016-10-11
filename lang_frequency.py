# -*- coding: utf-8 -*- 

def load_data(filepath):
    with open(filepath,'r') as file:
     data = file.read() 
     file.close()
    return data
   

def get_most_frequent_words(text):
    pass


if __name__ == '__main__':
    filepath = '/projects/5_lang_frequency/tst_text.txt'
    print (load_data(filepath))

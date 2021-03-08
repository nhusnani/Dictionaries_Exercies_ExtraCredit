'''
dict = {"Father": 0, "God": 0, "Christ": 0, "Spirit": 0, "life": 0, "man": 0}
text = open("book of John text.txt", "r") 
  

for line in text: 
    line = line.strip() 
    words = line.split(" ") 
  
    for word in words: 
        if word in dict: 
            dict[word] = dict[word] + 1

for key in list(dict.keys()): 
    print(key, ":", dict[key])
'''


lookup_dict = {"Father": 0, "God": 0, "Christ": 0, "Spirit": 0, "life": 0, "man": 0}

book_text = open("book of John text.txt", "r")

book_string = book_text.read()

book_word = book_string.split()


for word in book_word:
    if lookup_dict.get(word, None) is not None:
        lookup_dict[word] += 1

for key, value in lookup_dict.items():
    print(key, ": ", value)


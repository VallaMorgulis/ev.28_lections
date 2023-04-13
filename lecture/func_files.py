def longest_words(filename: str):
    with open(filename) as file:
        list_ = file.readlines()

    list_ = [x.replace('\n', '').strip() for x in list_]
    string = ''
    for item in list_:
        string = string + ' ' + item
    list_words = string.split()
    r = 0
    for i in range(len(list_words)):
        if r < len(list_words[i]):
                r = len(list_words[i])               
    longest_w = [list_words[i] for i in range(len(list_words)) if len(list_words[i]) == r]
    
    if len(longest_w) > 1:
         return longest_w
    else:
         return longest_w[0]
    

def shortest_word(filename: str):
    with open(filename) as file:
        list_ = file.readlines()

    list_ = [x.replace('\n', '').strip() for x in list_]
    string = ''
    for item in list_:
        string = string + ' ' + item
    list_words = string.split()
    r = len(max(list_words, key=len))
    for i in range(len(list_words)):
        if r > len(list_words[i]):
                r = len(list_words[i])
    shortest_w = [list_words[i] for i in range(len(list_words)) if len(list_words[i]) == r]  
     
    if len(shortest_w) > 1:
         return shortest_w
    else:
         return shortest_w[0]



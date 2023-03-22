import os

def dict_conversion(list):
    dictionary = {
        list[item] : list[item +1] for item in range(0, len(list), 2)
    }
    return dictionary



if __name__ == '__main__':



    with open('shows.txt', 'r') as shows:
        words_list = shows.readlines()
        print(words_list)

    for word in words_list:
        new_word = word.replace("\n", "")
        

    print(dict_conversion(words_list))




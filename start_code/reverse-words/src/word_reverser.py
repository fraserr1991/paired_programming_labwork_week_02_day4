#take input of string of words from test
def reverse_word(phrase):
    list_of_words = phrase.split(" ")
    #how do you seperate a word in a string by space
    combined_words = []

    for word in list_of_words:
        if len(word) >= 5:
            combined_words.append(word[::-1])
        else:
            combined_words.append(word)

    separator = " "
    final_words = separator.join(combined_words)

    return final_words

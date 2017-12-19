

def is_valid_pass_phrase(phrase):
    """Phrase is a list of strings"""

    word_dict = dict()
    for word in phrase:

        if word in word_dict:
            return False
        else:
            word_dict[word] = ''

    return True


if __name__ == "__main__":

    f = open('data.txt', 'r')
    phrases_text = f.read()
    f.close()

    phrases = phrases_text.split(chr(10))

    list_of_phrases = [phrase.split(" ") for phrase in phrases]

    print("Number of phrases: %d" % len(list_of_phrases))

    print("Valid phrases: %d" % len([phrase for phrase in list_of_phrases if is_valid_pass_phrase(phrase)]))

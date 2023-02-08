import string

def c_w(file):
    with open(file, 'r') as f:
        text = f.read().translate(str.maketrans('', '', string.punctuation))
        print(text)

        # split the text into words
        split = text.split()

        # create an empty dictionary to store the word count
        em_dict = {}

        # iterate through the words and count the occurrences
        for s in split:
            if s in em_dict:
                em_dict[s] += 1
            else:
                em_dict[s] = 1

    return em_dict

file = 'text1'
word_count = c_w(file)
print(word_count)
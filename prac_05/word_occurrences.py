text = input("Enter text: ")
text_words = text.split(" ")
word_count = {}
count = 0
for word in text_words:
    if word not in word_count:
        word_count[word] = 1
    else:
        count = word_count.get(word, 0)
        word_count[word] = count + 1
for word in text_words:
    if len(word) > count:
        count = len(word)
text_words = list(word_count.keys())
text_words.sort()
for word in text_words:
    print("{:{}} = {}".format(word, count, word_count[word]))

#Updating to feedback branch
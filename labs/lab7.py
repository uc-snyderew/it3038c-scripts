from /usr/local/lib/python3.6/site-packages/TextStatistic import count_words

Print("Enter the name of the file you want to get a word count from.")

filename = input()
cw = count_words (filename)
print(cw)

import gensim
import csv

model = gensim.models.KeyedVectors.load_word2vec_format('./GoogleNews-vectors-negative300.bin.gz', binary=True)

sentence = input("Type your sentence: ")
words = sentence.split()
new_sentence = []
total_words = []
is_int = False

while True:


    while not is_int:
        n = int(input("how many sentences?"))

        if isinstance(n, int):
            for i in range(0, n):
                temp = ("sentence "+ str(i))
                list_temp = []
                list_temp.append(temp)
                total_words.append(list_temp)
            is_int = True

    for word in words:
        try:
            #each y is a sentence
            new_words = (model.most_similar(positive=[word], topn=n))
            #print(new_words)
            new_sentence.append(new_words[0][0])
            #total_words.append(new_words[0][0])

            #new_word is a list of lists of tuples
            #each z is a position
            y = 0
            for new_word in new_words:
                
                #out_word is the string
                out_word = new_word[0]
                total_words[y].append(out_word)
                y += 1

        except:
            print(word, " is not in dictionary")
            continue
    
    with open("output.csv", "a") as endFile:
        out_writer = csv.writer(endFile, delimiter="|")
        for sentence in total_words:
            out_writer.writerow(sentence)

    words = []
    for word in new_sentence:
        words.append(word)
    
    new_sentence = []

    #this is the total output
    #delete first because it doesn't make sense
    #to have sentence 0
    del total_words[0]
    for out_sent in total_words:
        print(out_sent)

    x = input("Type 'quit' to stop or 'new' to try again: ")

    if x == 'quit':
        exit()

    if x == 'new':
        sentence = input("Type your sentence: ")
        words = sentence.split()
        is_int = False
        total_words = []


    else:
        continue

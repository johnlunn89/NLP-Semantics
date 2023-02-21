import spacy

# I have had to use the file directory location for the module as pycharm could not load it the conventional way
# due to some issue with how my laptop is storing the files I have not yet been able to resolve
nlp = spacy.load(r"C:\Users\John\AppData\Local\Programs\Python\Python311\Lib\site-packages\en_core_web_md\en_core_web_md-3.5.0")

word1 = nlp("cat")
word2 = nlp("monkey")
word3 = nlp("banana")

print(word1.similarity(word2))
print(word3.similarity(word2))
print(word3.similarity(word1))

# cat and monkey have similarity of 0.59
# monkey and banana have similarity of 0.40
# cat and banana have similarity of 0.22
# cat and monkey are similiar because they are animals. Monkey and banana have higher similarity than cat and banana
# because monkeys are more traditionally associated with bananas than cats are


# when I ran the above comparisons with the 'sm' language module the scores for each were much higher;
# cat and monkey - 0.59
# monkey and banana - 0.73
# cat and banana - 0.68
# Somehow the cat and banana have a higher similiarity score than the cat and monkey, and the score is 3x higher than
# on the previous run


tokens = nlp("tree trunk leaf sap blossom bark")

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

# in my example above tree and leaf have a 0.64 score which seems low,
# especially considering that bark/sap have a 1.0 score (sap can be used like: 'sap their energy' so for it to
# be a 1.0 score is also interesting
# tree and trunk are 0.55 similiar. Trunk has a lot of other uses so this makes sense
# tree and turn had a score of 0.54


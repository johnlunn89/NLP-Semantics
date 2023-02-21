# Import modules for use in code - spacy for NLP, numpy for argmax

import spacy
import numpy

#import medium module for NLP

nlp = spacy.load(r"C:\Users\John\AppData\Local\Programs\Python\Python311\Lib\site-packages\en_core_web_md\en_core_web_md-3.5.0")


# create two empty lists, one for movies.txt to be read into, one for similarity scores to be saved in
movies = []
similarity_scores = []


# reads in .txt file and tidies it up by stripping new lines values
with open("movies.txt", "r") as file:
    for line in file:
        movies.append(line.rstrip(", ").rstrip("\n"))

# planet hulk description saved as a var
planet_hulk = "Will he save their world or destory it? When the hulk becomes too dangerous for the Easth, the " \
              "illuminati trick Hulk into a shuttle and launch him into space to a planet where the " \
              "Hulk can live in peace.Unfortunately, Hulk lands on the planet Sakaar where he is sold into " \
              "slavery and trained as a gladiator."


# function uses a loop to create tokens from the list and pass them through NLP, appends score to list2
# uses argmax function to find idx pos of highest value, uses this in print statement
def semantic_comp(list, list2, var):
    for token in list:
        token = nlp(token)
        var_ = nlp(var)
        list2.append(token.similarity(var_))
    movie_pos = numpy.argmax(list2)
    print(f"The most similar movie is {list[movie_pos][:7]}")

# function call
semantic_comp(movies, similarity_scores, planet_hulk)

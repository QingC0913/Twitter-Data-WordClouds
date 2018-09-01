import json
from textblob import TextBlob
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt
from wordcloud import WordCloud


idx = 0
i = 0
polaritySum = 0
subjectivitySum = 0

tweetfile = open("tweetData.json", "r")
tweetData = json.load(tweetfile)
tweetfile.close()

subjectivity = []
polarity = []
for i in range(len(tweetData)) :
    tb = TextBlob(tweetData[i]["text"])
    polarity.append(tb.polarity)
    subjectivity.append(tb.subjectivity)

for idx in range(len(polarity)) :
    polaritySum = polaritySum + polarity[idx]
    subjectivitySum = subjectivitySum + subjectivity[idx]

polarityAverage = polaritySum/len(polarity)
subjectivityAverage = subjectivitySum/len(subjectivity)

#print ("The average polarity of tweets is: ", polarityAverage)
#print ("The average subjectivity of tweets is: ", subjectivityAverage)

num_bins = 20
def polHisto():
    n, bins, patches = plt.hist(polarity, num_bins, facecolor="aqua", alpha=0.5)
    plt.title("Histogram of Polarity")
    plt.xlabel("Polarity")
    plt.ylabel("Frequency")
    plt.axis([-0.5, 1, 0, 45])
    plt.show()

def subHisto():
    n, bins, patches = plt.hist(subjectivity, num_bins, facecolor="#4717F6", alpha=0.5)
    plt.title("Histogram of Subjectivity")
    plt.xlabel("Subjectivity")
    plt.ylabel("Frequency")
    plt.axis([0, 1, 0, 35])
    plt.show()

bigString = ""
for t in range(len(tweetData)):
        bigString = bigString + (tweetData[t]["text"])
bigString= bigString.lower()

wordList = ""

for word in bigString.split():
    if ('https') in word or ('@') in word or ("re") in word or ("rt") in word:
        continue
    elif ('#') in word:
        word = word.replace("#", "")
        wordList = wordList + word + " "
        continue
    elif len(word) <= 3:
        continue
    else:
        wordList = wordList + word + " "


negString = ''
posString = ''
neutString = ''

for word in bigString.split():
    tb = TextBlob(word)

    if ('https') in tb or ('@') in tb or ("re") in tb or ("rt") in tb or (".") in tb:
        continue
    elif ('#') in tb:
        tb = tb.replace("#", "")
        if tb.polarity > 0 :
            str(tb)
            posString = posString + word + " "
        elif tb.polarity < 0 :
            str(tb)
            negString = negString + word + " "
        else:
            str(tb)
            neutString = neutString + word + " "
    elif len(tb) <= 3:
        continue
    else:
        tb = tb.replace("#", "")
        if tb.polarity > 0 :
            str(tb)
            posString = posString + word + " "
        elif tb.polarity < 0 :
            str(tb)
            negString = negString + word + " "
        else:
            str(tb)
            neutString = neutString + word + " "

def posWordCloud():
    wordcloud = WordCloud().generate(posString)
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def negWordCloud():
    wordcloud = WordCloud().generate(negString)
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def neutWordCloud():
    wordcloud = WordCloud().generate(neutString)
    # Display the generated image:
    # the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

def allWordCloud():
    wordcloud = WordCloud().generate(wordList)
    # Display the generated image:
    #the matplotlib way:
    import matplotlib.pyplot as plt
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis("off")
    plt.show()

polHisto()
subHisto()
allWordCloud()
posWordCloud()
negWordCloud()
neutWordCloud()

'''
Written by Ankeet Tendulkar
'''

import nltk
import pandas as pd

trainFile = pd.read_csv('train.csv')

listOfFeatures = []
listOfLabels = []

def convertToBigrams(l):
    onlyTokens = []
    bigramList = []
    for i in range(0, len(l)):
        onlyTokens.append(l[i][0])
    for i in range(0, len(onlyTokens)):
        if(i == 0):
            bigramList.append("#_" + onlyTokens[i])
        else:
            bigramList.append(onlyTokens[i-1] + "_" + onlyTokens[i])
    return bigramList

for i in range(0,len(trainFile)):
    #print(trainFile["Tweet"][i])
    tweet = nltk.word_tokenize(trainFile["Tweet"][i])
    posTaggedTweet = nltk.pos_tag(tweet)
    #print(posTaggedTweet)
    featureDictionary = {}
    listOfBigrams = convertToBigrams(posTaggedTweet)
    for j in range(0,len(posTaggedTweet)):
        key = posTaggedTweet[j][0]
        #val = key
        val = posTaggedTweet[j][1]
        #val = listOfBigrams[j]
        featureDictionary[key] = val

    #print(featureDictionary)
    listOfFeatures.append(featureDictionary)
    listOfLabels.append(trainFile["Type"][i])
    #print(listOfLabels[i])

trainInput = []
for i in range(0,len(listOfFeatures)):
    trainInput.append((dict(listOfFeatures[i]),listOfLabels[i]))

print(len(listOfFeatures))
print(listOfFeatures[0])
print("Training Input Ready")

maxent = nltk.MaxentClassifier.train(trainInput)
print("Done Training")

testFile = pd.read_csv('test.csv')
outputFile = open("OutputMaxEntLen.csv",'w')
outputFile.write("Tweet,Type\n")

for i in range(0,len(testFile)):
    tweet = nltk.word_tokenize(testFile["Tweet"][i])
    posTaggedTweet = nltk.pos_tag(tweet)
    featureDictionary = {}
    listOfBigrams = convertToBigrams(posTaggedTweet)
    for j in range(0,len(posTaggedTweet)):
        key = posTaggedTweet[j][0]
        #val = key
        val = posTaggedTweet[j][1]
        #val = listOfBigrams[j]
        featureDictionary[key] = val
    label = maxent.classify(featureDictionary)
    outputFile.write(testFile["Tweet"][i].replace(",","") + "," + label + "\n")

outputFile.close()

print("Done Classifying Program")

checkFile = pd.read_csv('test.csv')
output = pd.read_csv('OutputMaxEntLen.csv')

#numberOfMismatch = 0

trueLabels = []
predictedLabels = []
labels = ["AbusiveHC","NonAbusiveHC","AbusiveDT","NonAbusiveDT"]

for i in range(0,len(checkFile)):
    trueLabels.append(checkFile["Type"][i])
    predictedLabels.append(output["Type"][i])

#print("Mismatches = {}".format(numberOfMismatch))
print("Total = {}".format(len(checkFile)))

from sklearn.metrics import classification_report
# getting a full report
print(classification_report(trueLabels, predictedLabels, target_names=labels))
print("Done Classifying....")

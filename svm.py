'''
Written by Aanchal Y Gupta
'''

import nltk
import pandas as pd
from sklearn.svm import LinearSVC
#import nltk


from nltk import word_tokenize,sent_tokenize
file_train = pd.read_csv('train.csv')

# tweet = nltk.word_tokenize(trainFile["Tweet"][0])
# posTaggedTweet = nltk.pos_tag(tweet)
# print(posTaggedTweet)
exp={}
features_list = []
labels_list = []
n_gram=''
for i in range(0,len(file_train)):
    tweet = nltk.word_tokenize(file_train["Tweet"][i])
    posTaggedTweet = nltk.pos_tag(tweet)
    #print(posTaggedTweet)
    feature_Dictionary = {}
    for j in range(0,len(posTaggedTweet)):
        key = posTaggedTweet[j][0]
        #val = posTaggedTweet[j][0] #For tokens
        #val=posTaggedTweet[j][1] #for pos tags
        #val = str(len(posTaggedTweet[j][0])) #for length of token
        if(len(posTaggedTweet[j][0])%2==0):
            val='1'
        else:
            val='0'
        feature_Dictionary[key] = val

    #print(featureDictionary)
    features_list.append(feature_Dictionary)

    labels_list.append(file_train["Type"][i])
    #print(listOfLabels[i])
    var=file_train["Type"][i]
    #print(var)

trainInput = []
for i in range(0,len(features_list)):
    trainInput.append((dict(features_list[i]),labels_list[i]))


classifier = nltk.classify.SklearnClassifier(LinearSVC())
classifier.train(trainInput)

testFile = pd.read_csv('test.csv')
outputFile = open("OutputSVM.csv",'w')
outputFile.write("Tweet,Type\n")

for i in range(0,len(testFile)):
    tweet = nltk.word_tokenize(testFile["Tweet"][i])
    posTaggedTweet = nltk.pos_tag(tweet)
    featureDictionary = {}
    for j in range(0,len(posTaggedTweet)):
        key = posTaggedTweet[j][0]
        #val = posTaggedTweet[j][0] #for tokens
        #val = posTaggedTweet[j][1]  # for pos tags
        #val = str(len(posTaggedTweet[j][0]))  # for length of token
        if (len(posTaggedTweet[j][0]) % 2 == 0):
            val = '1'
        else:
            val = '0'
        featureDictionary[key] = val
    label = classifier.classify(featureDictionary)

    outputFile.write(testFile["Tweet"][i].replace(",","") + "," + label + "\n")

outputFile.close()



check_File = pd.read_csv('test.csv')
outputFile = pd.read_csv('OutputSVM.csv')

#numberOfMismatch = 0

true_Labels = []
predicted_Labels = []
labels = ["AbusiveHC","NonAbusiveHC","AbusiveDT","NonAbusiveDT"]

for i in range(0,len(check_File)):
    true_Labels.append(check_File["Type"][i])
    predicted_Labels.append(outputFile["Type"][i])

#print("Mismatches = {}".format(numberOfMismatch))


from sklearn.metrics import classification_report
# getting a full report
print(classification_report(true_Labels, predicted_Labels, target_names=labels))
print("Done Classifying....")
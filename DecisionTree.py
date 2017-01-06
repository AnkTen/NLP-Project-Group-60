#Written by Shruti Thakur
#Decision Tree Classifier algorithm

import csv
import nltk

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

f = open('train.csv')
csv_f = csv.reader(f)

featureList = []
labelList = []

for row in csv_f:
    dictOfFeatures = {}
    tweet = nltk.word_tokenize(row[0])
    posTag = nltk.pos_tag(tweet)
    for i in range(0,len(posTag)):
        keyFeature = posTag[i][0]
        valFeature = posTag[i][1]
        dictOfFeatures[keyFeature] = valFeature
    featureList.append(dictOfFeatures)
    labelList.append(row[1])

    # With one feature
    """for i in range(0,len(posTag)):
        keyFeature = posTag[i][0]
        valFeature = keyFeature
        dictOfFeatures[keyFeature] = valFeature
    featureList.append(dictOfFeatures)
    labelList.append(row[1]) """

train = []
for i in range(0,len(featureList)):
    train.append((dict(featureList[i]),labelList[i]))

print(len(featureList))

try:
    decisiontree = nltk.DecisionTreeClassifier.train(train,entropy_cutoff=0.05,depth_cutoff=100,support_cutoff=10,binary=False,feature_values=None,verbose=False)
except Exception:
    print(Exception)
print("Training completed !!! ")

testFile = open('test.csv')
csv_testFile = csv.reader(testFile)

outputFile = open("OutputDecisionTree.csv",'w')
outputFile.write("Tweet,Type\n")

for row in csv_testFile:
    tweet = nltk.word_tokenize(row[0])
    tweetPOSTag = nltk.pos_tag(tweet)

    dictOfFeatures = {}
    for i in range(0, len(tweetPOSTag)):
        keyFeature = tweetPOSTag[i][0]
        valFeature = tweetPOSTag[i][1]
        dictOfFeatures[keyFeature] = valFeature
    label = decisiontree.classify(dictOfFeatures)
    outputFile.write(str(row[0]) + "," + str(label) + "\n")

    # with one feature
    """ for i in range(0, len(tweetPOSTag)):
        keyFeature = tweetPOSTag[i][0]
        valFeature = keyFeature
        dictOfFeatures[keyFeature] = valFeature
    label = decisiontree.classify(dictOfFeatures) """

outputFile.close()
print("Classifying Done !!! ")

checkFile = open("test.csv")
csv_checkFile = csv.reader(checkFile)

outputFile = open("OutputDecisionTree.csv")
csv_outputFile = csv.reader(outputFile)

trueLabels = []
predictedLabels = []
labels = ["AbusiveHC","NonAbusiveHC","AbusiveDT","NonAbusiveDT"]

for row in csv_checkFile:
   trueLabels.append(row[1])
for row in csv_outputFile:
   predictedLabels.append(row[1])

countAHC = 0
countNAHC = 0
countADT = 0
countNADT = 0

PcountAHC = 0
PcountNAHC = 0
PcountADT = 0
PcountNADT = 0

for i in range(0,len(trueLabels)):
    if predictedLabels[i] == "AbusiveHC":
        countAHC += 1
        if trueLabels[i] == "AbusiveHC":
            PcountAHC += 1
    elif predictedLabels[i] == "NonAbusiveHC":
        countNAHC += 1
        if trueLabels[i] == "NonAbusiveHC":
            PcountNAHC += 1
    elif predictedLabels[i] == "AbusiveDT":
        countADT += 1
        if trueLabels[i] == "AbusiveDT":
            PcountADT += 1
    elif predictedLabels[i] == "NonAbusiveDT":
        countNADT += 1
        if trueLabels[i] == "NonAbusiveDT":
            PcountNADT += 1

precisionADT = float(PcountADT/countADT)
precisionNADT = float(PcountNADT/countNADT)
precisionAHC = float(PcountAHC/countAHC)
precisionNAHC = float(PcountNAHC/countNAHC)

recallADT = float(PcountADT/100)
recallNADT = float(PcountNADT/100)
recallAHC = float(PcountAHC/100)
recallNAHC = float(PcountNAHC/100)

f1ADT = float((2*precisionADT*recallADT)/(precisionADT+recallADT))
f1NADT = float((2*precisionNADT*recallNADT)/(precisionNADT+recallNADT))
f1AHC = float((2*precisionAHC*recallAHC)/(precisionAHC+recallAHC))
f1NAHC = float((2*precisionNAHC*recallNAHC)/(precisionNAHC+recallNAHC))

print("Labels           Precision            Recall          F1-score")
print("AbusiveDT            "+str(precisionADT)+"           "+str(recallADT)+"          "+str(f1ADT))
print("NonAbusiveDT            "+str(precisionNADT)+"           "+str(recallNADT)+"          "+str(f1NADT))
print("AbusiveHC            "+str(precisionAHC)+"           "+str(recallAHC)+"          "+str(f1AHC))
print("NonAbusiveHC            "+str(precisionNAHC)+"           "+str(recallNAHC)+"          "+str(f1NAHC))

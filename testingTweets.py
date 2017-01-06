'''
Written by Shruti Thakur and Ankeet Tendulkar
'''

def containsNames(line, names):
    for word in names:
        if line.lower().find(word) != -1:
            return True
    return False

def testing():
    with open("inputData.txt", "r") as ins:
        array = []
        for line in ins:
            array.append(line.lower())

        #print(array)
    wordNonAbusiveHillary = ["#imwithher","#votehillary","#imwithher2016","#hillaryforpresident","#iamwithher","#wallstreetwhore","#dumptrump","#uniteblue","#hillaryforamerica","#hillarystrong"]
    wordAbusiveHillary = ["#clintoncorruption","#crookedhilary","#iamnotwithher","#imnotwithher","#neverhillary","#corrupthillary", "#lockherup", "#hillaryclintonforprison","#clintoncrimefamily","#hillaryisthedevil"]
    wordNonAbusiveDonald = ["#teamtrump","#trumpforpresident","#maga","#makeamericagreatagain","#trumppence16","#trumptrain","#votetrump","#trumppence"]
    wordAbusiveDonald = ["#votetrumpdestroyamerica","#gunsense","#nevertrump","#fucktrump","#draintheswamp","#ignoranttrump","#dumptrump","#burntrump","#trumpisaracist"]


    wordAbusiveHillaryDonald = ["#clintoncorruption","#crookedhilary","#iamnotwithher","#imnotwithher","#neverhillary","#corrupthillary", "#lockherup", "#hillaryclintonforprison","#clintoncrimefamily","#hillaryisthedevil","#votetrumpdestroyamerica","#gunsense","#nevertrump","#fucktrump","#draintheswamp","#ignoranttrump","#dumptrump","#burntrump","#trumpisaracist"]
    wordNonAbusiveHillaryDonald = ["#imwithher","#votehillary","#imwithher2016","#hillaryforpresident","#iamwithher","#wallstreetwhore","#dumptrump","#uniteblue","#hillaryforamerica","#hillarystrong","#teamtrump","#trumpforpresident","#maga","#makeamericagreatagain","#trumppence16","#trumptrain","#votetrump","#trumppence"]


    for eachLine in array:
        numOfNonAbusiveWords = len(set(eachLine.split()).intersection(set(wordNonAbusiveHillaryDonald)))
        numOfAbusiveWords = len(set(eachLine.split()).intersection(set(wordAbusiveHillaryDonald)))
        if(numOfNonAbusiveWords > numOfAbusiveWords):
            numOfNonAbusiveHillary = len(set(eachLine.split()).intersection(set(wordNonAbusiveHillary)))
            numOfNonAbusiveDonald = len(set(eachLine.split()).intersection(set(wordNonAbusiveDonald)))
            if(numOfNonAbusiveHillary > numOfNonAbusiveDonald):
                fopen = open('nonabusiveHC_1.txt', 'a', encoding='utf-8')
                fopen.write(eachLine)
                fopen.close()
            else:
                fopen = open('nonabusiveDT_1.txt', 'a', encoding='utf-8')
                fopen.write(eachLine)
                fopen.close()

        elif (numOfAbusiveWords > numOfNonAbusiveWords):
            numOfAbusiveHillary = len(set(eachLine.split()).intersection(set(wordAbusiveHillary)))
            numOfAbusiveDonald = len(set(eachLine.split()).intersection(set(wordAbusiveDonald)))
            if (numOfAbusiveHillary > numOfAbusiveDonald):
                fopen = open('abusiveHC_1.txt', 'a', encoding='utf-8')
                fopen.write(eachLine)
                fopen.close()
            else:
                fopen = open('abusiveDT_1.txt', 'a', encoding='utf-8')
                fopen.write(eachLine)
                fopen.close()
        else:

            fopen = open('leftover.txt', 'a', encoding='utf-8')
            fopen.write(eachLine)
            fopen.close()
#testing()
print("Done")

def leftOver():
    f1 = open('negative-words.txt', 'r')
    s1 = f1.readlines()
    negativeWords = []
    for eachWord in s1:
        negativeWords.append(eachWord.replace("\n",""))

    f2 = open('positive-words.txt', 'r')
    s2 = f2.readlines()
    positiveWords = []
    for eachWord in s2:
        positiveWords.append(eachWord.replace("\n",""))

    print(positiveWords)
    print(negativeWords)
    f3 = open('leftover.txt', 'r')
    s3 = f3.readlines()
    for eachline in s3:
        l = eachline.lower().split()
        #print(l)
        donaldNames = ["#donaldtrump", "#trump", "#realdonaldtrump", "@donaldtrump", "@trump", "@realdonaldtrump"]
        hillaryNames = ["#hillaryclinton", "@hillaryclinton"]

        if containsNames(eachline.lower(),hillaryNames) and not containsNames(eachline.lower(),donaldNames):
            numOfPositiveWords = len(set(l).intersection(set(positiveWords)))
            numOfNegativeWords = len(set(l).intersection(set(negativeWords)))
            #print(numOfPositiveWords)
            #print(numOfNegativeWords)
            if(numOfPositiveWords > numOfNegativeWords):
                fopen = open('NonAbusiveHC_2.txt', 'a', encoding='utf-8')
                fopen.write(eachline)
                fopen.close()
            elif(numOfNegativeWords > numOfPositiveWords):
                fopen = open('AbusiveHC_2.txt', 'a', encoding='utf-8')
                fopen.write(eachline)
                fopen.close()
        elif not containsNames(eachline.lower(),hillaryNames) and containsNames(eachline.lower(),donaldNames):
            numOfPositiveWords = len(set(l).intersection(set(positiveWords)))
            numOfNegativeWords = len(set(l).intersection(set(negativeWords)))
            if (numOfPositiveWords > numOfNegativeWords):
                fopen = open('NonAbusiveDT_2.txt', 'a', encoding='utf-8')
                fopen.write(eachline)
                fopen.close()
            elif (numOfNegativeWords > numOfPositiveWords):
                fopen = open('AbusiveDT_2.txt', 'a', encoding='utf-8')
                fopen.write(eachline)
                fopen.close()
        else:
            fopen = open('leftover_2.txt', 'a', encoding='utf-8')
            fopen.write(eachline)
            fopen.close()
testing()
print("Done 1")
leftOver()
print("Done 2")
print("Finally Done !!")
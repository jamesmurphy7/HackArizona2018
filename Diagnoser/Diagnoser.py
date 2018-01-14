import sys
import Library
import Diseas

def makeDiseasList():
    diseases = []


    for diseas in Library.Diseases.diseases:
        newDiseas = Diseas.diseas(diseas[0])
        for word in diseas[1:]:
            newDiseas.addSymptom(word.strip().lower())
        diseases.append(newDiseas)

    return diseases

def calcDiseas(diseas,symptoms):
    sympListNum = symptoms.__len__()
    diseasSympNum = diseas.symptoms.__len__()
    sympInDis = 0
    for symp in symptoms:
        if symp in diseas.symptoms:
            sympInDis = sympInDis + 1
    if sympInDis == 0:
        return None
    diseas.accuracy = float(sympInDis) / float(sympListNum)
    diseas.coverage = float(sympInDis) / float(diseasSympNum)
    return diseas

class diagnoser:
    def diagnose(symptoms):
        possibleDiseases = []
        chosenDiseas = Diseas.diseas("meme")
        diseases = makeDiseasList()
        for diseas in diseases:
            newdis = calcDiseas(diseas, symptoms)
            if newdis is not None:
                if newdis.accuracy >= chosenDiseas.accuracy:
                    if newdis.coverage > chosenDiseas.coverage:
                        chosenDiseas = newdis
        return chosenDiseas.name


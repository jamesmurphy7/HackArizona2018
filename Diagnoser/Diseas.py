import sys

class diseas:

    def __init__(self):
        self.coverage = 0
        self.accuracy = 0
        self.name = None
        self.symptoms = {}

    def __init__(self,n):

        self.coverage = 0
        self.accuracy = 0
        self.name = n
        self.symptoms = {}

    def addSymptom(self,symptomName):

        self.symptoms[symptomName] = symptomName


import re
import math

# Design neural network to determine if given sentence is in English. I need to figure out a way to
# allow different sized strings for input into the neural network.
# Possible outline
# (1) Create an indicator function which takes in a string and a letter and outputs a distribution of that letter
#     within the string.
# (2) Create a function which takes in two distributions and returns a vector which contains information about
#     average distance between occurrences of the letters...
# (3) Write a program that determines average number of occurrences of each letter, and every 2, 3, and 4 letter combo
#     as we input sentences and keeps track of standard deviations for each.
# (4) Train this on many sentences.
# (5) Determine a method of making predictions.  (Steps (4) and (5) seem like I should
#

alphabet = "abcdefghijklmnopqrstuvwxyz"

class Statistic:
    def __init__(self, chars):
        self.chars = chars
        self.avg   = 0
        self.variance = 0
        self.sd = 0
        self.num_sentences = 0
        self.num_occurrences_history = []
        self.sum = 0
        self.squared_sum = 0
        self.sentence = ''

    def computeAverage(self):
        self.avg = (self.avg*(self.num_sentences-1)+self.numberOfOccurences())/self.num_sentences
        return self.avg

    # Use Regex to find and return the number of occurrences of self.chars within sentence
    def numberOfOccurences(self):
        m = re.findall(self.chars, self.sentence)
        num_occurrences = len(m)
        return num_occurrences

    def computeVariance(self):
        self.sum += self.num_occurrences_history[-1]
        self.squared_sum += self.num_occurrences_history[-1]**2
        if self.num_sentences > 1:
            self.variance = (self.squared_sum - self.sum/self.num_sentences)/(self.num_sentences-1)
        return self.variance

    def computeStandardDeviation(self):
        self.sd = math.sqrt(self.variance)
        return self.sd

    def update(self, sentence):
        self.sentence = sentence
        self.num_sentences += 1
        self.num_occurrences_history.append(self.numberOfOccurences())
        self.avg = self.computeAverage()
        self.variance = self.computeVariance()
        self.sd = self.computeStandardDeviation()


x = Statistic('the')
x.update("The pen is mightier than the sword")

statistics = []

# Create array of Statistics objects with every combo of 1, 2, 3, and 4 characters. 475254 total objects
for letter1 in alphabet:
    statistics.append(Statistic(letter1))
    for letter2 in alphabet:
        statistics.append(Statistic(letter1 + letter2))
        for letter3 in alphabet:
            statistics.append(Statistic(letter1 + letter2 + letter3))
            for letter4 in alphabet:
                statistics.append(Statistic(letter1+letter2+letter3+letter4))

# Creates an array of length len(s) with a 1 if letter appears and a 0 otherwise
def indicator(s, letter):
    distribution = []
    for character in s:
        if character == letter:
            distribution.append(1)
        else:
            distribution.append(0)
    return distribution

# WIP
def letterDistanceInSentence(s, letter1, letter2):
    dist1 = indicator(s, letter1)
    dist2 = indicator(s, letter2)



for statistic in statistics:
    statistic.update("Sometimes I can feel my bones straining under the weight of all the lives I’m not living")


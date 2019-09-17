"""
    K-NN Model
"""

import math

k = 9

"""
    Finds the Edistance by taking square root of the summation of the square differences of given features x
    compared to given features yacross n iterations
"""
def eDistance(x, y, n):
    ED = 0
    for index in range(n):
        ED += math.pow(float(x[index]) - float(y[index]), 2)

    ED = math.sqrt(ED)
    return ED

"""
    Tally results from given votes and returns an array of arrays such that 
    [[n,v]sub1, ... [n,v]subi] where n = number of votes, v = the votes value and 
    i = the number of different vote values
"""
def tally(votes):
    scores = []
    for vote in votes:
        for score in scores:
            if vote[1][-1] == score[1]:
                score[0] += 1
            elif score == scores[-1]:
                scores.append([1, vote[1][-1]])
                break
        if scores == []:
            scores.append([1, vote[1][-1]])

    return scores

"""
    Main method of KNN that iterates through test samples comparing the euclidean distance from test feature to
    train feature. Then taking the K closest Neighbors, tallys the 'votes' of each neighbor to predict the value
    for the test data
"""
def evaluate (trainData, testData):
    for test in testData:
        KNN = []
        for train in trainData:
            ED = eDistance(test,train,len(test))
            if len(KNN) < k:
                KNN.append([ED, train])
            else:
                for index in range(len(KNN)):
                    if ED < KNN[index][0]:
                        KNN[index] = [ED, train]
                KNN.sort(reverse=True)
        KNN = tally(KNN)
        KNN.sort(reverse=True)
        test.append(KNN[-1][-1])

    return testData

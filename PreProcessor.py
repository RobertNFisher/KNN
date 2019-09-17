"""
Pre-Processor
"""

import csv
import random as rndm

class preProcessor:
    def __init__(self, filename):
        data = []
        self.test_data = []
        self.train_data = []

        # Opens CSV file and seperates rows
        with open(filename) as iData:
            file = csv.reader(iData, delimiter= ',')
            # Randomly assigns data to test and train data groups
            for row in file:
                data.append(row)
            if filename == "iris.data":
                self.irisLabel(data)
            elif filename == "student-mat.csv":
                data = self.studentLabel(data)
            rndm.shuffle(data)
            for i in range(0, len(data)):
                if i%4 == 0:
                    self.test_data.append(data[i])
                else:
                    self.train_data.append(data[i])

        self.cleanData(self.test_data)
        self.cleanData(self.train_data)


    # Call method for data
    def getData(self):
        return [self.test_data, self.train_data]

    # Remove empty data
    def cleanData(self, array):
        for i in range(0, len(array)-1):
            if len(array[i]) == 0:
                array.pop(i)
    # Organize data from iris set
    def irisLabel(self, data):
        for i in range(0, len(data)-1):
            if data[i][4] == "Iris-setosa":
                data[i][4] = 0
            elif data[i][4] == "Iris-versicolor":
                data[i][4] = 1
            elif data[i][4] == "Iris-virginica":
                data[i][4] = 2

    def studentLabel(self, data):
        keep = [4, 12, 13, 15, 24, 27, 29]
        target = 14
        newArray = []

        for i in range(len(data)-1):
            newArray.append([])

        # Keep chosen features
        for instance in range(0, len(data)-1):
            for i in range(0, len(data[instance])-1):
                for index in keep:
                    # Handle String Value
                    if i == 4 and index == i:
                        if data[instance][i] == "GT3":
                            newArray[instance].append(1)
                        elif data[instance][i] == "LE3":
                            newArray[instance].append(0)
                    # Handle String Value
                    elif i == 15 and index == i:
                        if data[instance][i] == "yes":
                            newArray[instance].append(1)
                        elif data[instance][i] == "no":
                            newArray[instance].append(0)
                    # Append info
                    elif i == index:
                        newArray[instance].append(data[instance][i])

            if data[instance][target] == '0' or data[instance][target] == "failures":
                newArray[instance].append(data[instance][target])
            elif float(data[instance][target]) > 0:
                newArray[instance].append(1)
        # Remove the labels
        print(newArray[0])
        newArray.pop(0)
        return newArray

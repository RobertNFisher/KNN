"""
    Name: Robert Fisher
    Date: 9/16/2019
    Class: Machine Learning
    Prof.: C. Hung
"""

"""
    Main Class
"""


import PreProcessor as pP
import KNN2

featureRemovalIndex = -1
irisData = pP.preProcessor("iris.data")
studentData = pP.preProcessor("student-mat.csv")
data = irisData.getData()
data = studentData.getData()
train_data = data[0]
test_data = data[1]
sample_data =[[]]

# Remove a given feature to adjust accuracy
if featureRemovalIndex >= 0:
    for i in range (0, len(test_data)):
        test_data[i].pop(featureRemovalIndex)

    for i in range (0, len(train_data)):
        train_data[i].pop(featureRemovalIndex)

# Collect sample_data to check for accuracy
for set in range(0,len(test_data)):
    for data in range(0, len(test_data[set])):
        value = test_data[set][data]
        sample_data[set].append(value)
    sample_data.append([])



# Removes label from test_data
for i in range(0,len(test_data)-1):
    if(len(test_data[i]) == 0):
        test_data.pop(i)
    try:
        test_data[i].pop(len(test_data[i])-1)
    except:
        print("ERROR removing label")

# For simple visualization of the data given
print("Sample Test Data: {}".format(test_data[0]))
print("Sample Train Data: {}".format(train_data[0]))

results = KNN2.evaluate(train_data, test_data)
print("Sample comparison: {} ?= {}".format(train_data[0][-1], sample_data[0][-1]))


# Calculates loss by counting the correct guesses to the actual values
correct = 0
for i in range(len(results)):
    given = results[i]
    actual = sample_data[i]
    if results[i] == sample_data[i]:
        correct += 1

accuracy = (correct/len(results))*100
print("Accuracy:{}".format(accuracy))



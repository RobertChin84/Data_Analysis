import sys
import csv
sys.path.append("../../stats_lib/")
import statistics as stat
sys.path.append("../../classification/")
import Naive_Bayes_Classifier as nbc

def load_data(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            data.append(row)
    return data
                
def load_test_data(filename):
    data = []
    with open(filename, 'rb') as csvfile:
        reader = csv.reader(csvfile)
        for row in reader:
            temp_row = ["unknown"]
            for var in row:
                temp_row.append(float(var))
            data.append(temp_row)
    return data            
def combine_data(dataIN,labels):
    data = []
    for i in range(len(dataIN)):
        row = []
        row.append(labels[i][0])
        for var in dataIN[i]:
            row.append(float(var))
        data.append(row)
    return data
            
def generate_temp_labels(N):
    row = []
    for i in range(0,N):
        row.append("var_{0}".format(i+1))
    return row
file_labels = "../data/scikit_learn_data/trainLabels.csv" 
file_data   = "../data/scikit_learn_data/train.csv"   
   
labels        = load_data(file_labels)
data          = load_data(file_data)
labels_for_classifer = ["classifer"]
labels_for_classifer.extend(generate_temp_labels(len(data[0])))
training_data = combine_data(data,labels)
prior_stats   = nbc.generate_prior_stats(training_data,labels_for_classifer)

test_file     = "../data/scikit_learn_data/test.csv"  
test_data     = load_test_data(test_file)
prediction_labels = []
i = 0
with open('scikit_test.csv', 'wb') as test_file:
    csv_writer = csv.writer(test_file)
    csv_writer.writerow(["Id","Solution"])
    for row in test_data:
        i+=1
        prediction = nbc.predict_data(row,prior_stats,labels_for_classifer)
        prediction_labels.append(prediction)
        csv_writer.writerow([i,prediction])




                    


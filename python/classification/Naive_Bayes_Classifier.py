import numpy as np
import sys
sys.path.append("/Users/rchin/MyDrive/stochastic_project/Data_Analysis/python/stats_lib")
import statistics as stat
#example data and algo taken from Wiki Naive Bayes Classifer
def generate_data():
    data =[['male',6,180,12],
           ['male',5.92,190,11],
           ['male',5.58,170,12],
           ['male',5.92,165,10],
           ['female',5,100,6],
           ['female',5.5,150,8],
           ['female',5.42,130,7],
           ['female',5.75,150,9]]
    labels = ["classifer","height","weight","foot size"]
    return data,labels

def generate_prior_stats(data,labels):
    #take the training data provided and convert to dictionary for computation
    #of prior stats of the mean and variance for training data set. 
    temp_data   = {}
    prior_stats = {}
    index_of_classifer = labels.index("classifer")
    for row in data:
        classifer = row[index_of_classifer]
        if classifer not in temp_data:
            temp_data[classifer] = {}
        for i in range(0,len(row)):
            if i!=index_of_classifer:
                if labels[i] not in temp_data[classifer]:
                    temp_data[classifer][labels[i]] = []
                temp_data[classifer][labels[i]].append(row[i])
    for classifer in temp_data:
        if classifer not in prior_stats:
            prior_stats[classifer] = {}
        for label in temp_data[classifer]:
            if label not in prior_stats[classifer]:
                prior_stats[classifer][label] = {}
            prior_stats[classifer][label]['mean']     = np.mean(temp_data[classifer][label])
            prior_stats[classifer][label]['variance'] = stat.sample_variance(temp_data[classifer][label])        
    return prior_stats
        
def predict_data(x,prior,labels):
    #Take the prior stats and compute the normal probabilities for the Bayes
    #probability
    probs = {}
    number_of_classes = len(prior.keys())
    inital_prob       = 1.0/float(number_of_classes)
    normalising_prob  = 0.0
    for classifer in prior:
        if classifer not in probs:
            probs[classifer] = 1.0
        for label in prior[classifer]:
            index_of_classifer = labels.index(label)
            prob               = stat.gaussian(x[index_of_classifer],prior[classifer][label]['mean'],prior[classifer][label]['variance'])
            probs[classifer]*=prob
        
        normalising_prob+=probs[classifer]*inital_prob
    max_prob = 0.0
    prediction = "Unknown"
    for classifer in probs:
        prob  = probs[classifer]/normalising_prob
        if prob > max_prob:
            max_prob   = prob
            prediction = classifer
           
    #print "Predicited class for:"
    #print x 
    #print "class: {0}".format(prediction)
    #print "Probability density value: {0}".format(max_prob)
    return prediction
       
#data,labels = generate_data()
#prior_stats = generate_prior_stats(data,labels)
#predict_data(['unknown',6,130,8],prior_stats,labels)
    
    
    
    
    

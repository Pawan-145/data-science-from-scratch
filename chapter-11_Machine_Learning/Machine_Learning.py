# Machine Learning


# Modeling

"""
 What is model? 
It's  simply a specification of a mathematical(or probabilistic) relationship that exists between different variables
"""

# What is Machine Learning?
''' We will use Machine Learning to refer to creating and using models that are learned from data 
In other contexts this might be called 'predictive modelling' or 'data mining'
'''

# Types of models
'''
1. Supervised models (in which there is a set of data labeled with the correct answers to learn from)
2. Unsupervised models (in which there is no such labels)

There are various other types:
(a) Semisupervised (in which only some of the data are labeled)
(b) Online (in which the model needs to continuously adjust to newly arriving data)
(c) Reinforcement(in which, after making making a series of predictions, the model gets a signal indicating how well it did)
'''

# Overfitting : A common danger in machine learning is overfitting
"""
In overfitting, it produces a model that performs well on the data you train it on but generalizes poorly to any new data.
This could involve learning noise in the data. Or it could involve learning to identify specify inputs rather than whatever factors 
are actually predictive for the desired output.
"""

# Underfitting
"""
In underfitting, it produces a model that doesn't perform well even on the training data, although typically when this happens you decide your model isn't good enough and keep looking for a better one 
"""

# Models that are too complex lead to overfitting and don't generalize well beyound that data they were trained on.
"""
The most fundamental approach involves using different data to train the model and to test the model.
The simplest way to do this is to split the dataset, so that (for example ) two-thirds of it is used to train the model, after which we 
measure the model's performance on the remaining third
"""

import random
from typing import TypeVar, List, Tuple
X = TypeVar('X')     # generic to represent a data point
def split_data(data:List[X],prob:float)-> Tuple[List[X],List[X]]:
    """ Split data into fractions [prob, 1-prob] """
    data = data[:]     # Shallow copy
    random.shuffle(data)        # Shuffle modifies the list
    cut = int(len(data)*prob)        # use prob to find a cutoff
    return data[:cut], data[cut:]

data  = [n for n in range(1000)]
train,test = split_data(data,0.75)

# The proportions should be correct
assert len(train) == 750
assert len(test) == 250

# and the original data should be preserved (in some order)
assert sorted(train+test) == data

"""
When you have paired data - inputs (x) and corresponding outputs (y). You must be careful that each (x) stays matched with its correct (y)
"""

Y = TypeVar('V')                   # generic type to represent output variable
def train_test_split(xs:List[X],
                     ys: List[Y],
                     test_pct: float) -> Tuple[List[X], List[X], List[Y], List[Y]]:
    # Generate the indices and split them
    idxs = [i for i in range(len(xs))]
    train_idxs, test_idxs = split_data(idxs, 1 - test_pct)
    return ([xs[i] for i in train_idxs],   # x_train
            [xs[i] for i in test_idxs],     # x_test
            [ys[i] for i in train_idxs],    # y_train
            [ys[i] for i in test_idxs])      # y_test


xs = [x for x in range(1000)]  
ys  = [2*x for x in xs]          # each y_i is twice x_i
x_train,x_test,y_train,y_test = train_test_split(xs,ys,0.25)

# Check that the proportions are correct
assert len(x_train) == len((y_train)) == 750
assert len(x_test) == len(y_test) == 250

# check that the corresponding data points are paired correctly 
assert all(y == 2*x for x,y in zip(x_train,y_train))
assert all(y == 2*x for x,y in zip(x_test,y_test))

# After which you can do something like:

model  = SomeKindOfModel()                # Assuming that there is a model 
x_train, x_test, y_train, y_test  = train_test_split(xs,ys,0.33)
model.train(x_train, y_train)
performance = model.test(x_test, y_test)


""" If there is a common pattern in the test and training data that wouldn't generalize to a larger dataset """
'''

Training set
User	Week	StudyHours	Score
A	    1	       2	      60
A	    3	       4	      65
B	    2	       2 	      58
C     	1	       5	      80
C	    3	       7	      85

Test set
User	Week	StudyHours	Score
A	     2	       3	   62
B	     1         1	   55
B	     3         3	   60
C	     2	       6	   82


In above split you can see same users which are in the Training set also present in Test set. In this case it will not work according to generalized formula rather it will start recognizing the users

Correct Split should be:

Training set
User	Week	StudyHours	Score
A	     1	       2	      60
A	     3	       4	      65
A	     2	       3	      62
B	     2	       2 	      58
B	     1         1	      55
B	     3         3	      60

Test set
User	Week	StudyHours	Score
C     	 1	       5	      80
C	     3	       7	      85
C	     2	       6	      82

Now, Training set have users (A) and (B) and Test set have user (c) which is totally different and new as compare to user (A) and (B) 
'''

# (Train-Validation-Test) Split
"""
Split the data into three parts: 
(1) A training set for building models
(2) A validation set for choosing among trained models
(3) A test set for judging the final model.
""" 


# tp = True Positive
# fp = False Positive
# fn = False Negative
# tn = True Negative 

# Accuracy: It is defined as the fraction of correct predictions
def accuracy(tp:int, fp:int, fn:int, tn:int)->float:
    correct = tp+tn
    total = tp+fp+fn+tn
    return correct/total

assert accuracy(70,4930,13930,981070) == 0.98114

# Precision: It measures how accurate our positive predictions were
def precision(tp:int,fp:int,fn:int,tn:int)->float:
    return tp/(tp+fp)

# Recall: It measures what fraction of positives our model identified
def recall(tp:int,fp:int,fn:int,tn:int)->float:
    return tp/(tp+fn)                             # fn-> model says negative but in real it's positive, so we have to include

assert recall(70,4930,13930,981070) == 0.005

# Precision and Recall combined into F1 score
def f1_score(tp:int,fp:int,fn:int,tn:int)-> float:
    p = precision(tp,fp,fn,tn)
    r = recall(tp,fp,fn,tn)
    return (2 * p * r) / (p + r)

''' This is the harmonic mean of precision and recall and necessarily lies between them '''


# The bias-variance Tradeoff
"""
It is a core machine learning concept describing the balance between a model's simplicity(low bias, high variance, underfitting) and complexity(high biasm low variance, overfitting), aiming to minimize the total predicition error (Mean Squared Error) on new data by finding the "sweet spot" where a model generalizes well without being overly sensitive to training data noise.
"""

# Features: are whatever inputs we provide to our model. It tells the model what to look at; the target tells is what to predict.
"""
Example: Healthcare / Medical
        features -> Age, Blood Pressure, Family history of disease, Cholesterol level, Number of risk factors
"""

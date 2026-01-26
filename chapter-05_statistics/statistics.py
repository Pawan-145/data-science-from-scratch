# Statistics

# Central Tendencies
## we will want some notion of where our data is centered

from typing import List
num_friends = [100,55,66,75,32,75,23]
daily_hours = [1.5, 2.0, 0.5, 3.0, 4.5, 2.5, 1.0, 2.2, 3.5, 0.8, 1.7, 2.8, 3.0, 1.2]
# Mean
def mean(xs: List[float])-> float:
    return sum(xs)/len(xs)
# If you have 10 data points, and you increase the value of any of them by 1, you increase the mean by 0.1

# Median (In median we have to sort the elements first)
def _median_odd(xs:List[float])->float:
    return sorted(xs)[len(xs)//2]                 # '//' -> it is floor division 
    
def _median_even(xs:List[float]) -> float:
    sorted_xs = sorted(xs)
    h_midpoint  = len(xs)//2
    return ((sorted_xs[h_midpoint-1]+sorted_xs[h_midpoint])/2)

def median(c:List[float]) -> float:
    return (_median_even(c) if len(c)%2==0 else _median_odd(c))

assert median([1,10,2,9,5]) == 5
assert median([1,9,2,10]) == (2+9)/2

# The generalization of median is the quantile, which represents the value under which a certain percentile of the data lies(the median represents the  data value under which 50% of the data lies)

def quantile(xs:List[float],p:float) -> float:
    p_index = int(p*len(xs))
    return sorted(xs)[p_index]

assert quantile(num_friends,0.10)
assert quantile(num_friends, 0.25)
assert quantile(num_friends, 0.75)
assert quantile(num_friends, 0.90)


# MODE
from collections import Counter
num_fri = [1,1,1,2,2,6,6,6]
def mode(x:List[float])->List[float]:
    '''Returns a list, since there might me more than one mode'''
    counts = Counter(x)
    max_count = max(counts.values())
    return [x_i for x_i,count in counts.items()
            if count == max_count]

assert set(mode(num_fri)) == {1,6}


# DISPERSION
## Range
# The range is zero is precisely when the max and min are equal, which can only happen if the elements of x are all the same, which means the data is as undispersed as possible. 
def data_range(xs:List[float])-> float:
    return(max(xs)-min(xs))

assert data_range(num_friends) == 77

# More complex  measure of dispersion is the variance
# VARIANCE

def de_mean(xs:List[float]) -> List[float]:
    x_bar = mean(xs)
    return[x-x_bar for x in xs]

def sum_of_squares(xs:List[float])-> float:
    return sum(x_i*x_i for x_i in xs)

def variance(xs:List[float])->float:
    assert len(xs) >= 2 , "variance requires at least two elements"

    n = len(xs)
    deviations = de_mean(xs)
    return(sum_of_squares(deviations)/(n-1))
    
assert 709.9 < variance(num_friends) < 710.1

# Standard deviation
import math
def standard_deviation(xs:List[float])-> float:
    ''' The standard deviation is the square root of the variance '''
    return math.sqrt(variance(xs))

assert  26.6 < standard_deviation(num_friends) < 26.7

#  The difference between the 75th percentile value and the 25th percentile value:

def interquartile_range(xs:List[float]) -> float:
    ''' Return the difference between the 75%-ile and the 25%-ile '''
    return quantile(xs,0.75) - quantile(xs,0.25)           # for quantile we sort the list

assert interquartile_range(num_friends) == 43

# Correlation 
 ## Covariance( for covariance both variables should)
daily_minutes = [1, 2, 3, 4, 5, 6, 7]
def dot(xs:List[float],ys:List[float]):
    return sum(x_i*y_i for x_i,y_i in zip(xs,ys))

def covariance(xs:List[float],ys:List[float])-> float:
    assert len(xs) == len(ys), "xs and ys must have same number of elements"
    n = len(xs)
    return dot(de_mean(xs), de_mean(ys)) / (n-1)

assert 22.42 < covariance(num_friends,daily_minutes) < 22.43
assert 22.42/60 < covariance(num_friends, daily_hours) < 22.43/60

# Correlation
def correlation(xs:List[float], ys:List[float])->float:
    ''' Measures how much xs and ys vary in tandem about their means '''
    stdev_x = standard_deviation(xs)
    stdev_y = standard_deviation(ys)
    if stdev_x>0 and stdev_y>0:
        return covariance(xs,ys) / stdev_x / stdev_y
    else:
        return 0                     # if no variation, correlation is zero 
    
# correlation is unitless and always lies between -1(perfect anticorrelation) and 1(perfect correaltion)

# If you find any outliers in given data, get it's index and remove it from all 
outlier = num_friends.index(100)

num_friends_good = [x
                    for out, x in enumerate(num_friends)
                    if out != outlier]
daily_minutes_good = [x
                      for out, x in enumerate(daily_minutes)
                      if out != outlier]
daily_hours_good = [dm/60 for dm in daily_minutes_good]


## Confounding variable :- It is an external factor in a study that influences both independent variable(what's being tested) and the dependent variable(the outcome)

# Simpson's Paradox
""" Simpson’s Paradox is when a trend that appears in several separate groups of data reverses or disappears when the groups are combined.
So the overall result tells the opposite story of each individual group — which is very confusing and dangerous if you don’t look deeper."""




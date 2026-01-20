# Hypothesis

from typing import Tuple
import math

def normal_approximation_to_binomial(n:int, p:float) -> Tuple[float, float]:
    """ Returns mu and sigma corresponding to a Binomial(n, p) """
    mu = p * n
    sigma = math.sqrt(p*(1-p)*n)
    return mu, sigma

def normal_cdf(x:float, mu:float = 0, sigma:float = 1)-> float:
    return(1+math.erf((x-mu)/math.sqrt(2)/sigma))/2

# The normal cdf _is_ the probability the variable is below a threshold
normal_probability_below = normal_cdf

# It's above the threshold if it's not below the threshold
def normal_probability_above(lo:float,
                             mu:float = 0,
                             sigma:float = 1)-> float:
    """ The probability that an N(mu, sigma) is greator than lo """
    return 1-normal_cdf(lo,mu,sigma)
# It's between if it's less than hi, but not less than lo
def normal_probability_between(lo: float,
                               hi: float,
                               mu: float = 0,
                               sigma:float = 1)-> float:
    ''' The probability that an N(mu, sigma) is between lo and hi '''
    return normal_cdf(hi, mu, sigma) - normal_cdf(lo,mu,sigma)

# It's outside if it's not between
def normal_probability_outside(lo:float,
                               hi:float,
                               mu:float,
                               sigma: float = 1)->float:
    """ The probability that an N(mu, sigma) is not between lo and hi """
    return 1 - normal_probability_between(lo,hi,mu,sigma)



""" We can do reverse also
for example, if we want to find na interval centered at the mean and containing 60% probability, then we find the cutoffs where the upper and lower tails each contain 20% of the probability (leaving 60%) """

# Sometimes we'll need to invert normal_cdf to find the value corresponding to a specified probability. There's no simple way to compute its inverse, but normal_cdf is continuous and strictly increasing, so we can use a binary search:

def inverse_normal_cdf(p:float,
                       mu:float = 0,
                       sigma:float =1,
                       tolerance:float = 0.00001)->float:
    """ Find approximate inverse using binary search """
    # if not standard, compute standard and rescale
    if mu!=0 or sigma != 1:
        return mu+ sigma*inverse_normal_cdf(p, tolerance=tolerance)
    low_z=-10.0                   # normal_cdf(-10) is (very close to) 0
    hi_z = 10.0                   # normal_cdf(10) is (very close to) 1
    while hi_z - low_z > tolerance:
        mid_z = (low_z+hi_z)/2                # consider the midpoint
        mid_p = normal_cdf(mid_z)             # the CDF's value there
        if mid_p < p:
            low_z = mid_z                     # midpoint too low search above it
        else:
            hi_z = mid_z                      # midpoint too high, search below it
    return mid_z

def normal_upper_bound(probability:float, mu:float = 0,
                       sigma:float = 1)->float:
    """ Returns the Z for which P(Z <= z) = probability """
    return inverse_normal_cdf(probability,mu,sigma)

def normal_lower_bound(probability:float,
                       mu:float = 0,
                       sigma:float = 1)-> float:
    """ Returns the z for which P(Z >= z) = probability """
    return inverse_normal_cdf(1-probability,mu,sigma)

def normal_two_sided_bounds(probability:float,
                            mu:float=0,
                            sigma:float = 1) -> Tuple[float,float]:
    """ Return the symmetric(about the mean) bounds that contain the specified probability """
    tail_probability = (1-probability)/2

    upper_bound = normal_lower_bound(tail_probability,mu,sigma)

    lower_bound = normal_upper_bound(tail_probability, mu, sigma)

    return lower_bound, upper_bound

mu_0, sigma_0 = normal_approximation_to_binomial(1000,0.5)

lower_bound, upper_bound  = normal_two_sided_bounds(0.95, mu_0, sigma_0)

""" We can calculate the power of the test  """
# 95% bounds based on assumption p is 0.5
lo,hi = normal_two_sided_bounds(0.95, mu_0, sigma_0)

# actual mu and sigma based on p = 0.55
mu_1, sigma_1 = normal_approximation_to_binomial(1000,0.55)

# A type 2 error means we fail to reject the null hypothesis, which will happen when X is still in our original interval
type2_probability  = normal_probability_between(lo,hi,mu_1,sigma_1)
power  = 1-type2_probability

hi = normal_upper_bound(0.95, mu_0, sigma_0)

type_2_probability = normal_probability_below(hi, mu_1, sigma_1)
power = 1 - type2_probability


# p-Values

def two_sided_p_value(x:float, mu:float = 0, sigma:float = 1)-> float:
    """ How likely are we to see a value at least as extreme as x(in either direction) if our values are from an N(mu,sigma)? """

    if x >= mu:
        # x is greater than the mean, so the tail is everything greater than x
        return 2*normal_probability_above(x, mu, sigma)
    else:
        # x is less than the mean, so the tail is everything less than x
        return 2 *normal_probability_below(x, mu, sigma)
    
''' If we were to see 530 heads '''
two_sided_p_value(529.5, mu_0, sigma_0)

# One way to convince yourself that this is a sensible estimate is with a simulation:

import random

extreme_value_count = 0
for _ in range(1000):
    num_heads = sum(1 if random.random() < 0.5 else 0
                    for _ in range(1000))
    if num_heads >= 530 or num_heads <= 470:
        extreme_value_count +=1

# p-value was 0.062 => ~62 extreme values out of 1000
assert 59 < extreme_value_count < 65, f"{extreme_value_count}"

""" Since the p-value is greater than 5% significance, we don't reject the null """
# If we instead saw 532 heads

two_sided_p_value(531.5,mu_0, sigma_0) 
""" Which is smaller than 5% significance, which means we would reject the null """

upper_p_value = normal_probability_above
lower_p_value = normal_probability_below

# For our one_sided test, if we saw 525 heads and not reject the null
upper_p_value(524.5,mu_0,sigma_0)

# If we saw 527 heads and reject the null
upper_p_value(526.5,mu_0,sigma_0) 

# Conifence Intervals
p = 0.5
math.sqrt(p*(1-p)/1000)

# Here we don't know p, so instead we use our estimate
p_hat = 525/1000
mu = p_hat
sigma = math.sqrt(p_hat*(1-p_hat)/1000)

# With 95% confidence that interval contains the true parameter p 
normal_two_sided_bounds(0.95, mu, sigma)


# p-Hacking
""" A procedure that erroneously rejects the null hypothesis only 5% of the time will - by -definition-5% of the time erronrously reject the null hypothesis  """

from typing import List
def run_experiment()->List[bool]:
    """ Flips a fair coin 1000 times, True = Heads, False = Tails """
    return[random.random() < 0.5 for _ in range(1000)]

def reject_fairness(experiment: List[bool]) -> bool:
    """ Using 5% significance levels  """
    num_heads = len([flip for flip in experiment if flip])
    return num_heads < 469 or num_heads>531

random.seed(0)
experiments = [run_experiment() for _ in range(1000)]
num_rejections =len([experiment
                     for experiment in experiments
                     if reject_fairness(experiment)])

assert num_rejections == 46

# Example: Running an A/B Test
""" If 990 out of 1000 A-viewers click their ad, while only 10 out of 1,000 B-viewers click their ad. You can be pretty confident that A is the better ad.

Let's say that Na people see ad A and na of them click it. we can think each ad view as a Bernoulli trial where (pa) is the probability that someone clicks ad A. Then (if Na is large which is here) we know that (na/Na) is approximately  a normal random variable with mean (pa) and standard deviation sigmaA = sqrt(pa*(1-pa)/Na)

similarly, (na/Nb) is approximately normal random variable with mean (pb) and standard deviation sigmaB = sqrt(pb*(1-pb)/Nb)  """

def estimated_parameters(N:int, n:int)-> Tuple[float,float]:
    p = n/N
    sigma = math.sqrt(p*(1-p)/N)
    return p, sigma

# If we assume those two normals are independent(which seems reasonable, since the individual Bernoulli trials ought to be), then their difference should also be normal with mean (pb-pa) and standard deviation sqrt(sigmaA**2 + sigmaB**2)

""" This means we can test the null hypothesis that pa and pb are same (that is, that pa - pb = 0) by using statistics """

def a_b_test_statistic(N_A:int, n_A:int, N_B:int, n_B: int) -> float:
    p_A, sigma_A = estimated_parameters(N_A, n_A)
    p_B, sigma_B = estimated_parameters(N_B, n_B)
    return (p_B - p_A)/math.sqrt(sigma_A**2 + sigma_B**2)

""" For example, if " tastes great " gets 200 clicks out of 1,000 views and "less bias" get 180 clicks out of 1,000 views """

z = a_b_test_statistic(1000,200,1000,180)

# The probability of seeing such a large difference if the means were actually equal would be :
two_sided_p_value(z)
 
""" Which is large enough that we can't conclude there's much of a difference.
on the other hand, if "less bias" only got 150 clicks """

z = a_b_test_statistic(1000,200,1000,150)
two_sided_p_value(z)    # 0.003

""" Which means there's only a 0.003 probability we'd see such a large difference if the ads were equally  effective """


# Bayesian Inference = means updating your belief using data

""" 
posterior directly proportional to (likelihood * prior) 
or
New Belief = Old belief x how well it explains data
"""

def B(alpha:float, beta:float)-> float:
    """ A normalizing constant so that the total probability is 1 """
    return math.gamma(alpha) * math.gamma(beta) / math.gamma(alpha+beta)

def beta_pdf(x:float, alpha:float, beta:float) -> float:
    if x <= 0 or x >= 1:
        return 0 
    return x ** (alpha-1)*(1-x)**(beta-1)/ B(alpha,beta)  

  # x ** (alpha-1)*(1-x)**(beta-1)/ B(alpha,beta) = This is the probability density function (PDF) of the Beta distribution.

""" Generally speaking, this distribution centers its weight at:
alpha / (alpha + beta)
and the larger alpha and beta are, the "tighter" the distribution is  """

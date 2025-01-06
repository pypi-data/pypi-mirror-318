"""
Module for manipulating finite discrete probability distributions with integer outcomes (like dice rolls)

Distributions are represented by frozendict objects of the form frozendict({outcome:probability})

Designed for a case where common results are re-used many times, so caches results
"""

import functools
from frozendict import frozendict

@functools.cache
def basic_die_dist(num_sides):
    """Returns the probability distribution for a num_sides sided-die"""
    return frozendict({i:1/num_sides for i in range(1,num_sides+1)})

@functools.cache
def min_dist(dist):
    """Returns the minimum result of a distribution"""
    return min(list(dist))

@functools.cache
def max_dist(dist):
    """Returns the maximum result of a distribution"""
    return max(list(dist))

@functools.cache
def prob_get(dist,outcome):
    """Gets the probability of outcome in distribution dist, returning zero if the outcome is not possible"""
    return dist.get(outcome,0)

@functools.cache
def add_dists(dist1,dist2):
    """Gives the distribution for the sum of a draw from dist1 and a draw from dist2"""
    return frozendict({i: sum([prob_get(dist1,j)*prob_get(dist2,i-j) for j in range(min_dist(dist1),i-min_dist(dist2)+1)]) for i in range(min_dist(dist1)+min_dist(dist2),max_dist(dist1)+max_dist(dist2)+1)})

@functools.cache
def multiple_dist(n_copies,dist):
    """Gives the distribution for the sum of n_copies draws from dist"""
    if(n_copies==1):
        return dist
    return add_dists(multiple_dist(n_copies-1,dist),dist)

@functools.cache
def add_const_to_dist(dist,bonus):
    """Gives the distribution for draws from dist plus a constant bonus"""
    return frozendict({list(dist)[i]+bonus: dist[list(dist)[i]] for i in range(len(list(dist)))})

@functools.cache
def mult_dist_by_const(dist,mult):
    """Gives the distribution of a value drawn from dist multiplied by mult
       Rounds down to get integers as required by D&D 3.5 and AD&D applications"""
    return frozendict({ i: sum(prob_get(dist,j) for j in range(int(i//mult),int((i+1)//mult))) for i in range(int(min_dist(dist)*mult//1),int(max_dist(dist)*mult//1)+1) })

@functools.cache
def prob_at_least(dist,outcome):
    """Gives the probability that a draw from dist is at least equal to outcome"""
    return sum([prob_get(dist,i) for i in range(outcome,max_dist(dist)+1)])

@functools.cache
def prob_at_most(dist,outcome):
    """Gives the probability that a draw from dist is at most equal to outcome"""
    return sum([prob_get(dist,i) for i in range(min_dist(dist),outcome+1)])

@functools.cache
def prob_between(dist,low,high):
    """Gives the probability that a draw from dist is between low and high, inclusive"""
    return sum([prob_get(dist,i) for i in range(low,high+1)])

@functools.cache
def min_one(dist):
    """Returns dist, changed so that any outcomes below one are set to one."""
    return frozendict({list(dist)[i]: dist[list(dist)[i]] if list(dist)[i]>1 else 0 for i in range(len(list(dist))) }) | frozendict({1: sum(dist[list(dist)[i]] if list(dist)[i]<=1 else 0 for i in range(len(list(dist)))) } )
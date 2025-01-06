"""
Module for calculating the chance to one-shot monsters in D&D 3.5.
"""

import pandas as pd
import functools
from frozendict import frozendict
from one_shot_calculator.discrete_dists import *
from one_shot_calculator import __version__

pd.options.plotting.backend = "plotly"

@functools.cache
def attack_dist(attack_bonus,armor_class,damage_dist,crit_range=(20,20),crit_mult=2,confirm_bonus=0,crit_effect=frozendict({0:1})):
    """Returns the probability distribution for damage dealt by attacks with attack_bonus against
       armor_class which if they hit deal damage_dist damage.
       
       Optional arguments:
       crit_range is a two-element tuple
       crit_mult is the critical multiplier. In D&D 3.5 one rolls an attack's original damage multiple times on a crit.
       confirm_bonus is any bonus to confirm critical hits. Confirming crits is an oft-forgotten rule.
       crit_effect is any bonus damage on a critical hit, such as a flaming burst weapon"""
    hit_chance=prob_between(basic_die_dist(20),min(max(2,armor_class-attack_bonus),20),20)
    confirm_chance=prob_between(basic_die_dist(20),min(max(2,armor_class-attack_bonus-confirm_bonus),20),20)
    crit_chance=prob_between(basic_die_dist(20),min(max(crit_range[0],armor_class-attack_bonus),20),20)*confirm_chance
    zerodist=frozendict({0: prob_between(basic_die_dist(20),1,min(max(1,armor_class-attack_bonus-1),20))})
    nonzerodist=frozendict({i: (hit_chance-crit_chance)*prob_get(min_one(damage_dist),i)+crit_chance*prob_get(min_one(add_dists(multiple_dist(crit_mult,damage_dist),crit_effect)),i) for i in range(min_dist(min_one(damage_dist)),max_dist(min_one(add_dists(multiple_dist(crit_mult,damage_dist),crit_effect)))+1)})
    return nonzerodist | zerodist

@functools.cache
def save_chance(save_bonus,difficulty_class):
    """Returns the chance to save with save_bonus against difficulty_class"""
    return prob_at_least(basic_die_dist(20),max(2,min(difficulty_class-save_bonus,20)))

@functools.cache
def save_for_half_dist(save_bonus,difficulty_class,damage_dist):
    """Returns the probability distribution for damage if one takes half damage on a successful save.
       Rolls with save_bonus against difficulty_class, on a failed save takes damage_dist"""
    return frozendict({i: save_chance(save_bonus,difficulty_class)*prob_get(min_one(mult_dist_by_const(min_one(damage_dist),0.5)),i)+(1-save_chance(save_bonus,difficulty_class))*prob_get(min_one(damage_dist),i) for i in range(max(1,int(0.5*min_dist(damage_dist)//1)),max_dist(damage_dist)+1)})

def attack_one_shot_function(attack_bonus,damage_dist,crit_range=(20,20),crit_mult=2,confirm_bonus=0,crit_effect=frozendict({0:1})):
    """Returns a one-shot-function for an attack suitable for entering into one_shot_histogram
       
       Required arguments:
       attack_bonus, the attack bonus of the attacker
       damage_dist, a damage distribution for the attack
       
       Optional arguments:
       crit_range is a two-element tuple
       crit_mult is the critical multiplier. In D&D 3.5 one rolls an attack's original damage multiple times on a crit.
       confirm_bonus is any bonus to confirm critical hits. Confirming crits is an oft-forgotten rule.
       crit_effect is any bonus damage on a critical hit, such as a flaming burst weapon"""

    
    def one_shot_function(row):
        return prob_at_least(attack_dist(attack_bonus,row["AC"],damage_dist,crit_range,crit_mult,confirm_bonus,crit_effect),row["hp"])
        
    return one_shot_function

def multi_attack_one_shot_function(attack_bonus_list,damage_dist_list,crit_range_list=None,crit_mult_list=None,confirm_bonus_list=None,crit_effect_list=None):
    """Returns a one-shot-function for multiple attacks suitable for entering into one_shot_histogram
       
       Required arguments:
       attack_bonus_list, a list of the attack bonuses for the attacks
       damage_dist_list, a list of damage distributions for the attacks
       
       Optional arguments:
       crit_range_list is a list of two-element tuples
       crit_mult_list is a list of critical multipliers
       confirm_bonus_list is a list of any bonuses to confirm critical hits
       crit_effect_list is a list of bonus damage on a critical hit, such as a flaming burst weapon"""   
     
    if len(attack_bonus_list) != len(damage_dist_list):
        raise ValueError("Lists do not have the same length!")

    if crit_range_list is None:
        crit_range_list=[(20,20)]*len(damage_dist_list)

    if len(damage_dist_list) != len(crit_range_list):
        raise ValueError("Damage dists and crit range list do not have the same length!")
    
    if crit_mult_list is None:
        crit_mult_list=[2]*len(damage_dist_list)

    if len(damage_dist_list) != len(crit_mult_list):
        raise ValueError("Damage dists and crit mult list do not have the same length!")
    
    if confirm_bonus_list is None:
        confirm_bonus_list=[0]*len(damage_dist_list)

    if len(damage_dist_list) != len(confirm_bonus_list):
        raise ValueError("Damage dists and confirm bonus list do not have the same length!")
    
    if crit_effect_list is None:
        crit_effect_list=[frozendict({0:1})]*len(damage_dist_list)

    if len(damage_dist_list) != len(crit_effect_list):
        raise ValueError("Damage dists and crit effect list do not have the same length!")
    
    def one_shot_function(row):
        return prob_at_least(functools.reduce(add_dists,[attack_dist(attack_bonus_list[i],row["AC"],damage_dist_list[i],crit_range_list[i],crit_mult_list[i],confirm_bonus_list[i],crit_effect_list[i]) for i in range(len(damage_dist_list))]),row["hp"])
 
    return one_shot_function

def spell_save_one_shot_function(save_type,difficulty_class):
    """Returns a one-shot-function for a spell granting a save suitable for entering into one_shot_histogram
       Currently does not take into account spell resistance
       
       Required arguments:
       save_type, the type of saving throw, one of:
         'Fort', 
         'Ref', 
         'Will'
        difficulty_class, the difficulty class for the save"""
    
    def one_shot_function(row):
        if row[save_type]=='-':
            return frozendict({1:1})
        else:
            return 1-save_chance(row[save_type],difficulty_class)
        
    return one_shot_function

def spell_save_for_half_one_shot_function(save_type,difficulty_class,damage_dist):
    """Returns a one-shot-function for something granting a save for half damage suitable for entering into one_shot_histogram
       Currently does not take into account spell resistance
       
       Required arguments:
       save_type, the type of saving throw, one of:
         'Fort', 
         'Ref', 
         'Will'
        difficulty_class, the difficulty class for the save
        damage_dist, the distribution of possible damage on a failed save"""
    
    def one_shot_function(row):
        if row[save_type]=='-':
            return prob_at_least(damage_dist,row['hp'])
        else:
            return prob_at_least(save_for_half_dist(row[save_type],difficulty_class,damage_dist),row["hp"])
        
    return one_shot_function


def one_shot_histogram(dataframe,low_CR,high_CR,one_shot_function,title=None):
    """Returns a histogram of the chance that an attack one-shots monsters in a given CR range.

       dataframe should be the result of a process_csv command
       low_CR is the lowest CR included, high_CR is the highest
       one_shot_function is a function that acts on the dataframe and gives a chance of one-shotting a monster
       """
    fig=dataframe.loc[(dataframe["CR"]>=low_CR) & (dataframe["CR"]<=high_CR)].apply(one_shot_function,axis=1).round(3).hist(bins=list(map(lambda x: x/20,range(21))),labels={ "value": "one-shot chance" }, hover_data={"variable" : False},title=title)
    fig.layout.update(showlegend=False,yaxis_title="number of monsters")
    fig.update_layout(title_subtitle={'text':"Created with one-shot-calculator v."+__version__,'font':{'color':'gray','size':13}})
    fig.update_xaxes(range=[0.0, 1.0])
    fig.update_traces(xbins={'start':0.0, 'end':1.0, 'size':0.05})

    return fig
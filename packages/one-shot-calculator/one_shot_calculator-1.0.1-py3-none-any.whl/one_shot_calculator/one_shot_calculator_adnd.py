"""
Module for calculating the chance to one-shot monsters in D&D 3.5.
"""

import pandas as pd
import functools
from frozendict import frozendict
from one_shot_calculator.discrete_dists import *
from one_shot_calculator import __version__

pd.options.plotting.backend = "plotly"

def monster_lookup(dataframe,monster_name):
    """Given a monster dataframe and a monster name, prints the full names of all monsters whose names contain that name"""
    print("Possible Matches:")
    for name in dataframe[functools.reduce(lambda x,y: x & y,[dataframe["Name"].str.contains(word) for word in monster_name.split()])]["Name"].unique():
        print(name)

def one_monster_table(dataframe,monster_full_name):
    """Given a monster dataframe and a monster full name, returns the rows in the dataframe corresponding to that monster.
       If not sure of the full name, check with monster_lookup first."""
    return dataframe[dataframe["Name"]==monster_full_name]

@functools.cache
def attack_dist(thac0,armor_class,damage_dist,attack_bonus=0):
    """Returns the probability distribution for damage dealt by attacks with thac0 against
       armor_class which if they hit deal damage_dist damage.
       
       Optional arguments:
       attack_bonus is a bonus added to attacks, such as from a magic weapon or high Str or Dex"""
    hit_chance=prob_between(basic_die_dist(20),min(max(2,thac0-armor_class-attack_bonus),20),20)
    zerodist=frozendict({0: 1-hit_chance})
    nonzerodist=frozendict({i: hit_chance*prob_get(min_one(damage_dist),i) for i in range(min_dist(min_one(damage_dist)),max_dist(min_one(damage_dist))+1)})
    return nonzerodist | zerodist

def attack_one_shot_function(thac0,medium_damage_dist,large_damage_dist,attack_bonus=0):
    """Returns a one-shot-function for an attack suitable for entering into one_shot_histogram
       
       Required arguments:
       thac0, the THAC0 of the attacker
       medium_damage_dist, a damage distribution for medium or smaller foes
       large_damage_dist, a damage distribution for large or larger foes
       
       Optional arguments:
       attack_bonus is a bonus added to attacks, such as from a magic weapon or high Str or Dex"""
    
    def one_shot_function(row):
        if row["larger_than_man"]:
            return prob_at_least(attack_dist(thac0,row["AC"],large_damage_dist,attack_bonus),row["hp"])
        else:
            return prob_at_least(attack_dist(thac0,row["AC"],medium_damage_dist,attack_bonus),row["hp"])
        
    return one_shot_function

def multi_attack_one_shot_function(thac0,medium_damage_dist_list,large_damage_dist_list,attack_bonus_list=None):
    """Returns a one-shot-function for multiple attacks suitable for entering into one_shot_histogram
       
       Required arguments:
       thac0, the THAC0 of the attacker
       medium_damage_dist_list, a list of damage distributions for medium or smaller foes
       large_damage_dist_list, a list of damage distributions for large or larger foes
       
       Optional arguments:
       attack_bonus_list is a list of bonuses added to attacks, such as from a magic weapon or high Str or Dex"""
    
    if len(medium_damage_dist_list) != len(large_damage_dist_list):
        raise ValueError("Damage dists do not have the same length!")

    if attack_bonus_list is None:
        attack_bonus_list=[0]*len(medium_damage_dist_list)

    if len(medium_damage_dist_list) != len(attack_bonus_list):
        raise ValueError("Damage dists and attack bonus list do not have the same length!")
    
    def one_shot_function(row):
        if row["larger_than_man"]:
            return prob_at_least(functools.reduce(add_dists,[attack_dist(thac0,row["AC"],large_damage_dist_list[i],attack_bonus_list[i]) for i in range(len(large_damage_dist_list))]),row["hp"])
        else:
            return prob_at_least(functools.reduce(add_dists,[attack_dist(thac0,row["AC"],medium_damage_dist_list[i],attack_bonus_list[i]) for i in range(len(large_damage_dist_list))]),row["hp"])
        
    return one_shot_function

@functools.cache
def save_chance(save_number,save_modifier=0,autofail_num=1):
    """Returns the chance to save for a monster with save_number for that save
    
        Optional arguments:
        save_modifier is a modifier to saves. For example, it would be -1 for the target of a specialist wizard in their specialty
        autofail_num is the number saves automatically fail on, which can be different with certain optional rules"""
    return prob_at_least(basic_die_dist(20),max(autofail_num+1,save_number-save_modifier))

@functools.cache
def save_for_half_dist(save_number,damage_dist,save_modifier=0,autofail_num=1):
    """Returns the probability distribution for damage if one takes half damage on a successful save.
       Rolls trying to hit save_number, on a failed save takes damage_dist
       
       Optional arguments:
       save_modifier is a modifier to saves. For example, it would be -1 for the target of a specialist wizard in their specialty
       autofail_num is the number saves automatically fail on, which can be different with certain optional rules"""
    return frozendict({i: save_chance(save_number,save_modifier,autofail_num)*prob_get(min_one(mult_dist_by_const(min_one(damage_dist),0.5)),i)+(1-save_chance(save_number,save_modifier,autofail_num))*prob_get(min_one(damage_dist),i) for i in range(max(1,int(0.5*min_dist(damage_dist)//1)),max_dist(damage_dist)+1)})

@functools.cache
def resist_chance(mr,mr_modifier=0):
    """Returns the chance to resist for a monster with magic resistance mr
    
        Optional arguments:
        mr_modifier is a modifier to magic resistance"""
    return prob_at_most(basic_die_dist(100),mr+mr_modifier)

@functools.cache
def spell_success_chance(save_number,save_modifier=0,autofail_num=1,mr=0,mr_modifier=0):
    """Returns the chance that a spell succeeds against a monster with save_number relevant save
    
        Optional arguments:
        save_modifier is a modifier to saves. For example, it would be -1 for the target of a specialist wizard in their specialty
        autofail_num is the number saves automatically fail on, which can be different with certain optional rules
        mr is the monster's magic resistance
        mr_modifier is a modifier to magic resistance"""
    return (1-resist_chance(mr,mr_modifier))*(1-save_chance(save_number,save_modifier,autofail_num))

@functools.cache
def spell_save_for_half_dist(save_number,damage_dist,save_modifier=0,autofail_num=1,mr=0,mr_modifier=0):
    """Returns the probability distribution for damage if one takes half damage on a successful save from a spell.
        Rolls trying to hit save_number, on a failed save takes damage_dist
       
        Optional arguments:
        save_modifier is a modifier to saves. For example, it would be -1 for the target of a specialist wizard in their specialty
        autofail_num is the number saves automatically fail on, which can be different with certain optional rules
        mr is the monster's magic resistance
        mr_modifier is a modifier to magic resistance"""
    zerodist=frozendict({0: resist_chance(mr,mr_modifier)})
    nonzerodist=frozendict({i: (1-resist_chance(mr,mr_modifier))*prob_get(save_for_half_dist(save_number,damage_dist,save_modifier,autofail_num),i) for i in range(min_dist(save_for_half_dist(save_number,damage_dist,save_modifier,autofail_num)),max_dist(save_for_half_dist(save_number,damage_dist,save_modifier,autofail_num))+1)})
    return nonzerodist | zerodist


def spell_save_one_shot_function(save_type,save_modifier=0,autofail_num=1,mr_modifier=0):
    """Returns a one-shot-function for a spell granting a save suitable for entering into one_shot_histogram
       
       Required arguments:
       save_type, the type of saving throw, one of:
         'save_vs_paralyzation/poison/death', 
         'save_vs_rod/staff/wand', 
         'save_vs_petrification/polymorph', 
         'save_vs_breath_weapon', 
         'save_vs_spells'
       
       Optional arguments:
       save_modifier is a modifier to saves. For example, it would be -1 for the target of a specialist wizard in their specialty
       autofail_num is the number saves automatically fail on, which can be different with certain optional rules
       mr_modifier is a modifier to MR. For example, if you reduce the target's MR by 10%, it should be -10"""
    
    def one_shot_function(row):
        return spell_success_chance(row[save_type],save_modifier,autofail_num,row["MR"],mr_modifier)
        
    return one_shot_function

def spell_save_for_half_one_shot_function(save_type,damage_dist,save_modifier=0,autofail_num=1,mr_modifier=0):
    """Returns a one-shot-function for something granting a save for half damage suitable for entering into one_shot_histogram
       
       Required arguments:
       save_type, the type of saving throw, one of:
         'save_vs_paralyzation/poison/death', 
         'save_vs_rod/staff/wand', 
         'save_vs_petrification/polymorph', 
         'save_vs_breath_weapon', 
         'save_vs_spells'
       damage_dist, the distribution of possible damage on a failed save
         
       Optional arguments:
       save_modifier is a modifier to saves. For example, it would be -1 for the target of a specialist wizard in their specialty
       autofail_num is the number saves automatically fail on, which can be different with certain optional rules
       mr_modifier is a modifier to MR. For example, if you reduce the target's MR by 10%, it should be -10"""
    
    def one_shot_function(row):
        return prob_at_least(spell_save_for_half_dist(row[save_type],damage_dist,save_modifier,autofail_num,row["MR"],mr_modifier),row["hp"])
        
    return one_shot_function




def one_shot_histogram_XP(dataframe,low_XP,high_XP,one_shot_function,title=None):
    """Returns a histogram of the chance that an attack one-shots monsters in a given XP range.

       dataframe should be the result of a process_csv command
       low_XP is the lowest XP included, high_XP is the highest
       one_shot_function is a function that acts on the dataframe and gives a chance of one-shotting a monster
       """
    fig=dataframe.loc[(dataframe["XP"]>=low_XP) & (dataframe["XP"]<=high_XP)].apply(one_shot_function,axis=1).round(3).plot(kind="hist",x=0,y=dataframe.loc[(dataframe["XP"]>=low_XP) & (dataframe["XP"]<=high_XP)]["weight"],histfunc="sum",labels={  "0" : "one-shot chance"},title=title)
    fig.layout.update(showlegend=False,yaxis_title="average number monsters")
    fig.update_layout(title_subtitle={'text':"Created with one-shot-calculator v."+__version__,'font':{'color':'gray','size':13}})
    fig.update_xaxes(range=[0.0, 1.0])
    fig.update_traces(xbins={'start':0.0, 'end':1.0, 'size':0.05})
    fig.update_traces(hovertemplate='one-shot chance=%{x}<br>average number of monsters=%{y}<extra></extra>')

    return fig
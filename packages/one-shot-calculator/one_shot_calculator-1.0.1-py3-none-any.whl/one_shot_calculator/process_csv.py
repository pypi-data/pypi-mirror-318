"""
This module processes a CSV file obtained from an Excel sheet of D&D monsters.

If you have trouble due to your file being in a different encoding, try using the check_encoding function,
then edit the appropriate process_csv function as needed.
"""

import pandas as pd
import numpy as np
import math
import charset_normalizer
from importlib import resources as impresources
from . import csv
from one_shot_calculator.discrete_dists import *

def check_encoding(csv_filename):
    """Tries to guess the encoding of a csv file and prints the result"""
    #using importlib.resources to control access to the csv files
    csv_file=impresources.files(csv) / csv_filename
    with csv_file.open("rb") as rawdata:
        print(charset_normalizer.detect(rawdata.read(50000)))

def process_csv_3p5():
    """Processes the CSV file Monster Compendium for D&D 3.5 monsters into a usable pandas dataframe and returns the result"""

    #using importlib.resources to control access to the csv files
    csv_file=impresources.files(csv) / 'Monster Compendium (Graphless).csv'

    third_ed_monster_table=pd.read_csv(csv_file,encoding="windows-1250")

    #dropping the weird extra NaN line at the end
    third_ed_monster_table=third_ed_monster_table[~third_ed_monster_table.Creature.isna()]

    #dropping extra columns at the end that were used for a legend in the Excel sheet
    third_ed_monster_table=third_ed_monster_table.drop(third_ed_monster_table.columns[31:],axis=1)
    
    #get rid of the weird CR - monsters
    third_ed_monster_table=third_ed_monster_table[~(third_ed_monster_table.CR=='-')]

    #convert things that should be numbers to numbers
    third_ed_monster_table["CR"]=third_ed_monster_table["CR"].map(eval)
    third_ed_monster_table["HD"]=third_ed_monster_table["HD"].map(eval)
    third_ed_monster_table["(hp)"]=third_ed_monster_table["(hp)"].map(int)
    third_ed_monster_table["Spd"]=third_ed_monster_table["Spd"].map(lambda x: x if x!=x else int(x))
    third_ed_monster_table["AC"]=third_ed_monster_table["AC"].map(int)
    third_ed_monster_table["t"]=third_ed_monster_table["t"].map(int)
    third_ed_monster_table["ff"]=third_ed_monster_table["ff"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["Grpl"]=third_ed_monster_table["Grpl"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["F"]=third_ed_monster_table["F"].map(int)
    third_ed_monster_table["R"]=third_ed_monster_table["R"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["W"]=third_ed_monster_table["W"].map(int)
    third_ed_monster_table["S"]=third_ed_monster_table["S"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["D"]=third_ed_monster_table["D"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["Co"]=third_ed_monster_table["Co"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["I"]=third_ed_monster_table["I"].map(lambda x: x if x=='-' else int(x))
    third_ed_monster_table["W.1"]=third_ed_monster_table["W.1"].map(int)
    third_ed_monster_table["Ch"]=third_ed_monster_table["Ch"].map(int)

    #rename columns for user-friendliness
    third_ed_monster_table=third_ed_monster_table.rename(columns={"(hp)":"hp","s/f/b/c":"SwimFlyBurrowClimb","t":"TouchAC","ff":"FlatFootedAC","F":"Fort","R":"Ref","W":"Will","S":"Str","D":"Dex","Co":"Con","I":"Int","W.1":"Wis","Ch":"Cha"})

    #fixing a mistake in the original compendium, in case you get the CSV directly from there
    third_ed_monster_table.loc[third_ed_monster_table["Creature"]=="Dragon, Chromatic, Blue, Young Adult","CR"]=11.0

    return third_ed_monster_table

#The following functions are for the AD&D application

def anagram_filter(str):
    """Adds an extra 9 to monster names that appear as anagrams so they don't get caught by deduplication"""
    if str=="tarek" or str=="xaver" or str=="nilbog" or str=="roc":
        return str+"9"
    else:
        return str

def deduplicate(dataframe):
     """Restricts the dataframe to one monster of each name, preferring 2e monsters when possible
        Lumps together reorderings of words and certain misspellings, but still can miss category words 'mammal'"""
     return pd.DataFrame([group.sort_values(by=['Edition']).iloc[-1] for name, group in dataframe.groupby(dataframe.Name.map(lambda x: tuple(sorted(list(filter(lambda y: y.isalpha() or y.isnumeric(),anagram_filter(x)))))))])

def safenumcheck(entry):
    """Checks if something is numeric without throwing errors if it's NaN"""
    if entry is np.nan:
        return False
    return entry.isnumeric()

def definitely_smaller_mask(dataframe):
    """Includes monsters with size t,s,m and not l,h,g"""
    return (dataframe["Size"].str.contains(r'(?<![a-z])[tsm](?![a-z?])')) & ~(dataframe["Size"].isna() | dataframe["Size"].str.contains(r'(?<![a-z])[hlg](?![a-z])') | dataframe["Size"].str.contains(r'varies'))

def definitely_larger_mask(dataframe):
    """Includes monsters with size l,h,g and not t,s,m"""
    return (dataframe["Size"].str.contains(r'(?<![a-z])[hlg](?![a-z?])')) & ~(dataframe["Size"].isna() | dataframe["Size"].str.contains(r'(?<![a-z])[tsm](?![a-z])') | dataframe["Size"].str.contains(r'varies'))

def intelligencemask(dataframe):
    """Since unintelligent monsters have different saves, throws out monsters for which this is ambiguous"""
    return ~( (dataframe["Intelligence"]=='unratable') | (dataframe["Intelligence"]=='special') | (dataframe["Intelligence"]=="it doesn't need any, you do") | (dataframe["Intelligence"]=='not ratable') | (dataframe["Intelligence"]=='non to semi (0-4)') )

def acmask(dataframe):
    """Keeps only numeric ACs, including negative ACs"""
    return dataframe["AC"].map(safenumcheck) | dataframe["AC"].str.fullmatch(r'-[0-9]+')

def hdmask(dataframe):
    """Restricts to HD values which can currently be processed"""
    return dataframe["HD"].map(safenumcheck) | (dataframe["HD"].str.fullmatch(r"[0-9]/[0-9]")) | (dataframe["HD"].str.fullmatch(r"[0-9]+ \([0-9]+ hp\)")) | (dataframe["HD"].str.fullmatch(r"[0-9]+/[0-9]+ \([0-9]+ hp\)")) | (dataframe["HD"].str.fullmatch(r"[0-9]+[\+\-][0-9]+ \([0-9]+ hp\)")) | ((dataframe["HD"]!='5-14') & (dataframe["HD"]!='3-8') & (dataframe["HD"]!='2-4') & (dataframe["HD"].str.fullmatch(r"[0-9]+[\+\-][0-9]+")))

def mrmask(dataframe):
    """Restricts to MR that is a single percentage"""
    return dataframe["MR"].isna() | (dataframe["MR"]=='nil') | (dataframe["MR"]=='standard') | (dataframe["MR"].str.fullmatch(r'[0-9]+%'))

def sizemask(dataframe):
    """Restricts to monsters definitely m or smaller or definitely l or larger"""
    return definitely_smaller_mask(dataframe) | definitely_larger_mask(dataframe)

def xpmask(dataframe):
    """Restricts to monsters with definite XP values.
        Includes empty XP only if the monster has a definite Level value so that it can be filtered on those grounds."""
    return dataframe["XP"].map(safenumcheck) | (dataframe["XP"].isna() & ~dataframe["Level"].isna()) | dataframe["XP"].str.fullmatch(r'[0-9]+\+[0-9]+')

def allmasks(dataframe):
    """Puts all masks together"""
    return intelligencemask(dataframe) & acmask(dataframe) & hdmask(dataframe) & mrmask(dataframe) & sizemask(dataframe) & xpmask(dataframe)

def mr_interpret(mr_val):
    """Takes MR from a string to a number"""
    if mr_val is np.nan or mr_val=='nil' or mr_val=='standard':
        return 0
    else: #intended to cover cases where string is number%
        return int(mr_val[:-1])

def xp_separator(dataframe):
    """For 1e monsters, separates out monsters with explicit additional XP per hp"""

    numericones=pd.DataFrame({"base_XP":dataframe[dataframe["XP"].map(safenumcheck)]["XP"].map(int),"XP_per_hp":0})

    nanners=pd.DataFrame({"base_XP":~dataframe[dataframe["XP"].isna()]["XP"].isna(),"XP_per_hp":0})

    has_xp_per_hp=dataframe[(~dataframe["XP"].isna()) & dataframe["XP"].str.fullmatch(r"[0-9]+\+[0-9]+")]["XP"].str.extract(r"(?P<base_XP>[0-9]+)\+(?P<XP_per_hp>[0-9]+)")
    if has_xp_per_hp.shape[0]>0:
        has_xp_per_hp.loc[:,"base_XP"]=has_xp_per_hp["base_XP"].map(int)
        has_xp_per_hp.loc[:,"XP_per_hp"]=has_xp_per_hp["XP_per_hp"].map(int)
        
    answer=pd.concat([numericones,nanners,has_xp_per_hp]).sort_index()
    if answer.shape[0]!=dataframe.shape[0]:
        raise ValueError("some HD data unprocessed")
    return answer

def hd_separator(dataframe):
    """Separates out the number of hit dice, the amount of bonus hit points, and any fixed hp value given.
        Currently does not support ranges of fixed hp"""
    
    dice_plus_bonus=dataframe[dataframe["HD"].str.fullmatch(r"[0-9]+[\+\-][0-9]+")]["HD"].str.extract(r"(?P<HD_dice>[0-9]+)(?P<HD_bonus>[\+\-][0-9]+)")
    if dice_plus_bonus.shape[0]>0:
        dice_plus_bonus.loc[:,"HD_dice"]=dice_plus_bonus["HD_dice"].map(int)
        dice_plus_bonus.loc[:,"HD_bonus"]=dice_plus_bonus["HD_bonus"].map(int)
        dice_plus_bonus.loc[:,"fixed_hp"]=False

    dice_and_fixed=dataframe[dataframe["HD"].str.fullmatch(r"[0-9]+ \([0-9]+ hp\)")]["HD"].str.extract(r"(?P<HD_dice>[0-9]+) \((?P<fixed_hp>[0-9]+) hp\)")
    if dice_and_fixed.shape[0]>0:
        dice_and_fixed.loc[:,"HD_dice"]=dice_and_fixed["HD_dice"].map(int)
        dice_and_fixed.loc[:,"HD_bonus"]=0
        dice_and_fixed.loc[:,"fixed_hp"]=dice_and_fixed["fixed_hp"].map(int)

    fraction_and_fixed=dataframe[dataframe["HD"].str.fullmatch(r"[0-9]+/[0-9]+ \([0-9]+ hp\)")]["HD"].str.extract(r"(?P<HD_dice>[0-9]+/[0-9]+) \((?P<fixed_hp>[0-9]+) hp\)")
    if fraction_and_fixed.shape[0]>0:
        fraction_and_fixed.loc[:,"HD_dice"]=fraction_and_fixed["HD_dice"].map(eval)
        fraction_and_fixed.loc[:,"HD_bonus"]=0
        fraction_and_fixed.loc[:,"fixed_hp"]=fraction_and_fixed["fixed_hp"].map(int)

    dice_and_bonus_and_fixed=dataframe[dataframe["HD"].str.fullmatch(r"[0-9]+[\+\-][0-9]+ \([0-9]+ hp\)")]["HD"].str.extract(r"(?P<HD_dice>[0-9]+)(?P<HD_bonus>[\+\-][0-9]+) \((?P<fixed_hp>[0-9]+) hp\)")
    if dice_and_bonus_and_fixed.shape[0]>0:
        dice_and_bonus_and_fixed.loc[:,"HD_dice"]=dice_and_bonus_and_fixed["HD_dice"].map(int)
        dice_and_bonus_and_fixed.loc[:,"HD_bonus"]=dice_and_bonus_and_fixed["HD_bonus"].map(int)
        dice_and_bonus_and_fixed.loc[:,"fixed_hp"]=dice_and_bonus_and_fixed["fixed_hp"].map(int)
    
    numericones=pd.DataFrame({"HD_dice":dataframe[dataframe["HD"].str.isnumeric()]["HD"].map(int),"HD_bonus":0,"fixed_hp": False})
    
    fractions=pd.DataFrame({"HD_dice":dataframe[dataframe["HD"].str.fullmatch(r'[0-9]/[0-9]+')]["HD"].map(eval),"HD_bonus":0, "fixed_hp":False})
    
    answer=pd.concat([dice_plus_bonus,dice_and_fixed,fraction_and_fixed,dice_and_bonus_and_fixed,numericones,fractions]).sort_index()
    if answer.shape[0]!=dataframe.shape[0]:
        raise ValueError("some HD data unprocessed")
    return answer

def effective_hd(hd_dice,hd_bonus,mode="DMG"):
    """Currently just implements DMG version of HD rules, in future will include MM version as well"""
    if mode=="DMG":
        if hd_bonus>0:
            return hd_dice+math.ceil(hd_bonus/4)
        else:
            return hd_dice
    else:
        raise ValueError('Not a valid mode')

def intfilter(int,hd):
    """Gives half HD rounded up for unintelligent monsters effective HD for saves"""
    if int==np.nan or int=='non (0)' or int=='programmed':
        return math.ceil(hd/2)
    else:
        return hd

def save_from_hd(hd,type,table='warrior'):
    """Finds save values from HD values. Currently only the warrior table is coded."""
    match table:
        case 'warrior':
            if hd<1:
                match type:
                    case 'paralyzation/poison/death':
                        return 16
                    case 'rod/staff/wand':
                        return 18
                    case 'petrification/polymorph':
                        return 17
                    case 'breath_weapon':
                        return 20
                    case 'spells':
                        return 19
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<3:
                match type:
                    case 'paralyzation/poison/death':
                        return 14
                    case 'rod/staff/wand':
                        return 16
                    case 'petrification/polymorph':
                        return 15
                    case 'breath_weapon':
                        return 17
                    case 'spells':
                        return 17
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<5:
                match type:
                    case 'paralyzation/poison/death':
                        return 13
                    case 'rod/staff/wand':
                        return 15
                    case 'petrification/polymorph':
                        return 14
                    case 'breath_weapon':
                        return 16
                    case 'spells':
                        return 16
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<7:
                match type:
                    case 'paralyzation/poison/death':
                        return 11
                    case 'rod/staff/wand':
                        return 13
                    case 'petrification/polymorph':
                        return 12
                    case 'breath_weapon':
                        return 13
                    case 'spells':
                        return 14
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<9:
                match type:
                    case 'paralyzation/poison/death':
                        return 10
                    case 'rod/staff/wand':
                        return 12
                    case 'petrification/polymorph':
                        return 11
                    case 'breath_weapon':
                        return 12
                    case 'spells':
                        return 13
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<11:
                match type:
                    case 'paralyzation/poison/death':
                        return 8
                    case 'rod/staff/wand':
                        return 10
                    case 'petrification/polymorph':
                        return 9
                    case 'breath_weapon':
                        return 9
                    case 'spells':
                        return 11
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<13:
                match type:
                    case 'paralyzation/poison/death':
                        return 7
                    case 'rod/staff/wand':
                        return 9
                    case 'petrification/polymorph':
                        return 8
                    case 'breath_weapon':
                        return 8
                    case 'spells':
                        return 10
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<15:
                match type:
                    case 'paralyzation/poison/death':
                        return 5
                    case 'rod/staff/wand':
                        return 7
                    case 'petrification/polymorph':
                        return 6
                    case 'breath_weapon':
                        return 5
                    case 'spells':
                        return 8
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<17:
                match type:
                    case 'paralyzation/poison/death':
                        return 4
                    case 'rod/staff/wand':
                        return 6
                    case 'petrification/polymorph':
                        return 5
                    case 'breath_weapon':
                        return 4
                    case 'spells':
                        return 7
                    case _:
                        raise ValueError("Not a valid save type!")
            else:
                match type:
                    case 'paralyzation/poison/death':
                        return 3
                    case 'rod/staff/wand':
                        return 5
                    case 'petrification/polymorph':
                        return 4
                    case 'breath_weapon':
                        return 4
                    case 'spells':
                        return 6
                    case _:
                        raise ValueError("Not a valid save type!")
        case 'priest':
            if hd<4:
                match type:
                    case 'paralyzation/poison/death':
                        return 10
                    case 'rod/staff/wand':
                        return 14
                    case 'petrification/polymorph':
                        return 13
                    case 'breath_weapon':
                        return 16
                    case 'spells':
                        return 15
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<7:
                match type:
                    case 'paralyzation/poison/death':
                        return 9
                    case 'rod/staff/wand':
                        return 13
                    case 'petrification/polymorph':
                        return 12
                    case 'breath_weapon':
                        return 15
                    case 'spells':
                        return 14
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<10:
                match type:
                    case 'paralyzation/poison/death':
                        return 7
                    case 'rod/staff/wand':
                        return 11
                    case 'petrification/polymorph':
                        return 10
                    case 'breath_weapon':
                        return 13
                    case 'spells':
                        return 12
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<13:
                match type:
                    case 'paralyzation/poison/death':
                        return 6
                    case 'rod/staff/wand':
                        return 10
                    case 'petrification/polymorph':
                        return 9
                    case 'breath_weapon':
                        return 12
                    case 'spells':
                        return 11
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<16:
                match type:
                    case 'paralyzation/poison/death':
                        return 5
                    case 'rod/staff/wand':
                        return 9
                    case 'petrification/polymorph':
                        return 8
                    case 'breath_weapon':
                        return 11
                    case 'spells':
                        return 10
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<19:
                match type:
                    case 'paralyzation/poison/death':
                        return 4
                    case 'rod/staff/wand':
                        return 8
                    case 'petrification/polymorph':
                        return 7
                    case 'breath_weapon':
                        return 10
                    case 'spells':
                        return 9
                    case _:
                        raise ValueError("Not a valid save type!")
            else:
                match type:
                    case 'paralyzation/poison/death':
                        return 2
                    case 'rod/staff/wand':
                        return 6
                    case 'petrification/polymorph':
                        return 5
                    case 'breath_weapon':
                        return 8
                    case 'spells':
                        return 7
                    case _:
                        raise ValueError("Not a valid save type!")
        case 'rogue':
            if hd<5:
                match type:
                    case 'paralyzation/poison/death':
                        return 13
                    case 'rod/staff/wand':
                        return 14
                    case 'petrification/polymorph':
                        return 12
                    case 'breath_weapon':
                        return 16
                    case 'spells':
                        return 15
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<9:
                match type:
                    case 'paralyzation/poison/death':
                        return 12
                    case 'rod/staff/wand':
                        return 12
                    case 'petrification/polymorph':
                        return 11
                    case 'breath_weapon':
                        return 15
                    case 'spells':
                        return 13
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<13:
                match type:
                    case 'paralyzation/poison/death':
                        return 11
                    case 'rod/staff/wand':
                        return 10
                    case 'petrification/polymorph':
                        return 10
                    case 'breath_weapon':
                        return 14
                    case 'spells':
                        return 11
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<17:
                match type:
                    case 'paralyzation/poison/death':
                        return 10
                    case 'rod/staff/wand':
                        return 8
                    case 'petrification/polymorph':
                        return 9
                    case 'breath_weapon':
                        return 13
                    case 'spells':
                        return 9
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<21:
                match type:
                    case 'paralyzation/poison/death':
                        return 9
                    case 'rod/staff/wand':
                        return 6
                    case 'petrification/polymorph':
                        return 8
                    case 'breath_weapon':
                        return 12
                    case 'spells':
                        return 7
                    case _:
                        raise ValueError("Not a valid save type!")
            else:
                match type:
                    case 'paralyzation/poison/death':
                        return 8
                    case 'rod/staff/wand':
                        return 4
                    case 'petrification/polymorph':
                        return 7
                    case 'breath_weapon':
                        return 11
                    case 'spells':
                        return 5
                    case _:
                        raise ValueError("Not a valid save type!")
        case 'wizard':
            if hd<6:
                match type:
                    case 'paralyzation/poison/death':
                        return 14
                    case 'rod/staff/wand':
                        return 11
                    case 'petrification/polymorph':
                        return 13
                    case 'breath_weapon':
                        return 15
                    case 'spells':
                        return 12
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<11:
                match type:
                    case 'paralyzation/poison/death':
                        return 13
                    case 'rod/staff/wand':
                        return 9
                    case 'petrification/polymorph':
                        return 11
                    case 'breath_weapon':
                        return 13
                    case 'spells':
                        return 10
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<16:
                match type:
                    case 'paralyzation/poison/death':
                        return 11
                    case 'rod/staff/wand':
                        return 7
                    case 'petrification/polymorph':
                        return 9
                    case 'breath_weapon':
                        return 11
                    case 'spells':
                        return 8
                    case _:
                        raise ValueError("Not a valid save type!")
            elif hd<21:
                match type:
                    case 'paralyzation/poison/death':
                        return 10
                    case 'rod/staff/wand':
                        return 5
                    case 'petrification/polymorph':
                        return 7
                    case 'breath_weapon':
                        return 9
                    case 'spells':
                        return 6
                    case _:
                        raise ValueError("Not a valid save type!")
            else:
                match type:
                    case 'paralyzation/poison/death':
                        return 8
                    case 'rod/staff/wand':
                        return 3
                    case 'petrification/polymorph':
                        return 5
                    case 'breath_weapon':
                        return 7
                    case 'spells':
                        return 4
                    case _:
                        raise ValueError("Not a valid save type!")
        case _:
            raise ValueError("Not a valid save table!")

def save_from_row(row,save_mode,type):
    match save_mode:
        case "all_warrior":
            if type=='paralyzation/poison/death':
                return save_from_hd(effective_hd(row["HD_dice"],row["HD_bonus"]),type)
            else:
                return save_from_hd(intfilter(row["Intelligence"],effective_hd(row["HD_dice"],row["HD_bonus"])),type)
        case "worst_case":
            if type=='paralyzation/poison/death':
                return min([save_from_hd(effective_hd(row["HD_dice"],row["HD_bonus"]),type,table=x) for x in ["priest","warrior","rogue","wizard"]])
            else:
                return min([save_from_hd(intfilter(row["Intelligence"],effective_hd(row["HD_dice"],row["HD_bonus"])),type,table=x) for x in ["priest","warrior","rogue","wizard"]])
        case _:
            raise ValueError("Not a valid save mode!")

def hp_dist(row):
    """Finds the hp options for a row in the dataframe"""
    if row["fixed_hp"]:
        return {row["fixed_hp"]:1}
    else:
        if row["HD_dice"]<1:
            return min_one(add_const_to_dist(mult_dist_by_const(basic_die_dist(8),row["HD_dice"]),row["HD_bonus"]))
        else:
            return min_one(add_const_to_dist(multiple_dist(row["HD_dice"],basic_die_dist(8)),row["HD_bonus"]))


def process_csv_adnd(edition_purist=None,save_mode="all_warrior"):
    """Processes the CSV file SBLaxman's AD&D Monster List for AD&D monsters into a usable pandas dataframe and returns the result
        edition_purist lets you specify to only include 1e or 2e monsters with edition_purist='1e' or '2e'
        save_mode lets you choose:
            all_warrior: all monsters assumed to save as warrior
            worst_case: all monsters assumed to have the highest save in any class's table for that level
        
        Current simplifications: 
        -2e save rules only, psionicist saves currently not included
        -DMG save rules rather than MM save rules
        -Various monsters filtered out if key stats are not easily machine-readable """

    #using importlib.resources to control access to the csv files
    csv_file=impresources.files(csv) / "SBLaxman's AD&D Monster List 2.1.csv"

    adnd_monster_table=pd.read_csv(csv_file)

    #every column is stringy so we clean up trailing whitespaces and capitalization
    adnd_monster_table=adnd_monster_table.apply(lambda col: col.str.lower().str.strip())

    #filter for a specific edition if you want
    if edition_purist is not None:
        adnd_monster_table=adnd_monster_table[adnd_monster_table['Edition']==edition_purist]

    print("Before filters, there are ",deduplicate(adnd_monster_table).shape[0]," unique monsters")
    
    #apply masks and deduplicate result
    adnd_monster_table=adnd_monster_table[allmasks(adnd_monster_table)]

    adnd_monster_table=deduplicate(adnd_monster_table)

    print("After filters, there are ",adnd_monster_table.shape[0]," unique monsters")

    #getting AC and MR to numeric values
    adnd_monster_table.loc[:,"AC"]=adnd_monster_table["AC"].map(int)

    adnd_monster_table.loc[:,"MR"]=adnd_monster_table["MR"].map(mr_interpret)

    #separate out HD_dice, HD_bonus, and any fixed_hp
    separated=hd_separator(adnd_monster_table)

    adnd_monster_table=adnd_monster_table.join(separated)

    #separates out base_XP and XP_per_hp for monsters that have it
    xp_separated=xp_separator(adnd_monster_table)

    adnd_monster_table=adnd_monster_table.join(xp_separated)

    #computes save numbers, currently using default 'everything is a warrior'
    adnd_monster_table.loc[:,'save_vs_paralyzation/poison/death']=adnd_monster_table.apply(lambda x: save_from_row(x,save_mode,'paralyzation/poison/death'),axis=1)
    adnd_monster_table.loc[:,'save_vs_rod/staff/wand']=adnd_monster_table.apply(lambda x: save_from_row(x,save_mode,'rod/staff/wand'),axis=1)
    adnd_monster_table.loc[:,'save_vs_petrification/polymorph']=adnd_monster_table.apply(lambda x: save_from_row(x,save_mode,'petrification/polymorph'),axis=1)
    adnd_monster_table.loc[:,'save_vs_breath_weapon']=adnd_monster_table.apply(lambda x: save_from_row(x,save_mode,'breath_weapon'),axis=1)
    adnd_monster_table.loc[:,'save_vs_spells']=adnd_monster_table.apply(lambda x: save_from_row(x,save_mode,'spells'),axis=1)

    #adds an entry that says whether a monster is large enough to take large monster damage
    adnd_monster_table.loc[:,'larger_than_man']=definitely_larger_mask(adnd_monster_table)

    #finds a distribution dict for hp for each monster, then explodes the dataframe, making one row for each hp value
    adnd_monster_table.loc[:,"hp_dist"]=adnd_monster_table.apply(hp_dist,axis=1)
    adnd_monster_table.loc[:,'hp']=adnd_monster_table['hp_dist'].map(list)
    adnd_monster_table=adnd_monster_table.explode('hp')
    #weight by probability
    adnd_monster_table.loc[:,'weight']=adnd_monster_table.apply(lambda x: x['hp_dist'][x['hp']],axis=1)
    #make sure XP increases with hp for monsters that work that way
    adnd_monster_table.loc[:,'XP']=(adnd_monster_table['base_XP']+adnd_monster_table['hp']*adnd_monster_table['XP_per_hp'])
    #make columns have int type when likely to be useful and remove impossible hp values
    adnd_monster_table=adnd_monster_table.astype({'hp':'int','XP':'int','AC':'int'})
    adnd_monster_table=adnd_monster_table[adnd_monster_table['weight']>0]


    return adnd_monster_table
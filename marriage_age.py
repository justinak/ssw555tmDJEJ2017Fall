"""
User Story 10
Marriage after 14

Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)
"""

import unittest
from GIF_classes import GedLine, Individuals, Family
from project3 import GEDCOM_Reader

from datetime import date
from datetime import datetime



gedcom_file = 'C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family.ged'


def marriage_age(individuals, families):
    
    for famId in families:
        if famId.marriage:
            husbandId = None
            wifeId = None
            
            for indis in individuals: 
                if indis.IndId == famId.husbandId: # check husband in family
                    husbandId = indis
                if indis.IndId == famId.wifeId: # check wife in family
                    wifeId = indis
            """  determine if marriage year occurred more than 14 years after birth """        
            if famId.marriage.year - husbandId.birthday.year <= 14: 
                print('ERROR: FAMILY: US10:', husbandId,':Marriage before age 14')
            if famId.marriage.year - wifeId.birthday.year <= 14:
                print('ERROR: FAMILY: US10:', famId.marriage,':Marriage before age 14')

marriage_age(individuals, families)



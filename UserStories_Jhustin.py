from datetime import date
from datetime import datetime
import os

import sys
import unittest


gedcom_file = 'Jhustin1.ged'

# main function for taking the file path
def main():

    individual, families = GEDCOM_Reader(gedcom_file)
    
#user story was to make sure that siblings could not marry each other
def checkIncest(families):
  Story_name = "US18"
  error_msg = "Siblings cannot marry"

  for family in families:
    for child1 in family.children:
        for child2 in family.children:
            for marriage in families:
                if child1 == child2:
                    pass
                elif(child1 == marriage.wife_Name or child1 == marriage.husband_Name) and (child2 == marriage.wife_Name or child2 == marriage.husband_Name):
                    location = [child1, child2]
                    error = (Story_name, error_msg, location)
                    print( error) 

def check_genderrole(individuals,families):
    Story_name = "US21"
    error_msg = "Gender role does not match"
    
    for family in families:
        for individual in individuals:
            if (individual.IndId == family.husbandId and individual.gender != "M"):
                location = [individual.IndId]
                error = (Story_name, error_msg, location)
                print(error)
            elif (individual.IndId == family.wifeId and individual.gender != "F"):
                location = [individual.IndId]
                error = (Story_name, error_msg, location)
                print(error)
            
def marriage_before_divorce(families):
    Story_name = "US04"
    error_msg = "Marriage should occur before divorce"
    
    for family in families:
        if family.marriage and family.divorced:
            if family.divorced <= family.marriage:
                location = [family.husbandId, family.wifeId]
                error = (Story_name, error_msg, location)
                print(error)
                
def marriage_before_death(individuals, families):
    Story_name = "US05"
    error_msg = "Marriage should occur before death"
    
    for family in families:
        for individual in individuals:
            if individual.IndId in [family.husbandId, family.wifeId] and individual.death_date and family.marriage:
                if individual.death_date <= family.marriage:
                    location = [individual.IndId]
                    error = (Story_name, error_msg, location)
                    print(error)

def divorce_before_death(individuals, families):
    Story_name = "US06"
    error_msg = "Divorce should occur before death"
    
    for family in families:
        for individual in individuals:
            if individual.IndId in [family.husbandId, family.wifeId] and individual.death_date and family.divorced:
                if individual.death_date <= family.divorced:
                    location = [individual.IndId]
                    error = (Story_name, error_msg, location)
                    print(error)

def illegitimate_date(individuals, families):
    Story_name = "US42"
    error_msg = "Date does not exist"

    try:
        GEDCOM_Reader(gedcom_file)
    except ValueError:
        error = (Story_name, error_msg, location)

def list_ages(individuals, families):
    Story_name = "US27"
    all_ages = {}
    for individual in individuals:
        all_ages[individual.IndId] = individual.age
        list_age = ''.join(str(all_ages))
        message = (Story_name, list_age)
        pass
    print(message)

def list_deceased(individuals, families):
    Story_name = "US29"
    all_dead = []
    all_dead.append 
    for family in families:
        for individual in individuals:
            if individual.death_date:
                all_dead.append(individual.IndId)
                list_dead = ''.join(str(all_dead))
                message =(Story_name + " All deceased family members: " + list_dead)
                pass
        print(message)
                               
class Test_checkIncest(unittest.TestCase):
    #One sibling married another sibling
    def test_1(self):
        self.assertEqual(checkIncest(GEDCOM_Reader('Jhustin1.ged')[1]),  ('US18', 'Siblings cannot marry', ['@I1@', '@I11@']),'This is incest')
        #Husband is a female
    def test_2(self):
        self.assertEqual(check_genderrole(*GEDCOM_Reader('Jhustin1.ged')),('US21', 'Gender role does not match', ['@I2@']),'Should be fine')
    #Divorce happens before the date of marriage    
    def test_3(self):
        self.assertEqual(marriage_before_divorce(GEDCOM_Reader('Jhustin1.ged')[1]),('US04', 'Marriage should occur before divorce', ['@I4@', '@I5@']),'Should be fine')
    #Death happens before the date of marriage    
    def test_4(self):
        self.assertEqual(marriage_before_death(*GEDCOM_Reader('Jhustin1.ged')),('US05', 'Marriage should occur before death', ['@I4@']),'Should be fine')

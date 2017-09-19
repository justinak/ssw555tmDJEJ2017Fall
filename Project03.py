""" 
Created on Sun Sep 17 2017 10:01:00 2017

@author: jkopec

 """
import unittest
from prettytable import PrettyTable
from collections import defaultdict

class Lineage:
    """Create a Lineage for family DJEJ """
    def __init__(self): # initialize repository
        self.individuals = dict() # key: Individual ID, value: instance of class Individual
        self.families = dict() # key: Family ID, value: instance of class Family

    def read_gedcom(self, gedcom_file):
        try:
            gedcom_file = open("C:\Users\jkope\Documents\Stevens-Software Engineering Masters\SSW 555 - Agile Methods for Software Development\Fall 2017\Week 3 - Scrum\DJEJ_family.ged", 'r')
        except FileNotFoundError:
            print("File cannot be read" )
            return(None)
        else:
            with gedcom_file:  
                for each_line in gedcom_file:
                    DJEJ_Fam = each_line.strip().split() 
                    # update line under with Devanshu's identification for Individual class
                    self.individuals[ID] = Individual()
                    self.families[ID] = Family(famID, married, divorced, husbandID, husband_name, wifeID, wife_name, children)
                    
                    for token in DJEJ_Fam:
                        if token[2] == 'FAM':
                            token.append(
        
    def convert_date(self):
        # trying to find if there is a module for converting the date or a function from:
        # 11 May 1991 to 1991-05-11
                    
    def individuals_summary(self):
        """ Create a table displaying information about individuals in the family """
        individuals_table = PrettyTable(['ID', 'Name', 'Gender', 'Birthday', 'Age', 'Alive', 'Death', 'Child', 'Spouse'])
        for individual in self.individuals.values():
            individuals_table.add_row([individuals.ID, individuals.name, individuals.gender, individuals.birthday, individuals.age, individuals.alive, individuals.death, individuals.child, individuals.spouse])
        print(individuals_table)
        
        
    def families_summary(self):
        """ Create a table displaying information about families in the lineage """
        families_table = PrettyTable(['ID', 'Married', 'Divorced', 'Husband ID', 'Husband Name', 'Wife ID', 'Wife Name', 'Children'])
        for family in self.families.values():
            families_table.add_row([families.famID, families.married, families.divorced, families.husbandID, families.husband_name, families.wifeID, families.wife_name, families.children])
        print(families_table)
                  
                  
class Family: # initialize family class
    def __init__(self, famID, married, divorced, husbandID, husband_name, wifeID, wife_name, children):
        self.famID = famID
        self.married = married
        self.divorced = divorced
        self.individuals[ID] = husbandID
        self.individuals[ID][name] = husband_name
        self.individuals[ID] = wifeID
        self.individuals[ID][name] = wife_name 
        self.children = defaultdict() # create dictionary with key FamID and values being Children in that family OR would this be better as a list                      
                   
def main():
    DJEJ_lineage = Lineage()
    DJEJ_lineage.read_gedcom(gedcom_file) 
    DJEJ_lineage.convert_date()
    DJEJ_lineage.individuals_summary()
    DJEJ_lineage.families_summary()


class LineageTest(unittest.TestCase):

    def read_gedcom(self, gedcom_file):
""" when this function is complete in the Lineage class copy it down here"""
        try:
            gedcom_file = open("C:\Users\jkope\Documents\Stevens-Software Engineering Masters\SSW 555 - Agile Methods for Software Development\Fall 2017\Week 3 - Scrum\DJEJ_family.ged", 'r')
        except FileNotFoundError:
            print("File cannot be read" )
            return(None)
        else:
            with gedcom_file:  
                for each_line in gedcom_file:
                    DJEJ_Fam = each_line.strip().split() 
                    # update line under with Devanshu's identification for Individual class
                    self.individuals[ID] = Individual()
                    self.families[ID] = Family(famID, married, divorced, husbandID, husband_name, wifeID, wife_name, children)

    def test_individuals_summary(self):
        """ Test Individual summary table """
        LineageTest.read_gedcom
        IndID = lineage.individuals_summary # add from Individual definition
        self.assertEqual(IndID, '')  # IndID may be changed just used as an example to get a start
        # complete the rest of the assertions to verify correctness

    def test_families_summary(self):
        """ Test Family summary table """        
        LineageTest.read_gedcom
        famID, married, divorced, husbandID, husband_name, wifeID, wife_name, children = lineage.families_summary
        self.assertEqual(famID, '@F1')
        self.assertEqual(married, '1991-05-11')
        self.assertEqual(divorced, 'N/A')
        self.assertEqual(husbandID, '@I2@')
        self.assertEqual(husband_name, 'Adam /Kopec/')
        self.assertEqual(wifeID, '@I3@')
        self.assertEqual(wife_name, 'Helena /Kopec/')
        self.assertEqual(children, ['@I1@', '@I4@', '@I5@']) 
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
    main()

"""
This file provides classes for parsing the GEDCOM file
"""

from prettytable import PrettyTable

from datetime import date
from datetime import datetime
import os
import sys


valid_tags = ['HEAD', 'NOTE', 'TRLR', 'INDI', 'FAM', 'BIRT', 'CHIL', 'DEAT', 'DIV', 'FAMC', 'FAMS', 'HUSB', 'MARR', 'NAME', 'SEX', 'WIFE', 'DATE']


class GedLine(object):
    """  break gedcom lines into tokens """
    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        list_line = line.split(' ')
        # set level of the object
        self.level = int(list_line[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = list_line[1]
            self.arg = list_line[2:]

        if self.level == 0:
            if list_line[1] in valid_tags:
                self.tag = list_line[1]
                self.arg = None
            else:
                self.tag = list_line[2]
                self.ref = list_line[1]


class Individuals(object): # initialize Individuals class
    def __init__(self, indID):
        self.indID = indID  # Individual ID
        self.name = None # Individual name
        self.birthday = None # Individual's birthday
        self.gender = None # gender of individual
        self.death_date = None # date of death for individual
        self.alive = True # True if indivudal alive, else false
        self.famc = [] # family id where individual is a child
        self.fams = [] # family id where individual is parent


class Families(object): # initialize Families class
    def __init__(self, famID):
        self.famID = famID
        self.marriage = None  # marriage in family
        self.divorced = None  # divorce in family
        self.husbandID = None  # ID of husband in family
        self.husband_name = None # husband name
        self.wifeID = None  # ID of wife in family
        self.wife_name = None # wife name
        self.children = [ ]   # create a list for children in family
        


# Function to Parse the GEDCOM file
def GEDCOM_Reader(gedcom_file):
    individual = [ ]
    family = [ ]
    gedcom_list = [ ]

    # read each line from file and strip new line from the last
    lines = [line.rstrip('\n\r') for line in open(gedcom_file)]

    # Create objects and add it to the list
    for line in lines:
        current_gedcom = GedLine(line)
        gedcom_list.append(current_gedcom)

    # Iterate every tag
    for index, gedcomline in enumerate(gedcom_list):
        #for saving Individual person
        if gedcomline.tag == 'INDI':
            date = None
            # Create blank object for the person
            indi_person = Individuals(gedcomline.ref)

            # set the values of the object UNTIL next level 0
            for gedcom_line in gedcom_list[index + 1:]:
                if gedcom_line.level == 0:
                    break
                if gedcom_line.tag == 'NAME':
                    indi_person.name = gedcom_line.arg
                if gedcom_line.tag == 'SEX':
                    indi_person.gender = gedcom_line.arg[0]
                if gedcom_line.tag == 'BIRT':
                    date = 'BIRT'
                if gedcom_line.tag == 'DEAT':
                    date = 'DEAT'
                if gedcom_line.tag == 'FAMC':
                    indi_person.famc.append(gedcom_line.arg[0])
                if gedcom_line.tag == 'FAMS':
                    indi_person.fams.append(gedcom_line.arg[0])

                # check if date is birth or date
                if gedcom_line.tag == 'DATE':
                    if date_type == 'BIRT':
                        indi_person.birthday = date(
                            int(gedcom_line.arg[2]),
                            datetime.strptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0]))
                        date = None
                    elif date_type == 'DEAT':
                        indi_person.death_date = date(
                            int(gedcom_line.arg[2]),
                            datetime.striptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0]))
                        indi_person.alive = False
                        date_type = None

            # add object into the individual list
            individual.append(indi_person)

        # For family list
        if gedcomline.tag == 'FAM':

            date = None

            # create blank object
            fam_obj = Families(gedcomline.ref)

            # ste values until next level 0
            for gedcom_line in gedcom_list[index + 1:]:
                if gedcom_line.level == '0':
                    break
                if gedcom_line.tag == 'MARR':
                    date = 'MARR'
                if gedcom_line.tag == 'DIV':
                    date = 'DIV'
                if gedcom_line.tag == "HUSB":
                    fam_obj.husbandID = gedcom_line.arg[0]
                    for person in individual:
                        if person.indID == gedcom_line.arg[0]:
                            fam_obj.husband_name = person.name
                if gedcom_line.tag == 'WIFE':
                    fam_obj.wifeID = gedcom_line.arg[0]
                    for person in individual:
                        if person.indID == gedcom_line.arg[0]:
                            fam_obj.wife_name = person.name
                if gedcom_line.tag == 'CHIL':
                    fam_obj.children.append(gedcom_line.arg[0])

                # check if marriage date or divorce date
                if gedcom_line.tag == 'DATE':
                    if date == 'MARR':
                        fam_obj.marriage = date(
                            int(gedcom_line.arg[2]),
                            datetime.striptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0]))

                        date = None
                    elif date == 'DIV':
                        fam_obj.divorced = date(int(gedcom_line.arg[2]),datetime. striptime(gedcom_line.arg[1], '%b').month, int(gedcom_line.arg[0]))
                        date = None
            
            families.append(fam_obj) # append object into the family list

    return individual, families



#default file path

gedcom_file = 'C:/Devanshu/Python Project/DJEJ_family.ged'

individuals = PrettyTable()
families = PrettyTable()

# main function for taking the file path
def main():
    individual, families = GEDCOM_Reader(gedcom_file)
    summary_table(individual, families)


def summary_table(individual, families):
    """ Summary tables for individuals and families """
    print()
    print("Individuals")
    print()
    individuals.field_names = ["ID","Name","Gender","Birthday", "Age", "Alive", "Death", "Child","Spouse"]
    for line in individual:
        attrs = vars(line)
        individuals.add_row(attrs.values())

    print(individuals)
    print()
    print()
    print("Families")
    print()
    # print Families
    families.field_names = ["ID","Married","Divorced", "Husband ID","Husband Name","Wife ID","Wife Name","Children"]
    for line in families:
        attrs = vars(line)
        families.add_row(attrs.values())
    print(families)      


if __name__ == '__main__':
    sys.stdout = open("PR3-output.txt","w")
    main()
    sys.__stdout__.close()
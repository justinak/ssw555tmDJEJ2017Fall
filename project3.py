"""
This file provides classes for parsing the GEDCOM file
"""

from datetime import date
from datetime import datetime
import os

import sys

from prettytable import PrettyTable

validTags = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE',
             'INDI', 'FAM']

# class for every gedcom tag line
class GedLine(object):

    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        list_Line = line.split(' ',)
        # set level of the object
        self.level = int(list_Line[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = list_Line[1]
            self.arg = list_Line[2:]

        if self.level == 0:
            if list_Line[1] in validTags:
                self.tag = list_Line[1]
                self.arg = None
            else:
                self.tag = list_Line[2]
                self.ref = list_Line[1]


# class for individual persons
class Individuals(object):

    def __init__(self, IndId):
        self.IndId = IndId  #umoque id of individual person
        self.name = None # name of individual person
        self.birthday = None # Date of birthday of individual person
        self.age = None # Age of indvidual person
        self.gender = None # gender of individual person
        self.death_date = None # Date of death of individual person
        self.alive = True # person alive or dead
        self.famc = [] # family id where individual is a child
        self.fams = [] # family id where individual is parent

# class for families
class Family(object):

    def __init__(self, famId):
        self.famId = famId
        self.marriage = None  # marriage event for family
        self.husbandId = None  # for husband in family
        self.husband_Name = None # name of husband
        self.wifeId = None  # for wife in family
        self.wife_Name = None # for name of the wife
        self.children = []  # for child in family
        self.divorced = None  # divorce event in family


# Function to Parse the GEDCOM file
def GEDCOM_Reader(gedcom_file):
    individual = []
    family = []
    gedcom_list = []

    # read each line from file and strip \n from the last
    lines = [line.rstrip('\n\r') for line in open(gedcom_file)]

    # Create objects and add it to the list
    for line in lines:
        current_gedcom = GedLine(line)
        gedcom_list.append(current_gedcom)

    # Iterate every tag
    for index, gedcomline in enumerate(gedcom_list):
        #for saving Individual person
        if gedcomline.tag == 'INDI':

            date_of = None
            # Create blank object for the person
            indi_person = Individuals(gedcomline.ref)

            # set the values of the object UNTIL next level 0
            for gedcom_line in gedcom_list[index + 1:]:
                if gedcom_line.level == 0:
                    break
                if gedcom_line.tag == "NAME":
                    indi_person.name = gedcom_line.arg
                if gedcom_line.tag == "SEX":
                    indi_person.gender = gedcom_line.arg[0]
                if gedcom_line.tag == "BIRT":
                    date_of = "BIRT"
                #if gedcom_line.tag == "BIRT":
                 #   indi_person.age.append(gedcom_line.arg[0])
                if gedcom_line.tag == "DEAT":
                    date_of = "DEAT"
                if gedcom_line.tag == "FAMC":
                    indi_person.famc.append(gedcom_line.arg[0])
                if gedcom_line.tag == "FAMS":
                    indi_person.fams.append(gedcom_line.arg[0])

                # check if date is birth or date
                if gedcom_line.tag == 'DATE':
                    if date_of == 'BIRT':
                        indi_person.birthday = date(
                            int(gedcom_line.arg[2]),
                            datetime.strptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0])
                        )
                        today = date.today()
                        birthdate = indi_person.birthday.year
                        indi_person.age = today.year - birthdate
                        date_of = None
                    elif date_of == 'DEAT':
                        indi_person.death_date = date(
                            int(gedcom_line.arg[2]),
                            datetime.strptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0])
                        )
                        indi_person.alive = False
                        date_of = None

            # add object into the individual list
            individual.append(indi_person)

        # For family list
        if gedcomline.tag == 'FAM':

            date_of = None

            # create blank object
            fam_obj = Family(gedcomline.ref)

            # ste values until next level 0
            for gedcom_line in gedcom_list[index + 1:]:
                if gedcom_line.level == 0:
                    break
                if gedcom_line.tag == "MARR":
                    date_of = "MARR"
                if gedcom_line.tag == "DIV":
                    date_of = "DIV"
                if gedcom_line.tag == "HUSB":
                    fam_obj.husbandId = gedcom_line.arg[0]
                    for person in individual:
                        if person.IndId == gedcom_line.arg[0]:
                            fam_obj.husband_Name = person.name
                if gedcom_line.tag == "WIFE":
                    fam_obj.wifeId = gedcom_line.arg[0]
                    for person in individual:
                        if person.IndId == gedcom_line.arg[0]:
                            fam_obj.wife_Name = person.name
                if gedcom_line.tag == "CHIL":
                    fam_obj.children.append(gedcom_line.arg[0])

                # check if marriage date or divorce date
                if gedcom_line.tag == "DATE":
                    if date_of == "MARR":

                        fam_obj.marriage = date(
                            int(gedcom_line.arg[2]),
                            datetime.strptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0]))
                        date_of = None

                    elif date_of == "DIV":

                        fam_obj.divorced = date(
                            int(gedcom_line.arg[2]),
                            datetime.strptime(gedcom_line.arg[1], '%b').month,
                            int(gedcom_line.arg[0]))
                        date_of = None
            # append object into the family list
            family.append(fam_obj)

    return individual, family



#default file path

gedcom_file = 'C:/Devanshu/Python Project/DJEJ_family.ged'

indi = PrettyTable()
fam = PrettyTable()

# main function for taking the file path
def main():

    individual, families = GEDCOM_Reader(gedcom_file)

    #printing values
    Summary_tables(individual, families)

# function for printing the list of individuals and families to
def Summary_tables(individual, families):

    # for printing Individuals
    print()
    print("INDIVIDUAL TABLE")
    print()
    indi.field_names = ["id","Name","Birthday","Age","Gender","Death","Alive","Child","Spouse"]
    for line in individual:
        attrs = vars(line)
        indi.add_row(attrs.values())

    print(indi)
    print()
    print()
    print("FAMILY TABLE")
    print()
    # For prnting Families
    fam.field_names = ["Fid","Married","Husband","Husband Name","Wife","Wife Name","Children","Divorce"]
    for line in families:
        attrs = vars(line)
        fam.add_row(attrs.values())

    print(fam)

if __name__ == '__main__':
    sys.stdout = open("PR3-output.txt","w")
    main()
    sys.__stdout__.close()
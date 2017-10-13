import sys

from prettytable import PrettyTable
from PythonFiles.User_stories_Devanshu import birth_before_death, birth_before_marriage, child_before_marriage, unique_ids
from PythonFiles.GedcomReader import GEDCOM_Reader

#default file path
gedcom_file = 'C:/Devanshu/Python Project/Files/DJEJ_family.ged'

indi = PrettyTable()
fam = PrettyTable()

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

# main function for
def main():
    # Getting individual and family objects from gedcom_file.
    individual, families = GEDCOM_Reader(gedcom_file)
    print("ERROR MESSAGES")
    print()

    # printing user story errors.
    birth_before_marriage(individual, families) #US-02
    birth_before_death(individual) #US-03
    child_before_marriage(individual, families) #US-08
    unique_ids(individual,families) #US-22

    # printing values
    Summary_tables(individual, families)

if __name__ == '__main__':
    sys.stdout = open("PR3-output.txt","w")
    main()
    sys.__stdout__.close()
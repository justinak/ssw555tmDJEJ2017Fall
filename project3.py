

import sys

from prettytable import PrettyTable
from User_stories import GEDCOM_Reader, birth_before_death, birth_before_marriage


#default file path

gedcom_file = 'C:/Devanshu/Python Project/DJEJ_family.ged'

indi = PrettyTable()
fam = PrettyTable()

# main function for taking the file path
def main():

    individual, families = GEDCOM_Reader(gedcom_file)
    print("ERROR MESSAGES")
    print()
    birth_before_death(individual)
    birth_before_marriage(individual,families)

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


import sys

from prettytable import PrettyTable
from User_Stories_Justina import GEDCOM_Reader, marriage_age, less_than_150yrs
from User_stories import GEDCOM_Reader, birth_before_death, birth_before_marriage
from userStory16 import male_last_names
from userStory1 import dates_before_dates
#from UserStories import GEDCOM_Reader, checkIncest, check_genderrole

#default file path

gedcom_file = 'GedcomFamilyJS.ged'

indi = PrettyTable()
fam = PrettyTable()

# main function for taking the file path
def main():

    individual, families = GEDCOM_Reader(gedcom_file)
    print("ERROR MESSAGES")
    print()
    birth_before_death(individual)
    birth_before_marriage(individual,families)
    male_last_names(individual, families)
    dates_before_dates(individual,families)
   # checkIncest(families)
   # check_genderrole(individual,families)

    #printing values
    #Summary_tables(individual, families)

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
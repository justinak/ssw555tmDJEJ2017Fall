import sys

from prettytable import PrettyTable
from PythonFiles.User_stories_Devanshu import birth_before_death, birth_before_marriage, child_before_marriage, unique_ids, uniq_name_birthdate, uniq_family_names
from PythonFiles.User_stories_Erin import dates_before_dates, birth_before_death_of_parents, male_last_names, no_bigamy, sibling_spacing, multiple_births
from PythonFiles.User_Stories_Justina import marriage_age, living_single, living_married, less_than_150yrs, recent_births_deaths
from PythonFiles.UserStories_Jhustin import check_genderrole, checkIncest, marriage_before_death, marriage_before_divorce, divorce_before_death, illegitimate_date

from PythonFiles.GedcomReader import GEDCOM_Reader

#default file path
gedcom_file = '../Files/DJEJ_family_erin.txt'

indi = PrettyTable()
fam = PrettyTable()
# function for printing the list of individuals and families to
def Summary_tables(individual, families):

    # for printing Individuals
    print()
    print("INDIVIDUAL TABLE")
    print()
    indi.field_names = ["id", "Name", "Birthday", "Age", "Gender", "Death", "Alive", "Child", "Spouse"]
    for line in individual:
        attrs = vars(line)
        indi.add_row(attrs.values())

    print(indi)
    print()
    print()
    print("FAMILY TABLE")
    print()
    # For prnting Families
    fam.field_names = ["Fid", "Married", "Husband", "Husband Name", "Wife", "Wife Name", "Children", "Divorce"]
    for line in families:
        attrs = vars(line)
        fam.add_row(attrs.values())
    print(fam)

# main function
def main():
    # Getting individual and family objects from gedcom_file.
    individual, families = GEDCOM_Reader(gedcom_file)

    print("ERROR MESSAGES")
    print()

    # printing Devanshu's user story errors.
    birth_before_marriage(individual, families) #US-02
    birth_before_death(individual) #US-03
    child_before_marriage(individual, families) #US-08
    unique_ids(individual, families) #US-22
    uniq_name_birthdate(individual) #US-23
    uniq_family_names(individual, families) #US-25


    #printing Justina's user stories
    less_than_150yrs(individual) #US-7
    marriage_age(individual, families) # US-10
    living_married(individual) #US-30
    living_single(individual) #US-31
    recent_births_deaths(individual) #US-35,36

    # printing Erin's user story errors.
    dates_before_dates(individual, families) #US-1
    birth_before_death_of_parents(individual, families) #US-9
    no_bigamy(individual, families) #US-11
    male_last_names(individual, families)  # US-16
    sibling_spacing(individual, families) #US-13
    multiple_births(individual, families) #US-14

    #printing Jhustin's user stories
    marriage_before_divorce(families)  # US-4
    marriage_before_death(individual, families)  # US-5
    checkIncest(families)  # US-18
    check_genderrole(individual, families)  # US-21
    divorce_before_death(individual, families) # US-6
    illegitimate_date(individual, families) #US-42

    # printing values from gedcom_file
    Summary_tables(individual, families)


if __name__ == '__main__':
    sys.stdout = open("../Files/DJEJ_Output.txt","w")
    main()
    sys.__stdout__.close()
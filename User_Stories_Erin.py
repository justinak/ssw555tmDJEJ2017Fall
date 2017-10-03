import unittest
from GIF_classes import GedLine, Individuals, Family

from datetime import date
from datetime import datetime



gedcom_file = 'GedcomFamilyJS.ged'


# Function to Parse the GEDCOM file
def GEDCOM_Reader(gedcom_file):
    individual = []
    family = []
    gedcom_list = []

    # read each line from file and strip \n from the last
    File = open(gedcom_file)
    lines = [line.rstrip('\n\r') for line in File]

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
                #if gedcom_line.tag == "BIRT":
                    #date_of = "BIRT"
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
    File.close()
    return individual, family
#user story 1, dates before dates
def dates_before_dates(individuals, family):
    current_date = date.today()
    ind_bad_bday = []
    ind_bad_death = []
    fam_bad_marr = []
    fam_bad_div = []
    for ind_obj in individuals:
        print(ind_obj.birthday)
        if (ind_obj.birthday != None):
            if ind_obj.birthday > current_date:
                print('Error: ' + ind_obj.IndId + ' Birthday before current date')
                ind_bad_bday += [ind_obj.IndId]
        if (ind_obj.death_date != None):
            if ind_obj.death_date > current_date:
                print('Error: ' + ind_obj.IndId + ' Deathday before current date')
                ind_bad_death += [ind_obj.IndId]

    for fam_obj in family:
        if fam_obj.marriage != None:
            if fam_obj.marriage > current_date:
                print('Error: ' + fam_obj.famId + ' Marriage date before current date')
                fam_bad_marr += [fam_obj.famId]
        if fam_obj.divorce_date != None:
            if (fam_obj.divorce_date != None):
                if fam_obj.divorce_date > current_date:
                    print('Error: ' + fam_obj.famId + ' Divorce date before current date')
                    fam_bad_div += [fam_obj.famId]
    return [ind_bad_bday, ind_bad_death, fam_bad_marr, fam_bad_div]

#User story 16, male last names

def male_last_names(inds, fams):
    for ind in inds:
        if ind.gender == "M":
            if len(ind.famc) > 0:
                for famc in ind.famc:
                    for fam in fams:
                        if fam.famId == famc:
                            if not ind.name[1] == fam.husband_Name[1]:
                                print("('US16', 'Sons' last names should match father's', " + ind.IndId + ")")
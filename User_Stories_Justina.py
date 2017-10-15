import unittest
from GIF_classes import GedLine, Individuals, Family

from datetime import date
from datetime import datetime



gedcom_file = 'C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged'


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
                if gedcom_line.tag == "BIRT":
                    date_of = "BIRT"
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


def marriage_age(individuals, families):
    """ User Story 10 - Marriage after 14"""
    for fam in families:
        if fam.marriage:
            husbandId = None
            wifeId = None
            
            for indis in individuals:
                if indis.IndId == fam.husbandId:
                    husbandId = indis
                if indis.IndId == fam.wifeId:
                    wifeId = indis
                    
            if fam.marriage.year - husbandId.birthday.year <= 14:
                location = [husbandId.IndId]
                print('ERROR: FAMILY: US10:', location,':Marriage before age 14')
                
            if fam.marriage.year - wifeId.birthday.year <= 14:
                location = [wifeId.IndId]
                print('ERROR: FAMILY: US10:', location,':Marriage before age 14')
                    
def less_than_150yrs(individuals):
    """ User Story 07 - Less Than 150 years"""
    for indis in individuals:
        if indis.age > 150:
            location = [indis.IndId] 
            print('ERROR: FAMILY: US07:', location,':Age should be less than 150')
            
def living_married(individuals):
    married_indis = [ ]
    for indis in individuals:
        if indis.alive == True and indis.fams == True:
            married_indis.append(indis.name)
    print('US30: Married people: ',married_indis)
    
def living_single(individuals):
    single_indis = [ ]
    for indis in individuals:
        if indis.alive == True and indis.age > 30 and indis.fams == False:
            single_indis.append(indis.name)
    print('US31: Living single individuals: ',single_indis)



class TestStories(unittest.TestCase):
    
    def test_one_marriage_age(self):
        """ Test that marriage occurred after age 14 for individuals that are married """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F1@ family marriage occurred after age 14')
        
    def test_two_marriage_age(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F2@ family marriage occurred after age 14')
        
    def test_three_marriage_age(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(marriage_age(indis, fam), 'ERROR: FAMILY: US10: @F7@: Marriage before age 14', 'Wife and Husband in @F7@ family marriage occurred after age 14')
        
    def test_four_marriage_age(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F5@ family marriage occurred after age 14')
        
    def test_five_marriage_age(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        with self.assertRaises(NameError):
           marriage_age(42, family)
           
    def test_lessthan150yrs(self):
        """ Test that age is less than 150 years """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(less_than_150yrs(indis), indis,' older than 150 years')
        
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
    marriage_age()
    less_than_150yrs()
    living_married()
    living_single()




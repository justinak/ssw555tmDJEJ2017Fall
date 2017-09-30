import unittest
from GIF_classes import GedLine, Individuals, Family

from datetime import date
from datetime import datetime



error_locations = []

gedcom_file = 'C:/Devanshu/Python Project/DJEJ_family.ged'
#US03 - Birth should occur before death of an individual



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


# User Story 2
# Birth before Marriage

def birth_before_marriage(individuals, families):

    US02_flag = True
    Story_name = "US02"
    for fam in families:
        if fam.marriage:
            husbandId = None
            wifeId = None

            for indis in individuals:
                if indis.IndId == fam.husbandId:
                    husbandId = indis
                if indis.IndId == fam.wifeId:
                    wifeId = indis

            if wifeId.birthday > fam.marriage:
                # Found a case spouse marries before birthday
                error_msg = "Wife is born after marriage."
                location = [wifeId.IndId]
                error = (Story_name, error_msg, location)
                print(error)
                US02_flag = False

            if husbandId.birthday > fam.marriage:
                error_msg = "Husband is born after marriage."
                location = [husbandId.IndId]
                error = (Story_name, error_msg, location)
                print(error)
                US02_flag = False

        return US02_flag

# User Story 3
# Birth should occur before death of the individual member


def birth_before_death(individuals):

    US03_flag = True
    Story_name = "US03"
    for indis in individuals: # getting the values of object of individual class from original file project3
        if indis.death_date and indis.birthday:
            if indis.death_date < indis.birthday: # If line "if indis.death_date and indis.birthday:" is not written
                                                  #  then the "<" is not allowed to execute between an instance of
                                                  # none type and an instance of datetime.date.
                error_msg = "Birth should occur before death."
                location = [indis.IndId] # gives ID location where the error occurs
                error = (Story_name,error_msg,location)
                print(error)

                US03_flag = False
    return US03_flag

class TestUserStories(unittest.TestCase):

    def test_us03_01(self):
        indis, _ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(birth_before_death(indis), False)
        print("Test case 1 passed")


    def test_us03_02(self):
        indis, _ = GEDCOM_Reader(gedcom_file)
        self.assertEqual(birth_before_death(indis), True)
        print("Test case 2 passed")

    def test_us03_03(self):
        indis, _ = GEDCOM_Reader(gedcom_file)
        self.assertTrue(birth_before_death(indis))
        print("Test case 3 passed")

    def test_us03_04(self):
        indis, _ = GEDCOM_Reader(gedcom_file)
        self.assertIs(birth_before_death(indis ),True)
        print("Test case 4 passed")

    def test_us03_05(self):
        indis, _ = GEDCOM_Reader(gedcom_file)
        self.assertIsNotNone(birth_before_death(indis))
        print("Test case 5 passed")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
    birth_before_death()



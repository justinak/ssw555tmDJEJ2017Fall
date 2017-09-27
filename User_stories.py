"""
User Story 3
Birth should occur before death of the individual member
"""

import unittest
from project3 import GEDCOM_Reader


error_locations = []
gedcom_file = 'C:/Devanshu/Python Project/DJEJ_family.ged'

#US03 - Birth should occur before death of an individual

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
    error = (birth_before_death.Story_name, birth_before_death.error_msg, birth_before_death.location)
    print(error)



import unittest
from PythonFiles.GedcomReader import GEDCOM_Reader
from PythonFiles.User_stories_Devanshu import birth_before_death, birth_before_marriage, unique_ids, child_before_marriage

#Default path of Gedcom file.
gedcom_file = 'C:/Devanshu/Python Project/Files/DJEJ_family.ged'

class TestUserStories(unittest.TestCase):

    def test_us03(self):
        indis, _ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(birth_before_death(indis), False)
        print("Test case 1 passed")

    def test_us02(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertTrue(birth_before_marriage(indis, fam))
        print("US02 testcase passed")

    def test_us08(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertTrue(child_before_marriage(indis, fam))
        print("US08 testcase passed")

    def test_us22(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertTrue(unique_ids(indis, fam))
        print("US22 testcase passed")

    def test_us23(self):
        indis,  = GEDCOM_Reader(gedcom_file)
        self.assertTrue(unique_ids(indis))
        print("US23 testcase passed")

    def test_us25(self):
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertTrue(unique_ids(indis, fam))
        print("US25 testcase passed")

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
    birth_before_death()

import sys
import unittest
from User_Stories_Justina import marriage_age, less_than_150yrs, living_married, living_single
from GedReaderJustina import GEDCOM_Reader
from GIF_classes import GedLine, Individuals, Family

class TestStories(unittest.TestCase):
    
    def test_one_marriage_age(self):
        """ Test that marriage occurred after age 14 for individuals that are married """
        indis, fam = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F1@ family marriage occurred after age 14')
        
    def test_two_marriage_age(self):
        indis, fam = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F2@ family marriage occurred after age 14')
        
    def test_three_marriage_age(self):
        indis, fam = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertNotEqual(marriage_age(indis, fam), 'ERROR: FAMILY: US10: @F7@: Marriage before age 14', 'Wife and Husband in @F7@ family marriage occurred after age 14')
        
    def test_four_marriage_age(self):
        indis, fam = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F5@ family marriage occurred after age 14')
        
    def test_five_marriage_age(self):
        indis, fam = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        with self.assertRaises(NameError):
           marriage_age(42, family)
           
    def test_lessthan150yrs(self):
        """ Test that age is less than 150 years """
        indis,_ = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertNotEqual(less_than_150yrs(indis), indis,' older than 150 years')
        
    def test_living_single(self):
        indis,_ = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertNotEqual(living_single(indis), False)
        print("US31 test passed")
        
    def test_living_married(self):
        indis,_ = GEDCOM_Reader('C:/Users/jkope/Documents/Stevens-Software Engineering Masters/SSW 555 - Agile Methods for Software Development/Fall 2017/Project Related Documents/DJEJ_family_test.ged')
        self.assertNotEqual(living_married(indis), False)
        print("US30 test passed")
        
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)

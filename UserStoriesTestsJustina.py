import sys
import unittest
from User_Stories_Justina import marriage_age, less_than_150yrs, living_married, living_single, recent_births_deaths, upcoming_births_anniversaries
from GedReaderJustina import GEDCOM_Reader
from GIF_classes import GedLine, Individuals, Family

class TestStories(unittest.TestCase):
    
    def test_one_marriage_age(self):
        """ Test that marriage occurred after age 14 for individuals that are married """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F1@ family marriage occurred after age 14')
        
    def test_two_marriage_age(self):
        """ Test that marriage occurred after age 14 for individuals that are married """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F2@ family marriage occurred after age 14')
        
    def test_three_marriage_age(self):
        """ Test that marriage occurred after age 14 for married individuals """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(marriage_age(indis, fam), 'ERROR: FAMILY: US10: @F7@: Marriage before age 14', 'Wife and Husband in @F7@ family marriage occurred after age 14')
        
    def test_four_marriage_age(self):
        """ Test that marriage occurred after age 14 for married individuals """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(marriage_age(indis, fam), None, 'Wife and Husband in @F5@ family marriage occurred after age 14')
        
    def test_five_marriage_age(self):
        """  Test the proper input is used in marriage age function """
        indis, fam = GEDCOM_Reader(gedcom_file)
        with self.assertRaises(NameError):
           marriage_age(42, family)
           
    def test_lessthan150yrs(self):
        """ Test that age is less than 150 years """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertEqual(less_than_150yrs(indis), "ERROR: FAMILY: US07: ['@I2@'] :Age should be less than 150", '@I2@ age should be less than 150 yrs')
        
    def test_lessthan150yrs(self):
        """ Test that age is less than 150 years """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(less_than_150yrs(indis), "ERROR: FAMILY: US07: ['@I1@'] :Age should be less than 150", '@I1@ age is less than 150 yrs')
        
    def test_living_single(self):
        """ Test printing living single people in the family """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertEqual(living_single(indis), "ERROR: US31: Living single individuals:  ['Antoinette', '/Moore/']", 'Antoinette Moore is a living, single individual')
            
    def test_living_single(self):
        """ Test printing living single people in the family """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(living_single(indis), "ERROR: US31: Living single individuals:  ['Jenita', '/Drummond/']", 'Jenita Drummond is a living, not single individual')
        
    def test_living_married(self):
        """ Test printing living married people in the family """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertEqual(living_married(indis), "ERROR: US30: Married people:  ['Mary', '/Scarlett/']", 'Mary Scarlett is a living, married individual')
        
    def test_living_married(self):
        """ Test printing living married people in the family """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(living_married(indis), "ERROR: US30: Married people:  ['Chadwick', '/Nelson/']", 'Chadwick Nelson is a living, not married individual')
        
    def test_recentbirth(self):
        """ Test printing of individuals born in the last 30 days """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertEqual(recent_births_deaths(indis), "ERROR: US35: Recent births:  ['Marilyn', '/Monroe/']", 'Marilyn Monroe was born in the last 30 days')
        
    def test_recentbirth(self):
        """ Test printing of individuals born in the last 30 days """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(recent_births_deaths(indis), "ERROR: US35: Recent births:  ['Dillon', '/Nelson/']", 'Dillon Nelson was not born in the last 30 days')
    
    def test_recentdeath(self):
        """ Test printing of individuals died in the last 30 days """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertEqual(recent_births_deaths(indis), "US36: Recent deaths:  ['George', '/Washington/']", 'George Washington died in the last 30 days')    
        
    def test_recentdeath(self):
        """ Test printing of individuals died in the last 30 days """
        indis,_ = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(recent_births_deaths(indis), "US36: Recent deaths:  ['Antoinette', '/Moore/']", 'Antoinette Moore did not die in the last 30 days')
        
    def test_upcomingbirth(self):
        """ Test printing of individuals with birth in the next 30 days """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(upcoming_births_anniversaries(indis, fam), "US38: Upcoming birthdays: ', ['Dillon', '/Nelson/']", 'Dillon Nelson has a birthday in the next 30 days')
        
    def test_upcomingbirth(self):
        """ Test printing of individuals with birth in the next 30 days """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertNotEqual(upcoming_births_anniversaries(indis, fam), "US38: Upcoming birthdays: ', ['Jenita', '/Drummond/']", 'Jenita Drummond does not have a birthday in the next 30 days')
        
    def test_upcominganniversary(self):
        """ Test printing of individuals with anniversary in the next 30 days """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(upcoming_births_anniversaries(indis, fam), "US39: Upcoming Anniversaries: ', ['George', '/Washington/'] and ['Martha', '/Washington/']", 'George & Martha Washington have an anniversary in the next 30 days')
        
    def test_upcominganniversary(self):
        """ Test printing of individuals with anniversary in the next 30 days """
        indis, fam = GEDCOM_Reader(gedcom_file)
        self.assertEqual(upcoming_births_anniversaries(indis, fam), "US39: Upcoming Anniversaries: ', ['Lennox', '/Nelson/'] and ['Jenita', '/Drummond/']", 'Lennox Nelson & Jenita Drummond do not have an anniversary in the next 30 days')
        
if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)

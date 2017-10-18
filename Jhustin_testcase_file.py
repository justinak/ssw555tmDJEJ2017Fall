import unittest
from PythonFiles.User_stories_Jhustin import checkIncest, check_genderrole, marriage_before_divorce, marriage_before_death
from PythonFiles.GedcomReader import GEDCOM_Reader

class Test_checkIncest(unittest.TestCase):
    # One sibling married another sibling
    def test_1(self):
        self.assertEqual(checkIncest(GEDCOM_Reader('Jhustin1.ged')[1]),
                         ('US18', 'Siblings cannot marry', ['@I1@', '@I11@']), 'This is incest')
        # Husband is a female

    def test_2(self):
        self.assertEqual(check_genderrole(*GEDCOM_Reader('Jhustin1.ged')),
                         ('US21', 'Gender role does not match', ['@I2@']), 'Should be fine')

    # Divorce happens before the date of marriage
    def test_3(self):
        self.assertEqual(marriage_before_divorce(GEDCOM_Reader('Jhustin1.ged')[1]),
                         ('US04', 'Marriage should occur before divorce', ['@I4@', '@I5@']), 'Should be fine')

    # Death happens before the date of marriage
    def test_4(self):
        self.assertEqual(marriage_before_death(*GEDCOM_Reader('Jhustin1.ged')),
                         ('US05', 'Marriage should occur before death', ['@I4@']), 'Should be fine')


if __name__ == '__main__':
    unittest.main()

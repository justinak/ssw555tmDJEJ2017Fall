"""
User Story 10
Marriage after 14

Marriage should be at least 14 years after birth of both spouses (parents must be at least 14 years old)

"""

import unittest

def marriage_age(famID):
    for fam_obj.famID in family:

        if gedcom_line.tag == "HUSB":
            fam_obj.husbandId = gedcom_line.arg[0]
            for person in individual:
                if person.IndId == gedcom_line.arg[0]:
                    fam_obj.husband_birthday = indi_person.birthday.year
                    if fam_obj.marriage.year - fam_obj.husband_birthday <= '14':
                        print('ERROR: FAMILY: US10:', fam_object.famID,':Marriage before age 14')
                    else:
                        pass
                        
        if gedcom_line.tag == "WIFE":
            fam_obj.wifeId = gedcom_line.arg[0]
            for person in individual:
                if person.IndId == gedcom_line.arg[0]:
                    fam_obj.wife_birthday = indi_person.birthday.year
                    if fam_obj.marriage.year - fam_obj.wife_birthday <= '14':
                        print('ERROR: FAMILY: US10:', fam_object.famID,': Marriage before age 14')
                    else:
                        pass
    
    
class TestMarriageAge(unittest.TestCase):
    
    def test_marriageage(self):
        """ Test that marriage occurred after age 14 for individuals that are married """
        self.assertEqual(marriage_age('@F1@'), None, 'Wife and Husband in @F1@ family marriage occurred after age 14')
        self.assertEqual(marriage_age('@F2@'), None, 'Wife and Husband in @F2@ family marriage occurred after age 14')
        self.assertEqual(marriage_age('@F5@'), None, 'Wife and Husband in @F5@ family marriage occurred after age 14')
        with self.assertRaises(NameError):
            marriage_age(42)
        self.assertNotEqual(marriage_age('@F7@'), 'ERROR: FAMILY: US10: @F7@: Marriage before age 14', 'Wife and Husband in @F7@ family marriage occurred after age 14')
        

if __name__ == '__main__':
    unittest.main(exit=False, verbosity=3)
    main()
        
    
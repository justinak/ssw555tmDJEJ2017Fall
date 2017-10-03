#testtttt
import unittest
from datetime import date
class Individuals(object):

    def __init__(self, IndId):
        self.IndId = IndId  #umoque id of individual person
        self.name = None # name of individual person
        self.birthday = None # Date of birthday of individual person
        self.age = None # Age of indvidual person
        self.gender = None # gender of individual person
        self.death_date = None # Date of death of individual person
        self.alive = True # person alive or dead
        self.famc = [] # family id where individual is a child
        self.fams = [] # family id where individual is parent

# class for families
class Family(object):

    def __init__(self, famId):
        self.famId = famId
        self.marriage = None  # marriage event for family
        self.husbandId = None  # for husband in family
        self.husband_Name = None # name of husband
        self.wifeId = None  # for wife in family
        self.wife_Name = None # for name of the wife
        self.children = []  # for child in family
        self.divorced = None  # divorce event in family
        self.divorce_date = None


class TestDatesBeforeDates(unittest.TestCase):
    def test_one_bad_death_one_bad_marr(self):
        i1 = Individuals("I01")
        i2 = Individuals("I02")
        i1.birthday = date(2015,5,17)
        i1.death_date = date(2020, 12, 1)
        i2.birthday = date(2012,6,19)
        individuals = [i1,i2]
        family1 = Family("F01")
        family1.marriage = date(2019,5,1)
        families = [family1]
        info = dates_before_dates(individuals=individuals, family=families)

        ind_bad_bday = info[0]
        ind_bad_death = info[1]
        fam_bad_marr = info[2]
        fam_bad_div = info[3]

        self.assertIn(i1.IndId,ind_bad_death)
        self.assertIn(family1.famId,fam_bad_marr)


#user story 1, dates before dates
def dates_before_dates(individuals, family):
    current_date = date.today()
    ind_bad_bday = []
    ind_bad_death = []
    fam_bad_marr = []
    fam_bad_div = []
    for ind_obj in individuals:
        if (ind_obj.birthday != None):
            if ind_obj.birthday > current_date:
                print('ERROR: INDIVIDUAL: US01: [' + ind_obj.IndId + '] :Birthday before current date')
                ind_bad_bday += [ind_obj.IndId]
        if (ind_obj.death_date != None):
            if ind_obj.death_date > current_date:
                print('ERROR: INDIVIDUAL: US01: [' + ind_obj.IndId + '] :Deathday before current date')
                ind_bad_death += [ind_obj.IndId]

    for fam_obj in family:
        if fam_obj.marriage != None:
            if fam_obj.marriage > current_date:
                print('ERROR: FAMILY: US01: [' + fam_obj.famId + '] :Marriage date before current date')
                fam_bad_marr += [fam_obj.famId]
       #if fam_obj.divorce_date != None:
            #if (fam_obj.divorce_date != None):
                #if fam_obj.divorce_date > current_date:
                    #print('Error: ' + fam_obj.famId + ' Divorce date before current date')
                    #fam_bad_div += [fam_obj.famId]
    return [ind_bad_bday, ind_bad_death, fam_bad_marr, fam_bad_div]


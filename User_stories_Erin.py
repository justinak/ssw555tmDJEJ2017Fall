from datetime import date, datetime, timedelta
import unittest

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
     return [ind_bad_bday, ind_bad_death, fam_bad_marr, fam_bad_div]

# US09 - Birth before death of parents
def birth_before_death_of_parents(individuals, families):
    US09_flag = True
    error_type = "US09"

    for ind in individuals:

        if len(ind.famc) > 0:
            father = None
            father_id = None
            mother = None
            mother_id = None
            fam = None

            # Get the ID of parents for an individual
            for family in families:
                if family.famId == ind.famc[0]:
                    father_id = family.husbandId
                    mother_id = family.wifeId
                    fam = family
                    break

            # Get the ID of individuals
            for ind in individuals:
                if ind.IndId == father_id:
                    father = ind
                if ind.IndId == mother_id:
                    mother = ind

            if father.death_date is not None and father.death_date < ind.birthday - timedelta(days=266):
                error_location = [fam.famId, ind.IndId]
                print('ERROR: FAMILY : US9: [' + fam.famId + ' , ' + ind.IndId + '] : Born before parents death day ')
                US09_flag = False

            if mother.death_date is not None and mother.death_date < ind.birthday:
                error_location = [fam.uid, ind.uid]
                print('ERROR: FAMILY : US9: [' + ind.IndId + '] : Born before parents death day ')
                US09_flag = False
    return US09_flag


#user story 11, no bigamy
def no_bigamy(individuals, family):
    for ind in individuals:
        marriages = 0
        for f in family:
            if f.husbandId == ind.IndId and currently_married(f, individuals):
                marriages += 1
            elif f.wifeId == ind.IndId and currently_married(f,individuals):
                marriages += 1
        if marriages > 1:
            print('ERROR: FAMILY: US11: ' + ind.name[0] + " is married more to more than one person")

def currently_married(family, individuals):
    if family.divorced != None:
        return False
    hus_id = family.husbandId
    wife_id = family.wifeId
    husband = None
    wife = None
    for i in individuals:
        if wife_id == i.IndId:
            wife = i
        elif hus_id == i.IndId:
            husband = i
    if husband.death_date != None:
        return False
    if wife.death_date != None:
        return False
    return True

#User story 16, male last names
def male_last_names(individuals, family):
    for ind in individuals:
        if ind.gender == "M":
            if len(ind.famc) > 0:
                for famc in ind.famc:
                    for fam in family:
                        if fam.famId == famc:
                            if not ind.name[1] == fam.husband_Name[1]:
                                print('ERROR: FAMILY : US16: [' + ind.IndId + '] :Sons last names should match fathers ')
#User story 13, sibling spacing
def sibling_spacing(individuals, family):
    error_messages = []
    for single_family in family:
        siblings = []
        siblings_strs = single_family.children
        for ind in individuals:
            if ind.IndId in siblings_strs:
                siblings += [ind]
        incorrect_spacings = []
        for person in siblings:
            person_bday = person.birthday
            for sib in siblings:
                date_diff = person_bday-sib.birthday
                if (date_diff < timedelta(days=30*8) and date_diff > timedelta(days=2)):
                    print("Error: US 13: " + person.IndId + " and " + sib.IndId + " are spaced incorrectly")
                    error_messages += ["Error: US 13: " + person.IndId + " and " + sib.IndId + " are spaced incorrectly"]
    return error_messages

#User story 14, multiple births
def multiple_births(individuals, family):
    error_messages = []
    for single_family in family:
        siblings = []
        siblings_strs = single_family.children
        birthdays = []
        occurences = []
        for ind in individuals:
            if ind.IndId in siblings_strs:
                siblings += [ind]
        for sib in siblings:
            if sib.birthday in birthdays:
                index = birthdays.index(sib.birthday)
                occurences[index] += 1
            else:
                birthdays += [sib.birthday]
                occurences += [1]
        for x in occurences:
            if x > 5:
                error_messages += ["Error US14: Too many births at once in " + single_family.famId]
                print("Error US14: Too many births at once in " + single_family.famId)
    return error_messages

class TestStories(unittest.TestCase):

    def test_sibling_spacing(self):
        ind1 =  Individuals("1")
        ind1.birthday = datetime(day=5,month=5,year=1999)
        ind2 = Individuals("2")
        ind2.birthday = datetime(day=5,month=6,year=1999)
        family = Family("f1")
        family.children = [ind1.IndId,ind2.IndId]
        errors = sibling_spacing([ind1,ind2],[family])
        self.assertTrue(errors==["Error: US 13: " + ind1.IndId + " and " + ind2.IndId + " are spaced incorrectly"] or errors==["Error: US 13: " + ind2.IndId + " and " + ind1.IndId + " are spaced incorrectly"])
    def test_multiple_births(self):
        ind1 =  Individuals("1")
        ind1.birthday = datetime(year=1999, month=5, day=5)
        ind2 = Individuals("2")
        ind2.birthday = datetime(year=1999, month=5, day=5)
        ind3 = Individuals("3")
        ind3.birthday = datetime(year=1999, month=5, day=5)
        ind4 = Individuals("4")
        ind4.birthday = datetime(year=1999, month=5, day=5)
        ind5 = Individuals("5")
        ind5.birthday = datetime(year=1999, month=5, day=5)
        ind6 = Individuals("6")
        ind6.birthday = datetime(year=1999, month=5, day=5)
        family = Family("F1")
        family.children = [ind1.IndId,ind2.IndId,ind3.IndId,ind4.IndId,ind5.IndId,ind6.IndId]
        errors = multiple_births([ind1,ind2,ind3,ind4,ind5,ind6],[family])
        self.assertEquals(errors,["Error US14: Too many births at once in " + family.famId])



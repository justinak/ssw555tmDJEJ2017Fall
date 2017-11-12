from datetime import date, datetime, timedelta

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
                print('ERROR: FAMILY: US10:', location, ':Marriage before age 14')

            if fam.marriage.year - wifeId.birthday.year <= 14:
                location = [wifeId.IndId]
                print('ERROR: FAMILY: US10:', location, ':Marriage before age 14')


def less_than_150yrs(individuals):
    """ User Story 07 - Less Than 150 years"""
    for indis in individuals:
        if indis.age > 150:
            location = [indis.IndId]
            print('ERROR: FAMILY: US07:', location, ':Age should be less than 150')

def living_married(individuals):
    """ User Story 30 - List all living married people """
    for indis in individuals:
        if indis.alive == True:
            spouse = indis.fams
            if spouse:
                married_indis = indis.name
                print('ERROR: US30: Married people: ',married_indis)

def living_single(individuals):
    """ User Story 31 - List all living single people """
    for indis in individuals:
        if indis.alive == True and indis.age > 30:
            spouse = indis.fams
            if not spouse:
                single_indis = indis.name
                print('ERROR: US31: Living single individuals: ',single_indis)
                
def recent_births_deaths(individuals):
    """US 35: List recent births 
    List all people in a GEDCOM file who were born in the last 30 days
    US 36: List recent deaths
    List all people in a GEDCOM file who died in the last 30 days"""
    for indis in individuals:
        indis_recent_birth = date.today() - indis.birthday
        if (timedelta(days=30)) >= indis_recent_birth:
            recent_born_indis = indis.name
            print('ERROR: US35: Recent births: ', recent_born_indis)
        elif indis.death_date != None:
            indis_recent_death = date.today() - indis.death_date
            if (timedelta(days=30)) >= indis_recent_death:
                recent_death_indis = indis.name
                print('ERROR: US36: Recent deaths: ', recent_death_indis)
    
def upcoming_births_anniversaries(individuals, families):
    """US 38: List upcoming birthdays
    List all living people in a GEDCOM file whose birthdays occur in the next 30 days
    US 39: List upcoming anniversaries
    List all living couples in a GEDCOM file whose marriage anniversaries occur in the next 30 days"""
    d1 = date.today() # find today's date
    d2 = date.today() + timedelta(days=30) # find 30 days from today
    for indis in individuals:
        if indis.birthday in range(d1, d2 + 1): # check in birthday in next 30 days
            upcoming_birth = indis.name # find name of person if it is
            print('US38: Upcoming birthdays: ', upcoming_birth)   
    for fam in families:
        if fam.marriage != None and fam.marriage in range(d1, d2 + 1): # if person is married and marriage date is in the next 30 days
            upcoming_anni_husband = fam.husband_Name # find name of husband who has anniversary
            upcoming_anni_wife = fam.wife_Name # find name of wife who has anniversary
            print('US39: Upcoming Anniversaries: ', upcoming_anni_husband, 'and', upcoming_anni_wife)

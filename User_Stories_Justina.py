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
                print('US30: Married people: ',married_indis)

def living_single(individuals):
    """ User Story 31 - List all living single people """
    for indis in individuals:
        if indis.alive == True and indis.age > 30:
            spouse = indis.fams
            if not spouse:
                single_indis = indis.name
                print('US31: Living single individuals: ',single_indis)
                
def recent_births_deaths(individuals):
    """US 35: List recent births 
    List all people in a GEDCOM file who were born in the last 30 days
    US 36: List recent deaths
    List all people in a GEDCOM file who died in the last 30 days
    """
    for indis in individuals:
        date_30_days_ago = datetime.now() - timedelta(days=30)
        indis_recent_birth = datetime.now() - indis.birthday
        indis_recent_death = datetime.now() - indis.death_date
        if date_30_days_ago >= indis_recent_birth:
            recent_born_indis = indis.name
            print('US35: Recent births: ', recent_born_indis)
        elif date_30_days_ago >= indis_recent_death:
            recent_death_indis = indis.name
            print('US36: Recent deaths: ', recent_death_indis)

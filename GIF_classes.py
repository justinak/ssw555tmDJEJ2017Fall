
validTags = ['NAME', 'SEX', 'FAMS', ' FAMC', 'MARR', 'BIRT', 'WIFE', 'HUSB', 'CHIL', 'DEAT', 'DIV', 'DATE', 'HEAD','TRLR', 'NOTE',
             'INDI', 'FAM']

# class for every gedcom tag line
class GedLine(object):

    def __init__(self, line):
        self.level = None
        self.tag = None
        self.arg = None
        self.ref = None

        list_Line = line.split(' ',)
        # set level of the object
        self.level = int(list_Line[0])

        # for setting tag and argument
        if self.level > 0:
            self.tag = list_Line[1]
            self.arg = list_Line[2:]

        if self.level == 0:
            if list_Line[1] in validTags:
                self.tag = list_Line[1]
                self.arg = None
            else:
                self.tag = list_Line[2]
                self.ref = list_Line[1]


# class for individual persons
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


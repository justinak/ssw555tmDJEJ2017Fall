#Declaring the data-structure where the location of error will be stored.
import collections
error_locations = []

#Default path of Gedcom file.
gedcom_file = 'C:/Devanshu/Python Project/Files/DJEJ_family.ged'

# User Story 2: Birth should occur before Marriage.
def birth_before_marriage(individuals, families):

    US02_flag = True
    Story_name = "US02"
    for fam in families:
        if fam.marriage:
            husbandId = None
            wifeId = None

            for indis in individuals:
                if indis.IndId == fam.husbandId:
                    husbandId = indis
                if indis.IndId == fam.wifeId:
                    wifeId = indis

            if wifeId.birthday.year > fam.marriage.year:
                # Found a case spouse marries before birthday
                error_msg = "Wife is born after marriage."
                location = [wifeId.IndId]
                print("ERROR: INDIVIDUAL: " + Story_name + ": [" + wifeId.IndId + "] : " + error_msg)
                US02_flag = False

            if husbandId.birthday > fam.marriage:
                error_msg = "Husband is born after marriage."
                location = [husbandId.IndId]
                print("ERROR: INDIVIDUAL: " + Story_name + ": [" + husbandId.IndId + "] : " + error_msg)
                US02_flag = False

        return US02_flag

# User Story 3: Birth should occur before death of the individual member
def birth_before_death(individuals):

    US03_flag = True
    Story_name = "US03"
    error_msg = "Birth should occur before death."
    for indis in individuals: # getting the values of object of individual class from original file project3
        if indis.death_date and indis.birthday:
            if indis.death_date < indis.birthday: # If line "if indis.death_date and indis.birthday:" is not written
                                                  #  then the "<" is not allowed to execute between an instance of
                                                  # none type and an instance of datetime.date.
                location = [indis.IndId] # gives ID location where the error occurs
                print("ERROR: INDIVIDUAL: " + Story_name + ": [" + indis.IndId + "] : " + error_msg)

                US03_flag = False
    return US03_flag

#User Story 8: Children should be born after marriage of parents.
def child_before_marriage(individuals, families):
    US08_flag = True
    Story_name = "US08"
    for fam in families:
        if fam.marriage:
            for indis in individuals:
                id = indis.IndId
                bday = indis.birthday
                if id in fam.children: #Checking for Individual IDs present in Children column of family table.
                    if bday.year < fam.marriage.year:
                        error_msg = "Child born before marriage of parents"
                        error_location = [indis.IndId]
                        print("ERROR: INDIVIDUAL: " + Story_name + ": [" + indis.IndId + "] : " + error_msg)
                        US08_flag = False
    return US08_flag

#User Story 22: Unique ID's
def unique_ids(individuals,families):

    US22_flag = True
    Story_name = "US22"
    error_msg = "ID already exists"
    unique_id = []
    exist = set()
    unique = set()
    for indis in individuals:
        unique_id.append(indis.IndId)
    for fam in families:
        unique_id.append(fam.famId)
    for x in unique_id:
        if x not in exist:
            exist.add(x)
        else:
            unique.add(x)

    for y in unique:
        print("ERROR: FAMILY: " + Story_name + ": [" + y + "] : " + error_msg)
        US22_flag = False

    return US22_flag

#User Story 23: Unique name and Birthdate
def uniq_name_birthdate(individuals):
    Story_name = "US23"
    US23_flag = True
    unique = set()
    repeat = set()
    for individual in individuals:
        id = str(individual.name) + " " + str(individual.birthday)
        if id in unique:
            repeat.add(id)
        else:
            unique.add(id)
    for item in repeat:
        print()
        print("ERROR: INDIVIDUAL: " + Story_name + ": " + id + " occurs more than once")
        US23_flag = False
    return US23_flag

#User Story 25: Unique first names in families
def uniq_family_names(individuals,families):
    Story_name = "US25"
    US25_flag = True
    for fam in families:
        if fam.marriage is not None:
            if len(fam.children) != 0:
                exist = set()
                unique = set()
                Child_Id= fam.children
                for indis in individuals:
                    indis_name = indis.name
                    if indis.IndId in Child_Id:
                        if str(indis_name) not in exist:
                            exist.add(str(indis_name))
                        else:
                            unique.add(str(indis_name))
                for y in unique:
                    error_msg = "Child-Name is not unique"
                    print("ERROR: FAMILY: " + Story_name + ": " + str(y) + " : " + error_msg)
                    US25_flag = False
            else:
                pass

    return US25_flag
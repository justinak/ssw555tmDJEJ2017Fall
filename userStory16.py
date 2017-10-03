#User story 16, male last names

def male_last_names(inds, fams):
    for ind in inds:
        if ind.gender == "M":
            if len(ind.famc) > 0:
                for famc in ind.famc:
                    for fam in fams:
                        if fam.famId == famc:
                            if not ind.name[1] == fam.husband_Name[1]:
                                print('ERROR: FAMILY : US16: [' + ind.IndId + '] :Sons last names should match fathers ')
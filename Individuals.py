import  sys

def individuals():
    with open('C:/Users/devan/Downloads/ssw555tmDJEJ2017Fall-master/ssw555tmDJEJ2017Fall-master/DJEJ_family.ged') as i:
        for line in i:
            list_indi = line.split()  # it will split line and assign each word in it to the particular index of list

            try:
                if list_indi[2] == 'INDI':
                    list_id = list_indi[1]
                    print(list_id)

                elif  list_indi[1] == 'NAME':
                    list_name = list_indi[2] + list_indi[3]
                    print(list_name)

                elif list_indi[1] == 'SEX':
                    list_gen = list_indi[2]
                    print(list_gen)

                elif list_indi[1] == 'FAMC':
                     list_childof = list_indi[2]
                     print("Child of : ",list_childof)

                elif list_indi[1] == 'FAMS':
                    list_parentof = list_indi[2]
                    print("Parent in : ",list_parentof)
                elif list_indi[1] == 'DATE':
                    print(list_indi[2]," ",list_indi[3]," ",list_indi[4])

            except IndexError:
                print()

if __name__ == '__main__':
    sys.stdout = open("Individuals.txt","w")
    individuals()
    sys.__stdout__.close()


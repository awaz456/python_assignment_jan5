class CheckError():
    def __init__(self,roll):
        if(roll>24):
            raise NameError()

dict = {
    1: "student1",
    2: "student2"
}
option = 1
while (option==1):
    try:
        option = int(input("choose an option"))
        if (option == 1):
            roll = int(input("roll no:"))
            name = input("name: ")
            CheckError(roll)
            dict.update({roll: name})
        elif (option == 2):
            roll = int(input("roll no.: "))
            print(dict[roll])
        elif (option == 3):
            del dict
    except KeyError:
        print("Roll no. does not exist")
    except NameError:
        print("cannot accomadate more than 24 students")
    except ValueError:
        print("enter an ingteger roll no.")
    except TypeError:
        print("students list doesnot exist")
    else:
        print("Error occured")
    finally:
        loop = input("would you like to continue? (yes/no)")
        if(loop == "yes"):
            option=1
        else:
            option=0

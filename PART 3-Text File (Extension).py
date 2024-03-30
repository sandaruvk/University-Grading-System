#I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20220054
# Date : 22.11.2022


# Initializing variables

progress = []
module_trailer = []
module_retriever = []
exclude = []
mark_list = []
allData = []
progress_count = 0
module_t_count = 0
exclude_count = 0
module_r_count = 0


def marking_process(pass_marks, defer_marks, fail_marks):
    global progress_count, module_t_count, exclude_count, module_r_count
    global progress, module_trailer, exclude, module_retriever

    if pass_marks == 120:
        print('Progression Outcome :', 'Progress')
        marks_list = [pass_marks, defer_marks, fail_marks]
        progress.append(marks_list)
        progress_count += 1

    elif pass_marks >= 100:
        print('Progression Outcome :', 'Progress – module trailer')
        marks_list = [pass_marks, defer_marks, fail_marks]
        module_trailer.append(marks_list)
        module_t_count += 1

    elif fail_marks >= 80:
        print('Progression Outcome :', 'Exclude')
        marks_list = [pass_marks, defer_marks, fail_marks]
        exclude.append(marks_list)
        exclude_count += 1

    else:
        print('Progression Outcome :', 'Do not progress – module retriever')
        marks_list = [pass_marks, defer_marks, fail_marks]
        module_retriever.append(marks_list)
        module_r_count += 1

    print("\n")


def addDataToArray():

    for data in progress:
        temp = str(data)
        allData.append("Progress = " + temp)
    for data in module_trailer:
        temp = str(data)
        allData.append("Progress (module trailer) = " + temp)
    for data in module_retriever:
        temp = str(data)
        allData.append("Module retriever = " + temp)
    for data in exclude:
        temp = str(data)
        allData.append("Exclude = " + temp)


def printData():
    for data in progress:
        temp = str(data)
        print("Progress = " + temp)
    for data in module_trailer:
        temp = str(data)
        print("Progress (module trailer) = " + temp)
    for data in module_retriever:
        temp = str(data)
        print("Module retriever = " + temp)
    for data in exclude:
        temp = str(data)
        print("Exclude = " + temp)

    print("\n")


def validation(pass_marks, defer_marks, fail_marks):
    if pass_marks + defer_marks + fail_marks == 120:

        if pass_marks % 20 != 0:
            print('Out of range')
        elif defer_marks % 20 != 0:
            print('Out of range')
        elif fail_marks % 20 != 0:
            print('Out of range')
        else:
            marking_process(pass_marks, defer_marks, fail_marks)  # marking_process function

    else:
        print('Total incorrect')


def histrogram():
    global progress, module_trailer, module_retriever, exclude
    global progress_count, module_t_count, exclude_count, module_r_count

    print("---------------------------------------------------------------------------")
    print("Progress", progress_count, ":", "*" * progress_count)
    print("Trailer ", module_t_count, ":", "*" * module_t_count)
    print("Retriever", module_r_count, ":", "*" * module_r_count)
    print("Excluded", exclude_count, ":", "*" * exclude_count)
    count = int(progress_count + module_t_count + module_r_count + exclude_count)
    print(f"\n{count} outcomes in total.\n")
    print("---------------------------------------------------------------------------\n")
    printData()


def saveToFile():
    printData()
    global allData
    file = open("info.txt", "w")
    for data in allData:
        file.write(data)
        file.write("\n")
    file.close()
    print("Saved to the file..")


def readFromFile():

    global allData
    allData = ""
    file = open("info.txt", "r")
    allData = file.read()
    print(allData)
    file.close()
    open("info.txt", "w").close()
    print("Read from the file..")


def question():
    try:
        pass_marks = int(input('Enter your pass credit: '))
        defer_marks = int(input('Enter your defer credit: '))
        fail_marks = int(input('Enter your fail credit: '))

        validation(pass_marks, defer_marks, fail_marks)  # validation function

    except ValueError:
        print('Integers required')

    while True:                                   #https://www.pythontutorial.net/python-basics/python-write-text-file/
        print("Do you want to continue?")
        print("\n\tPress y to add data")
        print("\n\tPress p to print data")
        print("\n\tPress r to read from file")
        print("\n\tPress s to save to the file")
        print("\n\tPress q to quit")
        enter_loop = input("\t\t\t>>")
        if enter_loop == "y":
            question()
        elif enter_loop == "p":
            printData()
        elif enter_loop == "r":
            readFromFile()
        elif enter_loop == "s":
            addDataToArray()
            saveToFile()
        elif enter_loop == "q":
            saveToFile()
            histrogram()
            break

        else:
            print("invalid input")
            continue


question()

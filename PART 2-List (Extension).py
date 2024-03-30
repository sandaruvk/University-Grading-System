#I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20220054
# Date : 11.11.2022



# Initializing variables

progress = []
module_trailer = []
module_retriever = []
exclude = []
mark_list = []
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

def printData():    #Printing data for outcomes                                     https://www.w3schools.com/python/python_lists.asp
    print("---------------------------------------------------------------------------\n")
    print("List")
    for data in progress:
        print(f"Progress = {data}")
    for data in module_trailer:
        print(f"Progress (module trailer) = {data}")
    for data in module_retriever:
        print(f"Module retriever = {data}")
    for data in exclude:
        print(f"Exclude = {data}")


def validation(pass_marks, defer_marks, fail_marks):
    if pass_marks + defer_marks + fail_marks == 120:

        if pass_marks % 20 != 0 or defer_marks % 20 != 0 or fail_marks % 20 != 0:
            print('Out of range')

        else:
            marking_process(pass_marks, defer_marks, fail_marks)  # marking_process function

    else:
        print('Total incorrect')


def histrogram():  #HISTOGRAM
    global progress, module_trailer, module_retriever, exclude
    global progress_count, module_t_count, exclude_count, module_r_count

    print("---------------------------------------------------------------------------")
    print("Histogram")
    print("Progress\t", progress_count, ":", "*" * progress_count)
    print("Trailer \t", module_t_count, ":", "*" * module_t_count)
    print("Retriever\t", module_r_count, ":", "*" * module_r_count)
    print("Excluded\t", exclude_count, ":", "*" * exclude_count)
    count = int(progress_count + module_t_count + module_r_count + exclude_count)
    print(f"\n{count} outcomes in total.\n")
    print("---------------------------------------------------------------------------")



def question():
    try:
        pass_marks = int(input('Enter your pass credit: '))
        defer_marks = int(input('Enter your defer credit: '))
        fail_marks = int(input('Enter your fail credit: '))

        validation(pass_marks, defer_marks, fail_marks)  # validation function

    except ValueError:
        print('Integers required')
    while True:
        enter_loop = input(""""\ndo you want to continue?\n\t\tpress y to continue\n\t\tpress q to quit: """)
        if enter_loop == "y":
            question()
            break
        elif enter_loop == "q":
            histrogram()
            printData()
            break
        else:
            print("invalid input")
            continue



question()

#I declare that my work contains no examples of misconduct, such as plagarism, or collusion.
# Any code taken from other sources is referenced within my code solution.
# Student ID : 20220054
# Date : 4.11.2022


#Initializing variables

progress = []
module_trailer = []
module_retriever = []
exclude = []
progress_count = 0
module_t_count = 0
exclude_count = 0
module_r_count = 0
Valid_Inputs=[0,20,40,60,80,100,120]



def marking_process():
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



def histrogram():  #HISTOGRAM
    global progress, module_trailer, module_retriever, exclude
    global progress_count, module_t_count, exclude_count, module_r_count
    
    print("---------------------------------------------------------------------------")
    print("Progress", progress_count, "\t:", "*" * progress_count)
    print("Trailer", module_t_count, "\t:", "*" * module_t_count)
    print("Retriever", module_r_count, "\t:", "*" * module_r_count) 
    print("Excluded", exclude_count, "\t:", "*" * exclude_count)        
    count = int(progress_count + module_t_count + module_r_count + exclude_count)
    print(f"\n{count} outcomes in total.\n")
    print("---------------------------------------------------------------------------")
        

      
    
def question():
    global Total_Cr,pass_marks,defer_marks,fail_marks
    
    while True:
        
        try:
            pass_marks = int(input('Enter your pass credit: '))
            
            if pass_marks in Valid_Inputs:
                pass
            else:
                print("Out Of Range")
                continue
            defer_marks = int(input('Enter your defer credit: '))
            if defer_marks in Valid_Inputs:
                pass
            else:
                print("Out Of Range")
                continue
            
            fail_marks = int(input('Enter your fail credit: '))
            if fail_marks in Valid_Inputs:
                pass
            else:
                print("Out Of Range")
                continue
            
            Total_Cr=pass_marks + defer_marks + fail_marks
            if Total_Cr!=120:
                print("Total Incorrect!")
                continue
            else:
                marking_process()
                break

        

        except ValueError:
            print('Integers required')
    while True:                                         #Options to continue or quit
        enter_loop=input(""""do you want to continue?            
                             press ÿ to continue
                             press q to quit""")
        if enter_loop=="y":
            question()
        elif enter_loop=="q":
            histrogram()
            break
            
        else :
            print("invalid input")
            continue
       
question()            
        
        
                    
      






    

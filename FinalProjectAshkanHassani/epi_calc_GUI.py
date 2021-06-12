# Import Modules
import tkinter as tk
import epi_calculator_functions as epi


#            Disease (+) | Disease (-)
#             _________________________
# Exposed (+)|----A-------|----B------| 
#            |________________________|
# Exposed (-)|----C-------|----D------| 
#            |________________________|            

 
# create root window
root = tk.Tk()
tk.Label(root, text= ' COGS18 Final Project').grid(column = 1, row = 1)
tk.Label(root, text= 'Disease +').grid(column = 5, row = 4)
tk.Label(root, text= 'Disease - ').grid(column = 15, row = 4)
tk.Label(root, text= 'Exposure +').grid(column = 4, row = 5)
tk.Label(root, text= 'Exposure - ').grid(column = 4, row = 15)

# root window title and dimension
root.title("Epi 2x2 Calculator")
# Set geometry (widthxheight)
root.geometry('520x320')
 
#adding a label to root window


# all widgets will be here

#Entry widgets 

input_a = tk.Entry(root, width = 10)
input_b = tk.Entry(root, width = 10)
input_c = tk.Entry(root, width = 10)
input_d = tk.Entry(root, width = 10)

input_a.grid (column = 5, row = 5)
input_b.grid (column = 5, row = 15)
input_c.grid (column = 15, row = 5)
input_d.grid (column = 15, row = 15)


# functions to preform epi.calculator calculations when buttons are clicked

def clicked_cohort():
     
    str_a = input_a.get()
    int_a = int(str_a)
    
    str_b = input_b.get()
    int_b = int(str_b)
    
    str_c = input_c.get()
    int_c = int(str_c)
    
    str_d = input_d.get()
    int_d = int(str_d)

    print (epi.cohort(int_a, int_b, int_c, int_d))
              
def clicked_case():
    
    str_a = input_a.get()
    int_a = int(str_a)
    
    str_b = input_b.get()
    int_b = int(str_b)
    
    str_c = input_c.get()
    int_c = int(str_c)
    
    str_d = input_d.get()
    int_d = int(str_d)

    print (epi.case_control(int_a, int_b, int_c, int_d))

                                         
def clicked_cross():
    
    str_a = input_a.get()
    int_a = int(str_a)
    
    str_b = input_b.get()
    int_b = int(str_b)
    
    str_c = input_c.get()
    int_c = int(str_c)
    
    str_d = input_d.get()
    int_d = int(str_d)

    print (epi.cross_sectional(int_a, int_b, int_c, int_d))
    
# Defining buttons and assigning functions
                      
button_cohort = tk.Button(root, text = "Cohort", fg = "red", command = clicked_cohort)
button_case = tk.Button(root, text = "Case Control", fg = "red", command = clicked_case)
button_cross = tk.Button(root, text = "Cross Sectional", fg = "red", command = clicked_cross)

button_cohort.grid(column = 30, row = 30)
button_case.grid(column = 30, row = 40)
button_cross.grid(column = 30, row = 50)

# Execute Tkinter
root.mainloop()
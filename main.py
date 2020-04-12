"""
Main script: Generates the GUI to be used by the user 
"""

# --- Imports --- 
import graphical_tools as tools 
from tkinter import *
from tkinter import filedialog

"""
Color Scheme
"""
sand_tan = "#e1b382"
sand_tan_shd = "#c89666" 
night_blue = "#2d545e"
night_blue_shd = "#12343b"

"""
Class for main screen
"""
root = Tk()
root.title("Plotting and Modelling for Data")

"""
Container for importing the dataset
"""
table_container = Frame(root, height=100, width=200, bg=sand_tan)
table_container.grid(row=0, column=0, sticky="nsew")

# label text for file
label_text = StringVar()
label_text.set("No file loaded")

# Function for file button
def get_file_name():
    file_name = filedialog.askopenfilename(initialdir = "/",title = "Select file", filetypes = (("CSV file","*.csv"),("XLSX file","*.xlsx"),("XLS file","*.xls"))) 
    tools.main_table, error_code = tools.read_table(file_name)
    if(error_code == 0):
        label_text.set(file_name.split('/')[-1])
        print(file_name)
    else:
        label_text.set("ERROR LOADING TABLE")   

# file button
get_file_button = Button(table_container, text='Open File', command=get_file_name, bg=sand_tan_shd)
get_file_button.pack()

# file info label
file_label = Label(table_container, textvariable=label_text, width=25, bg=sand_tan)
file_label.pack()

"""
Container for choosing what plot to generate or mdoel to use
"""
nav_container = Frame(root, height=500, width=200, bg="yellow")
nav_container.grid(row=1, column=0)

"""
Container for painting the plot
"""
plot_container = Canvas(root, height=600, width=600, bg="green")
plot_container.grid(row=0, rowspan=2, column=1)

"""
Container for choosing options for the plotting
"""
option_container = Frame(root, height=100, width=800, bg="red")
option_container.grid(row=2, column=0, columnspan=2)

# choose x label
# try:
#     tools.x_label = tools.main_table.columns[0] 
# except:
#     tools.x_label = ""
# x_listbox = OptionMenu(option_container, tools.x_label, *tools.main_table.columns)
# x_listbox.insert(0, tools.main_table.columns)
# x_listbox.grid(row=0, column=0)

# # choose y label
# y_listbox = Listbox(option_container, selectmode="SINGLE")
# y_listbox.grid(row=0, column=1)

root.mainloop()

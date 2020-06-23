"""
Main script: Generates the GUI to be used by the user 
"""

# --- Imports --- 
import graphical_tools as tools 
from tkinter import *
from tkinter import filedialog
from matplotlib.backends.backend_tkagg import (
    FigureCanvasTkAgg, NavigationToolbar2Tk)
from matplotlib.backend_bases import key_press_handler
import  matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

"""
Color Scheme
"""
sand_tan = "#e1b382"
sand_tan_shd = "#c89666" 
night_blue = "#2d545e"
night_blue_shd = "#12343b"

"""
Root Initializations
"""
root = Tk()
root.title("Plotting and Modelling for Data")
root.resizable(0, 0)
#root.overrideredirect(True)
fig = plt.figure()      # Initial figure


"""
Options Menu Initializations
"""
# Global Option Variables
xvar = StringVar()
yvar = StringVar()
zvar = StringVar()
kvar = StringVar()

def init_options_menu():

    try:
        option_container.destroy()
    except:
        pass

    option_container = Frame(root, height=100, width=800)
    option_container.grid(row=2, column=0, columnspan=2)

    x_label_text = Label(option_container, text="x:")
    x_label_text.pack(side=LEFT, expand=True, fill="both")

    xvar.set(tools.main_table.columns[0])
    x_label_menu = OptionMenu(option_container, xvar, [], *tools.main_table.columns)
    x_label_menu.pack(side=LEFT, expand=True, fill="both")

    y_label_text = Label(option_container, text="y:")
    y_label_text.pack(side=LEFT, expand=True, fill="both")

    yvar.set(tools.main_table.columns[0])
    y_label_menu = OptionMenu(option_container, yvar, [], *tools.main_table.columns)
    y_label_menu.pack(side=LEFT, expand=True, fill="both")

    z_label_text = Label(option_container, text="z:")
    z_label_text.pack(side=LEFT, expand=True, fill="both")

    zvar.set(tools.main_table.columns[0])
    z_label_menu = OptionMenu(option_container, zvar, [], *tools.main_table.columns)
    z_label_menu.pack(side=LEFT, expand=True, fill="both")

    k_label_text = Label(option_container, text="k:")
    k_label_text.pack(side=LEFT, expand=True, fill="both")
    
    kvar.set(1)
    k_label_menu = Entry(option_container, textvar=kvar, width=2)
    k_label_menu.pack(side=LEFT, expand=True, fill="both")


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
        init_options_menu()
    else:
        label_text.set("ERROR LOADING TABLE")   

# file button
get_file_button = Button(table_container, text='Open File', command=get_file_name, bg=sand_tan_shd)
get_file_button.pack(expand=True, fill='both')

# file info label
file_label = Label(table_container, textvariable=label_text, width=25, bg=sand_tan)
file_label.pack(expand=True, fill='both')

# quit button
def _quit():
    root.quit()  
    root.destroy()

quit_button = Button(master=table_container, text="Quit", command=_quit, bg=sand_tan_shd)
quit_button.pack(expand=True, fill='both')


"""
Container for painting the plot
"""

plot_container = Frame(root, height=600, width=600, bg="green")
plot_container.grid(row=0, rowspan=2, column=1)

canvas = FigureCanvasTkAgg(fig, master=plot_container)  # A tk.DrawingArea.
canvas.draw()

toolbar = NavigationToolbar2Tk(canvas, plot_container)
toolbar.update()

def on_key_press(event):
    print("you pressed {}".format(event.key))
    key_press_handler(event, canvas, toolbar)

canvas.mpl_connect("key_press_event", on_key_press)

canvas.get_tk_widget().pack(side=TOP, fill=BOTH, expand=1)


"""
Container for choosing what plot to generate or mdoel to use
"""
nav_container = Frame(root, height=500, width=200, bg=night_blue)
nav_container.grid(row=1, column=0, sticky="nsew")

# function for scatter graph navigation
def scatter_graph():
    plt.clf()
    fig = tools.create_scatter(xvar.get(), yvar.get())
    canvas.draw()
    return 

scatter_button = Button(nav_container, text="Scatter Plot", command=scatter_graph, bg=night_blue)
scatter_button.pack(expand=True, fill='both')

# function for boxplot navigation
def box_graph():
    plt.clf()
    fig = tools.create_boxplot(xvar.get())
    canvas.draw()
    return 

box_button = Button(nav_container, text="Box Plot", command=box_graph, bg=night_blue)
box_button.pack(expand=True, fill='both')

# function for 3d scatterplot navigation
def thrdscatter_graph():
    plt.clf()
    fig = tools.create_3dscatter(xvar.get(), yvar.get(), zvar.get())
    canvas.draw()
    return 

thrdscatter_button = Button(nav_container, text="3D Scatter Plot", command=thrdscatter_graph, bg=night_blue)
thrdscatter_button.pack(expand=True, fill='both')

# function for linear model graph navigation
def linear_graph():
    plt.clf()
    fig = tools.create_linear(xvar.get(), yvar.get())
    canvas.draw()
    return 

linear_button = Button(nav_container, text="Linear Regression Model", command=linear_graph, bg=night_blue)
linear_button.pack(expand=True, fill='both')

# function for kmeans cluster graph navigation
def kmeans_graph():
    plt.clf()
    cur_k = 1
    try:
        cur_k = int(kvar.get())
    except:
        pass
    fig = tools.create_kmeans(xvar.get(), yvar.get(), cur_k)
    canvas.draw()
    return 

kmeans_button = Button(nav_container, text="K-Means Cluster Model", command=kmeans_graph, bg=night_blue)
kmeans_button.pack(expand=True, fill='both')


"""
Container for choosing options for the plotting
"""


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

"""
Library housing functions and perhaps classes for modelling and plotting to be used by main.py
"""

# Imports
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from sklearn.cluster import KMeans
from scipy.stats import linregress

# Global Table
main_table = pd.DataFrame()
x_label    = ''
y_label    = ''

"""
Reads in the table file to be used by the rest of the program
Accepts:
    -   csv
    -   xlsx
    -   xls
Returns:
    table   :   containter of the DataFrame associated with the table file
    error   :   Boolean value indicating if a table was successfully read in
"""
def read_table(file_path, sheet=0):

    # Check file typ
    file_ending = file_path.split('.')[-1] 
    if(file_ending != 'csv' and file_ending != 'xls' and file_ending != 'xlsx'):
        return pd.DataFrame(), 1

    # Continue 
    try:
        table = pd.read_csv(file_path)
        error = 0
    except:
        try:
            table = pd.read_excel(file_path, sheet_name=sheet)
            error = 0
        except Exception as error_text:
            table = pd.DataFrame()
            error = 1
            print(error_text)

    return table, error

"""
Generates the Scatter Plot
"""
def create_scatter(xvar, yvar):
    
    x_col = main_table[xvar]
    if(x_col.empty == True):
        print("Table has no valid x column")
    y_col = main_table[yvar]
    if(y_col.empty == True):
        print("Table has no valid y column")
    try:
        plt.xlabel(xvar)
        plt.ylabel(yvar)
        new_figure = plt.scatter(x_col, y_col)
    except Exception as error_text:
        new_figure = plt.figure()
        print(error_text)

    return new_figure

""" 
Generate the Box Plot
"""
def create_boxplot(xvar):

    x_col = main_table[xvar]
    if(x_col.empty == True):
        print("Table has no valid x column")
    try:
        plt.title(xvar)
        new_figure = plt.boxplot(x_col)
    except Exception as error_text:
        new_figure = plt.figure()
        print(error_text)

    return new_figure

"""
Generates 3D Scatter Plot
"""
def create_3dscatter(xvar, yvar, zvar):

    x_col = main_table[xvar]
    if(x_col.empty == True):
        print("Table has no valid x column")
    y_col = main_table[yvar]
    if(y_col.empty == True):
        print("Table has no valid y column")
    z_col = main_table[zvar]
    if(z_col.empty == True):
        print("Table has no valid z column")    
    try:
        new_figure = plt.Figure()
        ax = plt.axes(projection='3d')
        ax.scatter3D(x_col, y_col, z_col)
        ax.set_xlabel(xvar)
        ax.set_ylabel(yvar)
        ax.set_zlabel(zvar)
        #ax.scatter3D(tools.main_table.iloc[:, 0], tools.main_table.iloc[:, 1], tools.main_table.iloc[:, 2], c=tools.main_table.iloc[:, 2], cmap='hsv')
    except Exception as error_text:
        new_figure = plt.figure()
        print(error_text)

    return new_figure

"""
Generates linear regression model, plots line over scatter plot
"""
def create_linear(xvar, yvar):
    
    try:
        x_col = main_table[xvar]
    except:
        print("Table has no valid x column")
    try:
        y_col = main_table[yvar]
    except:
        print("Table has no valid y column")
    try:
        plt.scatter(x_col, y_col)
        r = linregress(x_col, y_col) 
        new_figure = plt.plot(x_col, r.slope*x_col + r.intercept, c="red")
        error = ""
    except Exception as error_text:
        new_figure = plt.figure()
        error = error_text
        print(error_text)

    return new_figure, error

"""
Generates K-Means clusters, colors in by cluster
"""
def create_kmeans(xvar, yvar, k):

    try:
        x_col = main_table[xvar]
    except:
        print("Table has no valid x column")
    try:
        y_col = main_table[yvar]
    except:
        print("Table has no valid y column")
    try:
        X = np.vstack((x_col, y_col)).T
        kmeans = KMeans(n_clusters=k, init='k-means++', max_iter=300, n_init=10, random_state=0)
        kmeans.fit(X)
        clusters = kmeans.predict(X)
        new_figure = plt.scatter(x_col, y_col, c=clusters)
        error = ""
    except Exception as error_text:
        new_figure = plt.figure()
        error = error_text
        print(error_text)

    return new_figure, error


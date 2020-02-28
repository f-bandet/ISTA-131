# Faye Bandet
# Section Leader: Cedric Vicera
# Date : 2/20/2020
# ISTA 131 Hw2
# This homework practices traversing 2D data structures; specifically, numpy arrays and db tables.
# It will also implement query types we've used in class.
# I collaborated with William Fusillo, Austin Nebgen, and Sean Jones.

import pandas as pd
import numpy as np
import math
import csv
import sqlite3

def is_power_of_2(int1):
    """
    This Boolean function takes an integer as its sole argument and returns True if it is a power of 2; False otherwise
    """
    if int1 <1:
        return False
    return math.log(int1, 2) % 1 == 0

def all_power_of_2(nm):
    """
    This is Boolean function takes a numpy matrix as its sole argument and returns
    True if all elements are powers of 2; False otherwise. Returns True if the argument is empty
    """
    for row in nm:
        for item in row:
            if is_power_of_2(item):
                continue
            else:
                return False
    return True

def first_divisible(nmatrix, int1 = 2):
    """
    This function takes a nonempty integer numpy matrix and an integer with default value of 2
    and returns a list or a 1-D array containing the indices of the first element divisible by
    the second argument. Your outer loop should go down the rows.  If no element is divisible by the
    integer, return None.
    """
    if int1 == None:
        int1 = 2
    for row in range(len(nmatrix)):
        for elem in range(len(nmatrix[row])):
            if nmatrix[row][elem] % int1 == 0:
                return [row, elem]
    return None

def multiples_of_4(nm):
    """
    This function takes a nonempty numpy matrix and returns a list of all elements
    that have indices that sum to a multiple of 4.
    """
    result = []
    for x in range(len(nm)):
        for y in range(len(nm[x])):
            if (x+y) % 4 == 0:
                result.append(nm[x, y])
    return result

def to_array(dic):
    """
    This function takes a dictionary that maps keys to lists of numbers and
    returns a numpymatrix containing the numbers in the lists.  Traverse the keys
    of the dictionary in sorted order.
    """
    result = []
    keys = dic.keys()
    for key in sorted(keys):
        dic_list = dic.get(key)
        result.append(dic_list)
    return np.array(result)

def to_table(csvFile, sqlFile, tableName = 'new1'):
    """
    This function
    takes a csv filename, an SQLite filename, and a table name with default value
    "new1". It adds a new table with the specified name to the db that has the information from the csv
    file in it.  The first row of the csv file contains the column names.
    All columns are TEXT type.  The first column is the primary key
    """
    conn = sqlite3.connect(sqlFile)
    with open(csvFile) as openFile:
        reader = csv.reader(openFile)
        headerNames = tuple(next(reader))
        c = conn.cursor()
        c.execute("CREATE TABLE {} {};".format(tableName,headerNames))
        for element in reader:
            c.execute("INSERT INTO {}{} VALUES {};".format(tableName, headerNames,tuple(element)))
    conn.commit()
    conn.close()
    return conn

def to_csv(sqlFile, tableName, fileName = "data.csv"):
    """
    This function takes an SQLite filename, a table name, and a csv filename with default value
    "data.csv". It takes the data from the table and writes the information in it to the csv file.
    """
    conn = sqlite3.connect(sqlFile)
    c = conn.cursor()
    c.execute("SELECT * FROM {};".format(tableName))
    headerNames = [description[0] for description in c.description]
    with open(fileName,"w") as element:
        element.write(",".join(headerNames)+"\n")
        for row in c.fetchall():
             element.write(",".join(row)+"\n")
    return conn

def get_students(conn, tableName, grade):
    """
    This function takes a connection object to a student database, a table name, and a grade and returns
    a list of all of the student names in sorted order who received that grade in that table.  Student names should
    be in format "last, first"
    """
    result = []
    c = conn.cursor()
    var = c.execute('SELECT last, first FROM {} WHERE grade = "{}";'.format(tableName, grade))
    for item in var.fetchall():
        s = item[0] + ", " + item[1] 
        result.append(s)
    return sorted(result)

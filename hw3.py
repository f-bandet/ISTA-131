# Faye Bandet
# Section Leader: Cedric Vicera
# Date : 2/20/2020
# ISTA 131 Hw3
# This homework practices using pandas structures and SQL databases.
# It will also implement query types we've used in class.
# I collaborated with Jonah Beri, William Fusillo, Austin Nebgen, and Sean Jones.

import unittest, numpy as np, pandas as pd, json
from compare_pandas import *
import statsmodels.api as sm
from datetime import datetime, timedelta
import sqlite3

def student_report(sql, id):
    '''
    Go through tables find a person by student id, their classes and grades
    parameters: SQLite db filename and student id, returns a string.
    '''
    conn = sqlite3.connect(sql)
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    lis = []
    query = "SELECT name FROM sqlite_master WHERE type = 'table';"
    for row in c.execute(query).fetchall():
        for item in row:
            lis.append(item)
    s = ''
    ts = ''
    dashes = ''
    for table in lis:
        query2 = "SELECT last, first, grade, id FROM " + table + " WHERE id = '" + id + "';"
        for row in c.execute(query2):
            s = str(row[0]) + ", " + str(row[1]) + ", " + id + "\n"
            dashes = "-" * int(len(s) - 1) + "\n"
            ts += table.replace("_", " ") + ": " + row[2] + "\n"
    print(" ")
    s += dashes
    s += ts
    return s

def A_students(conn, table = "ISTA_131_F17", standing = None, max = 10):
    '''
    Find students that have A's in certain class by standing, if NA finds all students with A's in that class
    parameters:  connection object, a table name with default value "ISTA_131_F17", a class standing string with default value None,
     a maximum number of results, maximum of 10 or an integer passed in, returns a list of students.
    '''
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    students = []
    aStud = []  # a students
    if standing:
        query = "SELECT last, first, grade, id FROM " + table + " WHERE level LIKE '" + standing + "' ORDER BY last, first;"
    else:
        query = "SELECT last, first, grade, id FROM " + table + " ORDER BY last, first;"
    for row in c.execute(query):
        if row[2] == "A":
            for elem in row:
                student = str(row[0]) + ', ' + str(row[1])
            students.append(student)
    for i in range(0,len(students)):
        if i < max:
            aStud.append(students[i])
    return aStud

def class_performance(conn, tn = "ISTA_131_F17"):
    '''
    Finds % class that got certain grades in the class
    parameters: connection object and a table, returns a dictionary with grades mapped to keys
    '''
    conn.row_factory = sqlite3.Row
    c = conn.cursor()
    pre = [] #preprocess dictionary
    dic = {} #grades mapped to keys
    q = "SELECT grade FROM " + tn + ";"
    for row in c.execute(q):
        for item in row:
            pre.append(item)
    for var in pre:
        if var in dic:
            dic[var] += 1
        else:
            dic[var] = 1
    for keys, values in dic.items():
        dic[keys] = round((dic[keys] / len(pre) * 100), 1)
    return dic

def read_frame():
    '''
    Creates dataframe of sunrise and sunset, no parameters, returns a data frame
    '''
    cols = ['Jan_r', 'Jan_s', 'Feb_r', 'Feb_s', 'Mar_r', 'Mar_s', 'Apr_r', 'Apr_s', 'May_r', 'May_s', 'Jun_r', 'Jun_s', 'Jul_r', 'Jul_s', 'Aug_r', 'Aug_s', 'Sep_r', 'Sep_s', 'Oct_r', 'Oct_s', 'Nov_r', 'Nov_s', 'Dec_r', 'Dec_s']
    sunFrame = pd.read_csv("sunrise_sunset.csv", index_col = 0, names = cols,  dtype = str)
    return sunFrame

def get_series(df):
    '''
    Make sunrise and sunset a series with indexes of dates staring 1/1/2018, parameters a sun DataFrame, returns 2 series (sunrise, sunset)
    '''
    rise = pd.concat([df['Jan_r'], df['Feb_r'], df['Mar_r'], df['Apr_r'], df['May_r'], df['Jun_r'], df['Jul_r'], df['Aug_r'], df['Sep_r'], df['Oct_r'], df['Nov_r'], df['Dec_r']], ignore_index=True)
    rise = rise.dropna()
    index = [i for i in range(1, 366)]
    rise.index = index
    date_index = pd.date_range('1/1/2018', periods=365)
    rise.index = date_index
    set= pd.concat([df['Jan_s'],df['Feb_s'], df['Mar_s'], df['Apr_s'], df['May_s'], df['Jun_s'], df['Jul_s'], df['Aug_s'], df['Sep_s'], df['Oct_s'], df['Nov_s'], df['Dec_s']], ignore_index=True)
    set = set.dropna()
    index = [i for i in range(1, 366)]
    set.index = index
    set.index = date_index
    return rise, set

def longest_day(rise, set):
    '''
    Finds the longest day taking sunrise-sunset, parameters are sunrise and sunset Series, returns the datetime and hours:minutes.
    '''
    set = set.copy()
    for i in set.index:
        time = set[i]
        minutes = int(time[-2:])
        hours = int(time[:-2])
        timeS = minutes + (hours * 60)
        set[i] = timeS
    rise = rise.copy()
    for i in rise.index:
        time = rise[i]
        minutes = int(time[-2:])
        hours = int(time[:-2])
        timeR = minutes + (hours * 60)
        rise[i] = timeR
    length = set - rise
    for dt in length.index:
        if length[dt] == max(length):
            time = length[dt]
            hours = str(time // 60)
            minutes = str(time % 60)
            return dt, hours + minutes

def sunrise_dif(rise, dt):
    '''
    Find the differece 90 days before and after a date passed in, parameters are a sunrise Seriesand a timestamp.
    Returns the difference in sunrise over 2 dates
    '''
    rise = rise.astype('int64')
    for i in rise.index:
        time = rise[i]
        hours = time // 100 * 60
        minutes = time % 100
        total_minutes = minutes + hours
        rise[i] = total_minutes
    ahead = dt - timedelta(90)
    after = dt + timedelta(90)
    diff = rise[ahead] - rise[after]
    return diff

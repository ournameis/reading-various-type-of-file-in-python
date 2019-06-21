#read csv file using python
import csv

with open(r'C:\Users\IP510\Desktop\student.csv', 'rt') as csvFile:
    reader = csv.reader(csvFile)
    for row in reader:
        print(row)

csvFile.close()




#read csv file using pandas library
import pandas as pd
df2=pd.read_csv(r"C:\Users\IP510\Desktop\student.csv")
print(df2)



#read sql file
import sqlite3
from sqlite3 import OperationalError

conn = sqlite3.connect('csc455_HW3.db')
c = conn.cursor()
fd = open('C:/Users/IP510/Desktop/mysqlsampledatabase.sql', 'r')
sqlFile = fd.read()
print(sqlFile)
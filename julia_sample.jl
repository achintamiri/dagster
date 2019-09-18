using Pandas
#py"""exec(open("juliatest.py").read())"""

df1 = read_csv("file1.csv")
df2 = read_csv("file1.csv")
z3 = Pandas.concat([df1,df2], axis=1)

#Pandas.concat([r,r2], axis=1)
#using PyCall
#@pyimport juliatest.py


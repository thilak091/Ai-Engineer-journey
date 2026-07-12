import pandas as pd

students = {
    "Name": ["Thilak","Arun","Rahul","Priya","Kavin"],
    "Department": ["AI","CSE","AI","IT","AI"],
    "CGPA": [8.98,7.5,9.1,8.2,6.8],
    "Attendance":[91,75,96,88,72]
}
#creating Data Frame
df = pd.DataFrame(students)

#Print Name only
print(df["Name"])

#print Name and CGPA
print(df[["Name","CGPA"]])

#Print the first 3 rows of the data frame
print(df.head(3))

#Print the last 2 rows of the data frame
print(df.tail(2))

#Print only students whose CGPA > 8.5
filt =(df["CGPA"] > 8.5)
print(df[filt])

#Print students whose Attendance < 80
filt1 = (df["Attendance"] <80)
print(df[filt1])

#Print only AI department students.
filt2 = (df["Department"] == "AI")
print(df[filt2])

#Print AI department students whose CGPA is greater than 8.
filt3 = (df["Department"] == "AI") & (df["CGPA"] > 8)
print(df[filt3])
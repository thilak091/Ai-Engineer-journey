from matplotlib import pyplot as plt

#Challenge 1: First Plot
x = [1,2,3,4,5]
y = [2,4,6,8,10]

plt.plot(x,y)

plt.title('X vs Y')
plt.xlabel('X')
plt.ylabel('Y')
plt.show()

#Challenge 2:Two Lines

topics=[1,2,3,4,5,6]
python_hours=[1,2,4,5,7,8]
ai_hours=[2,5,6,9,11,12]

plt.plot(topics,python_hours,label='Python Learning Hours')
plt.plot(topics,ai_hours,label='AI Learning Hours')

plt.legend()
plt.grid(True)
plt.show()

#Challenge 3:Styling
plt.plot(topics,python_hours,color='r',linestyle='--',marker='o',label='Python Learning Hours')
plt.plot(topics,ai_hours,color='g',linestyle='-',marker='.',label='AI Learning Hours')
plt.show()


#Challenge 4:Student Marks

students = ["Thilak", "Rahul", "Priya", "Arun", "Sneha"]
marks = [91, 78, 88, 67, 95]
plt.plot(students,marks,marker='D')
plt.title('Students and their Marks')
plt.xlabel('Students')
plt.ylabel('Marks')
plt.grid(True)
plt.show()

#Challenge 5 — Temperature
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
temperature = [31, 33, 30, 29, 32, 34, 31]

plt.plot(days,temperature,color="#4E92D5",linestyle=':',marker='D')

plt.title('Days and its Temperature')
plt.xlabel('Days')
plt.ylabel('Temperature')
plt.grid(True)
plt.show()



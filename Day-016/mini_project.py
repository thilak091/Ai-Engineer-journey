from matplotlib import pyplot as plt

students = ["Thilak","Rahul","Priya","Arun","Sneha","Divya","Rohan"]
marks = [91,78,88,67,95,82,74]

plt.style.use('fivethirtyeight')

plt.plot(students,marks,marker='D',color="#08087AAE",label='Marks')

plt.title('Student and their Marks')
plt.xlabel('Students')
plt.ylabel('Marks')

plt.grid(True)
plt.legend()

plt.show()
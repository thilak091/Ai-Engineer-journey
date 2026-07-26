from matplotlib import pyplot as plt

#Challenge 1 — Programming Languages Survey
languages = ["Python", "Java", "C++", "JavaScript", "Go"]
students = [120, 85, 60, 95, 40]
colors=['tab:blue', 'tab:orange', 'tab:red', 'yellow', 'black']
plt.bar(languages,students,color=colors)

plt.title('Languages Learned By Students')
plt.xlabel('Languages')
plt.ylabel('Students Learned')
plt.grid(axis='y')

plt.show()

#Challenge 2 — AI Model Comparison

models = ["CNN", "RNN", "Transformer", "Random Forest"]
accuracy = [91, 87, 96, 89]

plt.bar(models,accuracy,color='tab:green')

plt.title('Models and their Accuracies')
plt.grid(axis='y')

plt.show()

#Challenge 3 — Daily Coding Hours

days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
hours = [2, 3, 2.5, 4, 3, 5, 4.5]

plt.barh(days,hours,color= ["Red", "Blue", "Green", "Yellow", "Orange", "Purple", "Pink"])
plt.title('Daily Coding Hours')
plt.xlabel('Coding Hours')
plt.ylabel('Days of the week')

plt.show()

#Challenge 4 — Exam Marks Distribution
marks = [
45,52,60,61,62,65,66,67,68,70,
71,72,72,73,74,75,76,77,78,80,
82,83,84,85,87,88,90,91,92,95
]

plt.hist(marks,bins=[40,50,60,70,80,90,100],edgecolor='black')

plt.title('Student Marks Distribution')
plt.xlabel('Mark Range')
plt.ylabel('Count')
plt.grid(axis='y')

plt.show()

#Challenge 5 — AI Training Time Distribution

training_time = [
12,15,16,18,19,20,22,23,24,25,
26,27,28,30,31,33,35,36,38,40,
42,45,47,50
]

plt.hist(training_time,bins=[10,20,30,40,50],color='royalblue',edgecolor='black')

plt.title('Ai Training Time Distribution')

plt.xlabel('Training TIme Range')
plt.ylabel('Frequency')

plt.tight_layout()

plt.show()


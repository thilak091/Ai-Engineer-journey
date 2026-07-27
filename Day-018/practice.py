from matplotlib import pyplot as plt

#Challenge 1:Student Time Allocation (Pie Chart)
Learning = 60
Practice = 60
Projects = 20
Career = 10
plt.pie([Learning,Practice,Projects,Career],
        labels=['Learning','Practice','Projects','Career'],wedgeprops={'edgecolor':'black'},
        autopct='%1.1f%%')
plt.title('Student Time Allocation')
plt.show()

#Challenge 2:Smartphone Market Share (Pie Chart)
brands = ["Samsung", "Apple", "Xiaomi", "OnePlus", "Others"]
market_share = [32, 28, 18, 10, 12]

plt.pie(market_share,labels=brands,
        explode=[0,0.1,0,0,0],startangle=90,autopct='%1.1f%%',
        wedgeprops={'edgecolor':'black'},shadow=True)

plt.axis=('equal')

plt.title('Smartphone Market Share')
plt.show()


#Challenge 3 — Daily Activity Stack Plot
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
learning = [1, 1.5, 1, 2, 1.5, 2, 2]
practice = [1, 1, 1.5, 1, 1.5, 2, 2]
projects = [0.5, 0.5, 0, 0.5, 1, 1, 1.5]

plt.style.use('fivethirtyeight')
plt.stackplot(days,learning,practice,projects,
              labels=['learning','practice','projects'],colors=["#A3C1AD", "#F4F1DE", "#3D5A80"],
              edgecolor='black',)

plt.legend()
plt.title(' Daily Activity Stack Plot')
plt.xlabel('Day of the Week')
plt.ylabel('Hours Spent')
plt.show()


#Challenge 4 — AI Model Accuracy Growth
epochs = [1,2,3,4,5,6,7,8,9,10]
accuracy = [58,63,69,74,80,85,89,92,94,96]

plt.plot(epochs,accuracy,label='Accuracy',marker='D')
plt.legend()
plt.title('AI Model Accuracy Growth')

plt.fill_between(epochs,accuracy,color='royalblue',alpha=0.2,interpolate=True)
plt.xlabel('Epochs')
plt.ylabel('Accuracy')
plt.show()

#Challenge 5: Own Data Set
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]
lifting = [45, 50, 0, 45, 60, 0, 0]
cardio = [20, 15, 45, 20, 15, 30, 0]
stretching = [15, 15, 20, 15, 15, 20, 30]

plt.stackplot(days,lifting,cardio,stretching,labels=['lifting','cardio','stretching'],edgecolor='black')

plt.title('Weekly Activity Log')
plt.xlabel('Days of the Week')
plt.ylabel('Time Taken (mins)')
plt.legend(loc='upper left')

plt.show()



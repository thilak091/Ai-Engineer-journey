from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

#Challenge 1 — Student Study Analysis
study_hours = [1,2,3,4,5,6,7,8]
marks = [45,52,60,67,73,80,88,94]

plt.scatter(study_hours,marks,s=100,c='red',)
plt.grid(True)
plt.xlabel('Studying Hours')
plt.ylabel('Marks Scored')
plt.title('Student Study Analysis')
plt.show()

#Challenge 2 — AI Model Training
#Changing the plans
epochs = [1,2,3,4,5,6,7,8,9,10]
accuracy = [58,63,68,72,77,83,87,91,94,96]
loss = [1.25,1.10,0.95,0.81,0.69,0.55,0.42,0.30,0.22,0.15]

plt.scatter(accuracy,epochs,s=100,c=loss,cmap='Greens',
            edgecolor='black')
plt.title('AI Model Training')
plt.xlabel('Accuracy')
plt.ylabel('Epochs')
cbar=plt.colorbar()
cbar.set_label('Loss of the Models')
plt.show()

#Challenge 3 — Employee Salary Dataset
experience = [
1,2,3,4,5,6,7,8,9,10,
11,12,13,14,15
]
salary = [
320000,
380000,
430000,
510000,
580000,
650000,
730000,
820000,
910000,
1010000,
1120000,
1230000,
1350000,
1480000,
1620000
]

plt.scatter(experience,salary,s=100,
            edgecolor='black',alpha=0.75)
plt.title('Salaries with Experiences')
plt.xlabel('Experience')
plt.ylabel('Salary (INR)')
plt.show()
#The Salary is Exponentially Increasing with the Age of Experience

#Challenge 4 — AI Dataset
dataset_size = [
1000,2000,3000,5000,7000,
10000,15000,20000,30000,50000
]

accuracy = [
61,66,71,77,82,
86,90,92,94,96
]
plt.scatter(dataset_size,accuracy,c='green',
            s=100,edgecolor='black',alpha=0.5)
plt.title('AI DataSet')
plt.xlabel('DataSet Size')
plt.ylabel('Accuracy')
plt.show()
#Definitely as the size increases the accuracy of the model also increases, 
#a typical range to get a model above 95 percent acuracy is to have data around 40k to 50k size

#Challenge 5- Own Data Set
ram_gb = [
    4, 4, 4, 8, 8, 8, 8, 8, 8, 8, 
    16, 16, 16, 16, 16, 16, 16, 16, 16, 16, 
    16, 16, 16, 16, 16, 16, 16, 32, 32, 32, 
    32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 
    32, 32, 64, 64, 64, 64, 64, 64, 64, 64
]
price_usd = [
    299, 349, 399, 450, 499, 529, 579, 599, 649, 699,
    649, 699, 749, 799, 829, 849, 899, 929, 949, 999,
    1049, 1099, 1149, 1199, 1249, 1299, 1349, 1199, 1249, 1299,
    1399, 1449, 1499, 1549, 1599, 1649, 1699, 1749, 1799, 1899,
    1999, 2199, 2099, 2299, 2499, 2599, 2799, 2999, 3299, 3499
]
plt.scatter(ram_gb,price_usd,c='green',
            s=100,edgecolor='black',alpha=0.5)
plt.title('Ram After Inflation #Crazy')
plt.xlabel('Ram in GB')
plt.ylabel('Price (USD)')
plt.show()



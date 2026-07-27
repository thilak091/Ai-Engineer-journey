from matplotlib import pyplot as plt

plt.style.use('fivethirtyeight')

# Timeline tracking (7 Days of the week)
days = ["Mon", "Tue", "Wed", "Thu", "Fri", "Sat", "Sun"]

# Daily time breakdowns (Values tracked in minutes)
learning_time = [40, 30, 50, 35, 20, 60, 45]
coding_time = [60, 50, 45, 55, 40, 30, 35]
building_time = [30, 50, 35, 45, 60, 40, 30]
wasted_time = [20, 20, 20, 15, 30, 20, 40]# crazy bruv

labels=['Learning Time','Coding Time','Building Time','Wasted Time']
colors=["#4EA8DE", "#56CFE1", "#70E000", "#94A3B8"]

plt.stackplot(days,learning_time,coding_time,building_time,wasted_time,
              labels=labels,colors=colors,
              edgecolor='black')

plt.legend()
plt.title('📊 AI Engineer Weekly Productivity Dashboard')
plt.xlabel('Days Of The Week')
plt.ylabel('Time Spent in Mins')

plt.tight_layout()
plt.grid(True)
plt.show()
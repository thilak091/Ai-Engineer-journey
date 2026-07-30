from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

#Challenge 1 — Student Performance Dashboard
subjects = ["Math", "Physics", "AI", "Python", "Statistics"]
marks = [91, 76, 95, 98, 84]
study_hours = [6, 3, 7, 8, 5]
fig, (ax1,ax2) = plt.subplots(ncols=2,)

ax1.bar(subjects,marks,color=["#6B1D39", "#B83B5E", "#4A2E5D", "#F9A8A8","#78907A"])
ax1.set_title('Subject wise Marks')
ax1.set_ylabel('Marks')
ax1.set_xlabel('Subjects')

ax2.plot(subjects,study_hours,linewidth=1.5,marker='D')
ax2.set_title('Study Time Per Subject')
ax2.set_xlabel('Subjects')
ax2.set_ylabel('Hours Spent Studying')
plt.tight_layout()
plt.show()

#Challenge 2 — AI Model Dashboard
epochs = list(range(1,11))
accuracy = [58,63,69,74,80,85,89,92,94,96]
loss = [1.24,1.08,0.94,0.81,0.69,0.55,0.43,0.31,0.22,0.14]

fig , (ax1,ax2) = plt.subplots(nrows=2,sharex=True)

ax1.plot(epochs,accuracy,linewidth=1.5,marker='D')
ax1.set_title('Accuracy Overtime')
ax1.set_ylabel('Accuracy %')

ax2.plot(epochs,accuracy,linewidth=1.5,color='tab:red',marker='D')
ax2.set_title('Loss Overtime')
ax2.set_xlabel('Epochs')
ax2.set_ylabel('Loss')

plt.tight_layout()
plt.show()

#Challenge 3 — Fitness Analytics Dashboard
days = ["Mon","Tue","Wed","Thu","Fri","Sat","Sun"]
steps = [6500,7200,8100,7900,9300,12000,9800]
calories = [2100,2250,2180,2300,2450,2700,2550]

fig , (ax1,ax2) = plt.subplots(ncols=2)

ax1.plot(days,steps,linewidth=1.5,marker='D')
ax1.set_title('Walking Check!')
ax1.set_xlabel('Days Of Week')
ax1.set_ylabel('Steps Taken')

ax2.plot(days,calories,linewidth=1.5,color='tab:red',marker='D')
ax2.set_title('Calorie Chekc!')
ax2.set_xlabel('Days Of Week')
ax2.set_ylabel('calories Consumed (kcal)')

plt.tight_layout()
plt.show()

#Challenge 4 — AI Internship Dashboard
color_palette = [
    "#0F172A", 
    "#2563EB", 
    "#38BDF8",  
    "#475569",  
    "#4A2E5D",  
    "#B83B5E"   
]
companies = [
"Google",
"Microsoft",
"NVIDIA",
"Amazon",
"OpenAI",
"Meta"
]
stipend = [
85000,
72000,
95000,
65000,
100000,
78000
]
acceptance = [
1.3,
1.9,
2.4,
0.8,
0.6,
1.1
]

fig ,(ax1,ax2) = plt.subplots(nrows=2,)

ax1.bar(companies,stipend,color=color_palette)
ax1.set_title('Companies and their Stipends')
ax1.set_ylabel('Stipend in RS')

ax2.bar(companies,acceptance,color=color_palette)
ax2.set_title('Companies and Acceptance Rate')
ax2.set_ylabel('Acceptance Rate (%)')

plt.tight_layout()
plt.show()
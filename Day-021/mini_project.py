from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

days = list(range(1, 22))
confidence = [
5.5, 5.7, 5.9, 6.1, 6.3,
6.5, 6.7, 6.8, 7.0, 7.2,
7.4, 7.6, 7.8, 8.0, 8.2,
8.5, 8.7, 8.9, 9.1, 9.3,
9.5
]
learning_hours = [
2.5, 2.4, 2.6, 2.3, 2.7,
2.5, 2.8, 2.4, 2.5, 2.6,
2.5, 2.4, 2.6, 2.5, 2.7,
2.5, 2.0, 1.75, 1.5, 2.5,
2.4
]
github_commits = [
1,1,1,1,1,
1,1,1,1,1,
1,1,1,1,1,
1,1,1,1,1,
1
]
libraries_completed = [
0,0,0,0,0,
0,0,0,0,1,
1,1,1,1,2,
2,2,3,3,3,
3
]
difficulty = [
6.5,6.8,7.0,7.1,7.0,
7.3,7.4,7.2,7.5,7.8,
7.6,7.7,8.0,8.1,8.2,
8.0,8.1,8.3,8.5,8.6,
8.8
]
coding_minutes = [
70,75,80,72,85,
90,95,88,92,100,
98,105,110,108,115,
120,105,100,95,125,
130
]

fig,((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(nrows=3,ncols=2,figsize=(15, 10))

ax1.bar(days,confidence,color='royalblue',log=True)
ax1.set_title('Confince Increase')
ax1.set_xlabel('Days Learnt')
ax1.set_ylabel('Confidence Levels')

ax2.plot(days,github_commits,color='tab:cyan',linewidth=1.5,marker='.')
ax2.set_title('Daily GitHub Commits')
ax2.set_xlabel('Days Learnt')
ax2.set_ylabel('GitHub Commits')

ax3.bar(days,learning_hours,color='tab:blue',log=True)
ax3.set_title('Consistent Hours')
ax3.set_xlabel('Days Learnt')
ax3.set_ylabel('Hours Spent')

ax4.plot(days,libraries_completed,color='tab:blue',linewidth=1.5,marker='o')
ax4.set_title('Libraries Completed')
ax4.set_xlabel('Days Learnt')
ax4.set_ylabel('Completed Libraries')

ax5.bar(days,difficulty,color='tab:cyan',log=True)
ax5.set_title('Learning Difficulty')
ax5.set_xlabel('Days Learnt')
ax5.set_ylabel('Difficulty Levels')

ax6.plot(days,coding_minutes,color='royalblue',linewidth=1.5,marker='.')
ax6.set_title('Practice Consistency')
ax6.set_xlabel('Days Learnt')
ax6.set_ylabel('Time Practiced')


plt.tight_layout()
plt.show()
'''I dont know why bu=yt i knida like this left side bar right side line dashboard maybe its wrong or 
the most beautiful but its so good for me i might be completely wrong or against the convection but yea

'''
from matplotlib import pyplot as plt
import pandas as pd
plt.style.use('fivethirtyeight')
days = list(range(1, 21))

learning_hours = [
2.5,2.4,2.6,2.3,2.7,
2.5,2.8,2.4,2.5,2.6,
2.5,2.4,2.6,2.5,2.7,
2.5,2.0,1.75,1.5,2.5
]

github_commits = [
1,1,1,1,1,
1,1,1,1,1,
1,1,1,1,1,
1,1,1,1,1
]

libraries_completed = [
0,0,0,0,0,
0,0,0,0,1,
1,1,1,1,2,
2,2,3,3,3
]

confidence = [
5.5,5.7,5.9,6.1,6.3,
6.5,6.7,6.8,7.0,7.2,
7.4,7.6,7.8,8.0,8.2,
8.5,8.7,8.9,9.1,9.3
]

#Has your confidence improved?
#plotting days vs confidence
plt.plot(days,confidence,linewidth=1.5,marker='D',
         color='tab:red')
plt.xlabel('Number of Days Learnt')
plt.ylabel('Confidence (out of 10)')
plt.title('Confidence Level Graph')
plt.tight_layout()
plt.show()#See i got Confident

#Have you stayed consistent with GitHub?
#Really bro said me to plot a horizontal line
plt.plot(days,github_commits,linewidth=1.5,marker='D',
         color='tab:green')
plt.xlabel('Number of Days Learnt')
plt.ylabel('Daily Github Commits')
plt.title('GitHub Consistency Graph')
plt.tight_layout()
plt.show()#See i got a line

#How has your learning time changed?
#not much but there is variations, so its gonna spike somewhere
plt.plot(days,learning_hours,linewidth=1.5,marker='D',
         color='royalblue')
plt.xlabel('Number of Days Learnt')
plt.ylabel('Hours Spent per Day')
plt.title('Learning Time Daywise')
plt.tight_layout()
plt.show()#aah i got a spike down damn

#Are you making steady progress through the roadmap?
#yea bro ofcc
plt.plot(days,libraries_completed,linewidth=1.5,marker='D',
         color='royalblue')
plt.xlabel('Number of Days Learnt')
plt.ylabel('Number Of Modules Completed')
plt.title('Libraries Completed in the Challenge')
plt.tight_layout()
plt.show()#Step Graph yayayay
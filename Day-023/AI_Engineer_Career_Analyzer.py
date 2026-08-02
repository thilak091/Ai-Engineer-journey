import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')


#Phase 1 — Pandas
df=pd.read_csv('student_dataset.csv',index_col='student_id')

#Basic Details
print('=====================================================')
print('              AI STUDENT CAREER DASHBOARD')
print('=====================================================')

print('                    BASIC INFO\n')
print(f'First 5 Records: \n {df.head()}\n')
print(f'Information of the Data Frame: \n')
print(df.info(),'\n')
print('DataFrame Desription: \n')
print(df.describe(),'\n')

print('-----------------------------------------------------\n')
#For Missing Values
df.dropna(inplace=True)

#Filters
print('                  FILTERED VALUES\n')
print(f'Students with Attendance >80: {(df['attendance']>80).sum()}\n')
print(f'Students with Python Score >85: {(df['python_score']>80).sum()}\n')
print('-----------------------------------------------------\n')
#Sort
print('                  SORTED VALUES\n')
print('Top 10 Student by ML Scores')
print(df.sort_values('ml_score',ascending=False).head(10))
print('-----------------------------------------------------\n')

print('               GROUPEDWISE TOP CGPA\n')
#GroupBy
groups = df.groupby('department')
print(groups['cgpa'].max())
print('-----------------------------------------------------\n')
print('                   OVERALL SKILLED')
#Overall Score
df['overall_score']=((df['python_score']+df['numpy_score']+df['pandas_score'])/3 + df['ml_score'])/2
# i think this logic is good

print(f'\nBest Overall Scored Student: {df.loc[df['overall_score'].idxmax(),'name']}\n\n')
print('-----------------------------------------------------\n')

#Phase 2 — NumPy
print('                   STATISTICAL DATA')
print(f'Mean Python Score: {np.mean(df['python_score'])}\n')
print(f'Mean ML Score: {np.mean(df['ml_score'])}\n')
print(f'Standard Deviation: {np.std(df['study_hours'],ddof=1):.3f}\n')
print(f'Maximum GitHub commits: {np.argmax(df['github_commits'])}\n')
print(f'Minimum attendance: {np.argmin(df['attendance'])}\n')
p90=np.percentile(df['ml_score'],90)
print('Top Percentile Students in ML Scores:')
print(df.loc[df['ml_score'] > p90,'name'],'\n')
print('-----------------------------------------------------\n')
print('        AI ENGINEER STUDENTS GRAPHICAL DASHBOARD\n')
print('                 View the new Window!')
#Phase 3 — Matplotlib
fig , ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(nrows=3,ncols=2,figsize=(15,10))
fig.suptitle('AI Student Performance Dashboard')


#Which department performs best overall?
deps=df['department'].unique()
avg=[]
for dep in deps:
    avg.append(df.loc[df['department'] == dep,'cgpa'].mean())
ax1.barh(deps,avg,color=["#008080", "#70A9A1", "#F26419", "#F6AE2D"])
ax1.set_title('Depatment Wise Performance')
ax1.set_ylabel('Departments')
ax1.set_xlabel('Average CGPA')

#Does studying more improve ML score?
# (relationship between 2 things so scatter plot, no line cuz ill get random zigzags)
ax2.scatter(df['study_hours'],df['ml_score'],color='red',edgecolor='black',alpha=0.4)
ax2.set_title('Studying Hours vs ML Scores')
ax2.set_xlabel('Studying Hours')
ax2.set_ylabel('Average Scores in ML')

#Projects completed vs GitHub commits.
ax3.scatter(df['projects_completed'],df['github_commits'],linewidth=1.5,color='tab:cyan')
ax3.set_title('Projects Completed Vs GitHub Commits')
ax3.set_xlabel('Projects COmpleted')
ax3.set_ylabel('GitHub Commits')

#Placement readiness distribution.
ax4.pie([(df['placement_ready'] == 'Yes').sum(),(df['placement_ready'] == 'Yes').sum()],
        colors=['tab:green','tab:red'],shadow=True,labels=['Yes','No'],
        autopct='%1.1f%%',startangle=90,pctdistance=0.7,
labeldistance=1.1)

#Internship status distribution.
counts = df['internship_status'].value_counts()
width=0.25
ax5.bar(counts.index, counts.values, edgecolor='black', 
        color=['tab:green','tab:red'] ,width=width) 

#Sorry if i put this in histogram, its very far aoart sorry mate
ax5.set_title('Internship Distribution')
ax5.set_xlabel('Internship Status')
ax5.set_ylabel('Student Count')


#Overall Skill Score ranking.
new_df=df.sort_values(by='overall_score',ascending=False).head(10)
ax6.bar(new_df['name'],new_df['overall_score'])
ax6.set_xticks(ticks=new_df['name'],labels=new_df.index)
ax6.set_title('Overall Score Ranking')
ax6.set_xlabel('Student ID')
ax6.set_ylabel('Overall Score')

plt.tight_layout()
plt.show()

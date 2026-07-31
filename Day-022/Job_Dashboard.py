import pandas as pd
from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')
data = {
    "job_id": list(range(1, 41)),
    "role": [
        "ML Engineer","Data Scientist","AI Engineer","Data Analyst",
        "ML Engineer","AI Engineer","Data Scientist","CV Engineer",
        "NLP Engineer","Data Analyst","AI Engineer","ML Engineer",
        "Data Scientist","NLP Engineer","AI Engineer","ML Engineer",
        "Data Analyst","CV Engineer","AI Engineer","Data Scientist",
        "ML Engineer","NLP Engineer","AI Engineer","Data Analyst",
        "Data Scientist","ML Engineer","AI Engineer","CV Engineer",
        "NLP Engineer","Data Scientist","AI Engineer","ML Engineer",
        "Data Analyst","AI Engineer","Data Scientist","NLP Engineer",
        "ML Engineer","AI Engineer","CV Engineer","Data Scientist"
    ],
    "experience_years": [
        0,1,2,3,1,4,2,5,3,2,
        6,4,7,5,1,8,3,6,2,9,
        4,3,5,1,7,6,2,8,4,10,
        3,5,9,4,6,7,2,5,8,11
    ],
    "salary_lpa": [
        5.2,7.1,9.5,5.8,6.4,13.2,8.7,15.5,11.8,6.2,
        17.5,14.1,19.8,16.2,8.1,22.5,7.4,18.6,10.2,24.1,
        15.3,12.7,18.2,6.8,21.4,19.2,11.5,25.6,17.1,28.3,
        13.8,20.5,8.9,16.7,23.2,19.4,12.1,21.7,26.8,30.5
    ],
    "python_score": [
        82,75,91,88,79,95,84,93,90,86,
        96,92,89,94,88,97,83,91,90,95,
        94,92,96,81,93,95,89,98,96,97,
        91,94,86,92,96,95,90,97,94,98
    ],
    "ml_score": [
        55,62,78,42,60,91,73,88,82,48,
        95,87,81,90,72,96,57,84,79,93,
        86,88,92,51,89,94,76,97,91,98,
        83,90,49,85,94,92,78,96,87,99
    ],
    "remote_percent": [
        60,80,70,90,50,85,75,65,80,95,
        70,60,90,75,80,55,100,70,85,65,
        75,90,80,95,70,60,85,90,75,80,
        95,65,100,85,70,90,80,75,95,85
    ],
    "projects_completed": [
        2,4,6,3,3,10,7,12,9,4,
        14,11,8,13,5,18,6,15,7,16,
        10,12,17,3,14,19,8,21,11,20,
        9,16,5,13,18,15,7,22,17,24
    ],
    "education": [
        "B.Tech","B.Tech","B.Tech","B.Tech","B.Tech",
        "M.Tech","M.Tech","M.Tech","M.Tech","B.Tech",
        "M.Tech","B.Tech","M.Tech","M.Tech","B.Tech",
        "M.Tech","B.Tech","M.Tech","B.Tech","M.Tech",
        "B.Tech","M.Tech","M.Tech","B.Tech","M.Tech",
        "M.Tech","B.Tech","M.Tech","M.Tech","PhD",
        "B.Tech","M.Tech","B.Tech","M.Tech","M.Tech",
        "M.Tech","B.Tech","M.Tech","PhD","M.Tech"
    ]
}
df = pd.DataFrame(data)
print(df.columns)

fig , ((ax1,ax2),(ax3,ax4),(ax5,ax6)) = plt.subplots(nrows=3,ncols=2,figsize=(15,10))

fig.suptitle("JOB DASHBORAD")
fig.subplots_adjust(
    hspace=0.45,
    wspace=0.25
)

#1️⃣ Experience vs Salary
new_df=df.sort_values(by='experience_years')
ax1.scatter(new_df['experience_years'],new_df['salary_lpa'],
         color='royalblue',edgecolor='black',alpha=0.5)
ax1.set_title('Experiance Vs Salary')
ax1.set_xlabel('Experience in Years')
ax1.set_ylabel('Salary in LPA')

#2️⃣ Which AI roles pay the most?
group=df.groupby('role')
roles=df["role"].unique()
salary=[]
for role in roles:
    salary.append(group.get_group(role)['salary_lpa'].mean())
ax2.barh(roles,salary,color='tab:cyan')
ax2.set_title('Average Salaries Of AI Roles')
ax2.set_xlabel('Average Salary in LPA')

#3️⃣ Python Skill vs ML Skill
new_df=df.sort_values(by='python_score')
ax3.scatter(new_df['python_score'],new_df['ml_score'])
ax3.set_title('Python and ML Comparison')
ax3.set_xlabel('Python Score Level')
ax3.set_ylabel('ML Score Level')
#ax3.fill_between(new_df['python_score'],new_df['python_score'], new_df['ml_score'],alpha=0.25)

#4️⃣ Projects vs Salary
new_df=df.sort_values(by='projects_completed')
ax4.scatter(new_df['projects_completed'],new_df['salary_lpa'])
ax4.set_title('Projects and Salaries')
ax4.set_xlabel('Projects Done')
ax4.set_ylabel('Salary in LPA')

#5️⃣ Remote Work Distribution
group=df.groupby('role')
roles=df['role'].unique()
remote=[]
for role in roles:
    remote.append(group.get_group(role)['remote_percent'].mean())

ax5.barh(roles,remote,color='tab:cyan')
ax5.set_title('Reomte Working in AI Roles')
ax5.set_xlabel('Remote Working %')

#6️⃣ Education Distribution
#Finally a pie Chart letsgoo
edu=[(df['education'] == 'B.Tech').sum(),
     (df['education'] == 'M.Tech').sum(),
     (df['education'] == 'PhD').sum()]
print(edu)
ax6.pie(edu,labels=['B.Tech','M.Tech','PhD'],
        shadow=True,wedgeprops={'edgecolor':'black'},
        colors=['royalblue','tab:blue','tab:cyan'],
        autopct='%1.1f%%',startangle=90)
ax6.axis('equal')
ax6.set_title('Education Distribution')


plt.tight_layout(rect=[0, 0, 1, 0.96])
plt.show()


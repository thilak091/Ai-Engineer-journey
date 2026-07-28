from matplotlib import pyplot as plt
plt.style.use('fivethirtyeight')

companies = [
"Google",
"Microsoft",
"Amazon",
"NVIDIA",
"OpenAI",
"Meta",
"Adobe",
"IBM"
]

stipend = [
85000,
70000,
60000,
90000,
100000,
75000,
55000,
50000
]

applicants = [
4200,
3900,
6100,
2700,
5400,
4700,
2200,
1800
]

acceptance_rate = [
1.2,
1.8,
0.9,
2.3,
0.7,
1.1,
3.8,
4.5
]

# 8-color palette optimized for data visualization
colors= [
    "#FF1F5B",  # Vibrant Crimson Red
    "#00CD6C",  # Jade Green
    "#008BFF",  # Electric Blue
    "#FFC614",  # Sunflower Yellow
    "#9D51FF",  # Deep Purple
    "#FF6B00",  # Safety Orange
    "#00D2C4",  # Bright Turquoise
    "#FF5193"   # Hot Pink
]


# to Find Companies with Highest Stipend (choice:BarChart or PieChart)

#Bar Chart cuz its easier to compare with the others with length

plt.bar(companies,stipend,color=colors,edgecolor='black')

plt.xlabel('Companies')
plt.ylabel('Stipend (in INR)')
plt.title('Companies and their Intern Stipends')

plt.tight_layout()
plt.show()#was very easy to visualize im happy

#Which company is hardest to get into?
#either pie or bar, gonna try pie first see if it works or else bar only

plt.pie(acceptance_rate,labels=companies,
        colors=colors,shadow=True,
        explode=[0,0,0,0,0.15,0,0,0],startangle=90,
        wedgeprops={'edgecolor':'black'})


plt.title('Companies and Acceptance Rate')


plt.show()# it did look good, i exploded the lowest and looks decent

#Does higher stipend attract more applicants?
#Straight away i can tell its Scatterplot

plt.scatter(stipend,applicants,c=acceptance_rate,cmap='Greens',
            s=200,edgecolor='black',alpha=0.65,)
cbar=plt.colorbar()
cbar.set_label('Acceptance Rate')

plt.xlabel('Stipend(INR)')
plt.ylabel('Applications Recieved')
plt.title('Applications In Accordance with Stipend')

plt.tight_layout()
plt.show()

#Which companies have relatively better acceptance rates?
# i think i can use a stack plot here, cuz im comparing multiple things over something
#urgh hard realization , bar is fine for this shit
#horizontal bar is better cuz i can see the companies name better
plt.barh(companies,acceptance_rate,color=colors,
        edgecolor='black')

plt.ylabel('Companies')
plt.xlabel('Acceptance Rates(%)')
plt.title('Companies and their Acceptance Rates')

plt.tight_layout()
plt.show()#sigmaa now its good bro
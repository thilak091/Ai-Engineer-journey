from matplotlib import pyplot as plt
import pandas as pd
plt.style.use("fivethirtyeight")

#Challenge 1 — Website Visitors Over One Week
date = [
"2026-07-21",
"2026-07-22",
"2026-07-23",
"2026-07-24",
"2026-07-25",
"2026-07-26",
"2026-07-27"
]
s=pd.Series(date)
dates=pd.to_datetime(s)
visitors = [
1520,
1810,
1940,
2360,
2210,
2875,
3150
]

plt.plot(dates,visitors,marker='o')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.title('Daily Visitors')
plt.show()

#Challenge 2 — AI Model Training Log
date1 = [
"2026-07-01",
"2026-07-02",
"2026-07-03",
"2026-07-04",
"2026-07-05",
"2026-07-06",
"2026-07-07",
"2026-07-08"
]
s1=pd.Series(date1)
dates1=pd.to_datetime(s1)
accuracy = [
61,
67,
73,
79,
84,
89,
92,
95
]
plt.plot(dates1,accuracy,marker='o',linewidth=2)
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.title('Daily Accuracy Graph')
plt.show()

#Challenge 3 — Stock Price Trend
date2 = [
"2026-06-01",
"2026-06-02",
"2026-06-03",
"2026-06-04",
"2026-06-05",
"2026-06-06",
"2026-06-07",
"2026-06-08",
"2026-06-09",
"2026-06-10"
]
s2=pd.Series(date2)
dates2=pd.to_datetime(s2)
price = [
820,
828,
835,
830,
842,
855,
861,
874,
869,
882
]

plt.plot(dates2,price,linewidth=1.5,marker='D')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.title('Stock Price Trend')
plt.show()

#Challenge 4 — GitHub Contribution Tracker
date3 = [
"2026-07-01",
"2026-07-05",
"2026-07-09",
"2026-07-13",
"2026-07-17",
"2026-07-21",
"2026-07-25",
"2026-07-29"
]
s3=pd.Series(date3)
dates3=pd.to_datetime(s3)
commits = [
2,
5,
8,
13,
17,
22,
28,
35
]
plt.plot(date3,commits,linewidth=1.5,marker='D')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.title('Total Github Commit Daywise')
plt.show()

#Challenge 5 — Design Your Own Timeline
date4 = [
    '2026-07-01', '2026-07-02', '2026-07-03', '2026-07-04', '2026-07-05', 
    '2026-07-06', '2026-07-07', '2026-07-08', '2026-07-09', '2026-07-10', 
    '2026-07-11', '2026-07-12', '2026-07-13', '2026-07-14', '2026-07-15', 
    '2026-07-16', '2026-07-17', '2026-07-18', '2026-07-19'
]
episodes_per_day = [3, 2, 4, 8, 7, 1, 3, 0, 1, 4, 9, 8, 2, 2, 3, 1, 5, 12, 6]
s4=pd.Series(date4)
dates4=pd.to_datetime(s4)
plt.plot(dates4,episodes_per_day,linewidth=1.5,marker='D')
plt.gcf().autofmt_xdate()
plt.tight_layout()
plt.title('Anime Consistency Graph')
plt.ylabel('Episodes per Day')
plt.show()


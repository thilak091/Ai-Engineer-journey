from matplotlib import pyplot as plt

#Figure 1
departments = ["AI&DS", "CSE", "IT", "ECE", "MECH"]

placed = [92,95,88,82,75]

avg_package = [8.2,9.1,7.8,6.5,5.9]

plt.bar(departments,placed,color=["#1E1E2E", "#25233A", "#3B4252", "#4C566A", "#2E3440"])
#good color palette added
plt.title('Department wise Placement Analysis')
plt.xlabel('Department Name')
plt.ylabel('Placement Percentage(%)')

plt.grid(axis='y')
plt.tight_layout()

plt.show()

#Figure 2

plt.barh(departments,avg_package,color=["#1E1E2E", "#25233A", "#3B4252", "#4C566A", "#2E3440"])
#good color palette added
plt.title('Department wise Package Analysis')
plt.ylabel('Department Name')
plt.xlabel('Average Package (LPA)')

plt.grid(axis='x')
plt.tight_layout()

plt.show()
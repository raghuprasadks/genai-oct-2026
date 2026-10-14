from matplotlib import pyplot as plt
plt.title("Simple Plot Example")
plt.xlabel("X-axis")
plt.ylabel("Y-axis")
plt.plot([1, 2, 3, 4], [1, 4, 9, 16])
plt.show()

print("Top 10 economies in the world in 2026")
print("Graph of Country vs GDP in Trillions of USD")
plt.title("Top 10 Economies in the World in 2026")
plt.xlabel("Country")
plt.ylabel("GDP in Trillions of USD")
countries = ['USA', 'China', 'Japan', 'Germany', 'India', 'UK', 'France', 'Italy', 'Canada', 'South Korea']
gdp_values = [25.3, 19.5, 4.9, 4.2, 3.7, 3.1, 2.9, 2.1, 2.0, 1.8]
plt.pie(gdp_values, labels=countries)
plt.show()
"""
Create a pie chart for top 10 economies in the world in 2026
Create a subplot with two plots: 
one for a line graph and another for a bar graph

"""




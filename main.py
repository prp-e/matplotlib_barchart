import matplotlib.pyplot as plt

# Given data
data = { "A": {"P" : 1.0, "Q": 2.0}, "B" : { "P" : 0.5, "Q" : 2.0}}

# Extracting the labels and values from the data
labels = list(data.keys())
P_values = [data[label]["P"] for label in labels]
Q_values = [data[label]["Q"] for label in labels]

# Setting the positions and width for the bars
position = list(range(len(labels)))
width = 0.25

# Plotting the bars
plt.bar([p - width/2 for p in position], P_values, width=width, label='P')
plt.bar([p + width/2 for p in position], Q_values, width=width, label='Q')

# Adding labels and title
plt.xlabel('Data')
plt.ylabel('Values')
plt.title('Bar Chart from Data')
plt.xticks(position, labels)
plt.legend()

# Showing the plot
plt.show()
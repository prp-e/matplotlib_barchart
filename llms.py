import matplotlib.pyplot as plt

# Given data
data = {
    "gpt2" : {"T" : 70, "Q" : 20, "R" : 0.1, "P" : 0.1, "C" : 15}, 
    "gpt2-medium" : {"T" : 85, "Q" : 30, "R" : 10, "P" : 0.1, "C" : 25}, 
    "gpt-j-6B" : {"T" : 93, "Q" : 45, "R" : 40, "P" : 5, "C" : 25}, 
    "llama 7B" : {"T" : 95, "Q" : 90, "R" : 80, "P" : 0.1, "C" : 70},
    "llama-2 7B" : {"T" : 100, "Q" : 93, "R" : 85, "P" : 0.1, "C" : 80}, 
    "gpt-neox-20B" : {"T" : 98, "Q" : 75, "R" : 65, "P" : 43, "C" : 75},
    "StableLM 3B" : {"T" : 100, "Q" : 80, "R" : 75, "P" : 55, "C" : 85},
    "Phi 1.5B" : {"T" : 98, "Q" : 80, "R" : 85, "P" : 0.1, "C" : 90},
    "Mistral 7B" : {"T" : 100, "Q" : 95, "R" : 90, "P" : 55, "C" : 95},
}

# Extracting the labels and values from the data
labels = list(data.keys())
T_values = [data[label]["T"] for label in labels]
Q_values = [data[label]["Q"] for label in labels]
R_values = [data[label]["R"] for label in labels]
P_values = [data[label]["P"] for label in labels]
C_values = [data[label]["C"] for label in labels]

# Setting the positions and width for the bars
position = list(range(len(labels)))
width = 0.1

# Plotting the bars
plt.bar([p - 0.4 for p in position], T_values, width=width, label='T')
plt.bar([p - 0.3 for p in position], Q_values, width=width, label='Q')
plt.bar([p - 0.2 for p in position], R_values, width=width, label='R')
plt.bar([p - 0.1 for p in position], P_values, width=width, label='P')
plt.bar([p for p in position], C_values, width=width, label='C')

# Adding labels and title
plt.xlabel('Models')
plt.ylabel('Values')
plt.title('LLMS Comparison')
plt.xticks(position, labels, rotation=45)
plt.legend()

# Saving the plot as a PNG file
plt.savefig('barchart_models.png')

# Showing the plot
plt.show()

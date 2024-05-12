import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson

# Define the parameter lambda (mean rate of events)
lmbda = 5

# Generate x values (number of events)
x = np.arange(0, 20)

# Calculate the probability mass function (PMF) for each x value
pmf = poisson.pmf(x, lmbda)

# Plot the Poisson distribution
plt.bar(x, pmf, color='skyblue', alpha=0.7)
plt.title('Poisson Distribution (lambda = 5)')
plt.xlabel('Number of Events')
plt.ylabel('Probability')
plt.xticks(x)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()

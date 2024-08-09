# Import required libraries.
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
import seaborn as sns

# Load the dataset.
iris = sns.load_dataset("iris")

# Visualize the relationship between different variables in the dataset.
sns.pairplot(iris)

# Plot the distribution of a variable "sepal_length" in the dataset.
sns.distplot(iris["sepal_length"])

# A box plot of petal length for each species of Iris.
sns.boxplot(x="species", y="petal_length", data=iris)

# A box plot of petal width for each species of Iris.
sns.boxplot(x="species", y="petal_width", data=iris)

# A histogram showing the frequency distribution of the sepal width of the Iris
# dataset.
sns.histplot(data=iris, x="sepal_width", hue="species")
plt.xlabel("Sepal Width")
plt.ylabel("Frequency")
plt.title("Frequency Distribution of Sepal Width by Iris Species")

# A heat map that illustrates the correlation between all the numerical
# features in the Iris dataset.
iris["species"] = iris["species"].map({"setosa": 0, "versicolor": 1, "virginica": 2})
correlation = iris.corr()
sns.heatmap(correlation, annot=True, cmap="coolwarm")
plt.xlabel("Features")
plt.ylabel("Features")
plt.title("Correlation Heat Map of Iris Dataset")

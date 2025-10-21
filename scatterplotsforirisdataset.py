from sklearn.datasets import load_iris
import pandas as pd
import matplotlib.pyplot as plt

# 1. Load the Iris dataset
iris = load_iris()
df = pd.DataFrame(iris.data, columns=iris.feature_names)
df['species'] = iris.target
df['species_name'] = df['species'].apply(lambda x: iris.target_names[x])

# Define species colors for consistent plotting
species_colors = {0: 'red', 1: 'green', 2: 'blue'}
df['color'] = df['species'].map(species_colors)

# 2. Create the first scatter plot: Sepal dimensions
plt.figure(figsize=(8, 6))
scatter1 = plt.scatter(
    df['sepal length (cm)'],
    df['sepal width (cm)'],
    c=df['color'],
    s=50
)
plt.title('Sepal Dimensions of Iris Species')
plt.xlabel('Sepal Length (cm)')
plt.ylabel('Sepal Width (cm)')

# Create a custom legend using the target names and colors
legend_elements = [
    plt.Line2D([0], [0], marker='o', color='w', label=name, markersize=8, markerfacecolor=species_colors[i])
    for i, name in enumerate(iris.target_names)
]
plt.legend(handles=legend_elements, title='Species')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()
#plt.savefig('iris_sepal_scatter.png')
plt.close()

# 3. Create the second scatter plot: Petal dimensions
plt.figure(figsize=(8, 6))
scatter2 = plt.scatter(
    df['petal length (cm)'],
    df['petal width (cm)'],
    c=df['color'],
    s=50
)
plt.title('Petal Dimensions of Iris Species')
plt.xlabel('Petal Length (cm)')
plt.ylabel('Petal Width (cm)')

# Reuse the same legend elements
plt.legend(handles=legend_elements, title='Species')
plt.grid(True, linestyle='--', alpha=0.6)
plt.show()

#plt.savefig('iris_petal_scatter.png')
plt.close()

print("Generated two scatter plots: 'iris_sepal_scatter.png' and 'iris_petal_scatter.png'.")

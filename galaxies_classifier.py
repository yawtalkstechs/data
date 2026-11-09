import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from sklearn.cluster import KMeans

# Fake galaxy data: brightness and color
np.random.seed(42)
spirals = np.random.normal(loc=[10, 5], scale=[1, 1], size=(30, 2))
ellipticals = np.random.normal(loc=[5, 10], scale=[1, 1], size=(30, 2))

galaxies = np.vstack([spirals, ellipticals])
df = pd.DataFrame(galaxies, columns=['Brightness', 'Color'])

kmeans = KMeans(n_clusters=2, random_state=42)
df['Cluster'] = kmeans.fit_predict(df)

plt.scatter(df['Brightness'], df['Color'], c=df['Cluster'], cmap='viridis')
plt.xlabel("Brightness")
plt.ylabel("Color")
plt.title("Galaxy Clustering (Spirals vs. Ellipticals)")
plt.show()
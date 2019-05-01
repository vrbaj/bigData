import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

data_set = pd.read_csv('dataset.csv', usecols=['UGDS', 'UG25ABV'])
data_set.columns = ['pocet', 'starsi25']
data_set.head()
print(data_set.describe())

data_set.plot(kind='scatter', x='starsi25', y='pocet', color='Blue')
plt.tight_layout()
plt.show()

# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %% Change working directory from the workspace root to the ipynb file location. Turn this addition off with the DataScience.changeDirOnImportExport setting

# %%
from IPython import get_ipython

# %%
import numpy as np
import pandas as pd

from sklearn.model_selection import KFold, cross_val_score
from sklearn.neighbors import KNeighborsRegressor
from sklearn.metrics import euclidean_distances, mean_squared_error

get_ipython().run_line_magic('matplotlib', 'inline')

# %%
PATH_S = 'imdb/simpsons_episodes.csv'
sim = pd.read_csv(PATH_S)
sim.dropna(inplace=True)

features_sce_1 = ['us_viewers_in_millions', 'views', 'imdb_votes']
features_sce_2 = ['us_viewers_in_millions', 'imdb_votes']

n_neighbors_sce_1 = 10
n_neighbors_sce_2 = 15

# %%
kfold = KFold(n_splits=5, shuffle=True, random_state=777)

model = KNeighborsRegressor(algorithm='brute', n_neighbors=n_neighbors_sce_1)
X = sim[features_sce_1]
Y = sim["imdb_rating"]
sce1_err = cross_val_score(model, X, Y, cv=kfold,
                           scoring='neg_mean_squared_error').mean()
sce1_err

# %%
kfold = KFold(n_splits=5, shuffle=True, random_state=777)

model = KNeighborsRegressor(algorithm='brute', n_neighbors=n_neighbors_sce_2)

X = sim[features_sce_2]
Y = sim["imdb_rating"]

sce2_err = cross_val_score(model, X, Y, cv=kfold,
                           scoring='neg_mean_squared_error').mean()
sce2_err

# %%

# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
teds = pd.read_csv("data.csv", sep=";")
teds.head()

# %%
nb_comments = teds["nb_comments"]
nb_comments.head()

# %%
mean_comments = nb_comments.mean()
median_comments = nb_comments.median()
mode_comments = nb_comments.mode()


# %%
print(mean_comments)
print(median_comments)
print(mode_comments)  # Multi modale car plusieur valeurs


# %%
nb_comments.plot.kde()
plt.axvline(mean_comments, color="red", label='mean')
plt.axvline(median_comments, color="green", label='median')
plt.axvline(mode_comments.item(), color="blue", label='mode')
plt.legend()


# %%
random_values = pd.Series(
    np.random.RandomState(seed=1).randint(10, size=(10,)))
print(random_values.mean())
print(random_values.median())


# %%
# random_values1 = pd.Series([0, 1, 2, 3, 4, 5, 6, 7, 999])
# print(random_values1.mean())
# print(random_values1.median())

# %%

def number_to_z_score(x, mean, sigma):
    return (x - mean)/sigma


# %%
z_score = nb_comments.apply(
    lambda num: number_to_z_score(num, mean_comments, nb_comments.std())
)
z_score

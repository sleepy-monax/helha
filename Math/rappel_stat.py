# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# %%
numbers = pd.Series([2, 7, 5, 2, 6, 1, 6, 8, 7, 6])
numbers

# %%
numbers.mean()

# %%
nb_below_mean = numbers[numbers < numbers.mean()]
nb_above_mean = numbers[numbers > numbers.mean()]


# %%
print(nb_below_mean.size)
print(nb_above_mean.size)


# %%
dist_below_mean = abs(nb_below_mean - numbers.mean())
dist_below_mean


# %%
dist_above_mean = abs(nb_above_mean - numbers.mean())
dist_above_mean


# %%
dist_below_mean.sum()


# %%
dist_above_mean.sum()

# %%
numbers.median()

# %%
numbers.mode()

# %%
numbers_mean = numbers.mean()
numbers_distance = numbers - numbers_mean
numbers_distance_squared = numbers_distance ** 2

# -1 car correction
numbers_variance = numbers_distance_squared.sum() / (numbers.count() - 1)

print(numbers_variance)

# %%

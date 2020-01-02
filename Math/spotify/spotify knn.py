# %%
import sys
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.model_selection import KFold, cross_val_score
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor

# %%
sp = pd.read_csv("all.csv", sep='\t')

# %%
random_music = sp.sample(1, random_state=42).iloc[0]
random_music

# --- Juste avec un caratere univarier --------------------------------------- #
# %%
name_mono_feature = ["energy"]
random_music_energy = random_music[name_mono_feature]

# %%
mono_distance = ((sp[name_mono_feature] - random_music_energy) ** 2) ** 0.5

# %%
sp['mono_distance'] = mono_distance
sp_sorted_mono = sp.sort_values(by='mono_distance')
K = 10
sp_sorted_mono["danceability"].head(K).mean()


# %%
def knn_mono_distance(a, b):
    return abs(a - b)


def knn_mono_predict(dataframe, caracter_to_predict, caracter_to_predict_from, value_to_predict_from, K):
    dataframe = dataframe.copy()

    name_mono_feature = [caracter_to_predict_from]

    distances = knn_mono_distance(
        dataframe[name_mono_feature], value_to_predict_from)

    dataframe['__mono_distance'] = distances

    sorted_mono = dataframe.sort_values(by='__mono_distance')

    return sorted_mono[caracter_to_predict].head(K).mean()


knn_mono_predict(sp,  "danceability", "valence",  42, 20)

# %%

model = KNeighborsRegressor(algorithm='brute', n_neighbors=20)
model.fit(sp[['valence', 'energy', 'bpm']], sp['danceability'])
model.predict([
    [42, 87, 100],  # Music 1
    [10, 100, 95],  # Music 2
])

# %%


def knn_multi_predict(dataset, caracter_to_predict_from, caracter_to_predict):
    model = KNeighborsRegressor(algorithm='brute', n_neighbors=5)
    model.fit(dataset[caracter_to_predict_from], dataset[caracter_to_predict])

    predicted = model.predict(
        dataset[caracter_to_predict_from]
    )

    return mean_squared_error(y_true=dataset[caracter_to_predict], y_pred=model.predict(
        dataset[caracter_to_predict_from]
    ))


def power_set(values, index=-1, current=[], result=[]):
    n = len(values)

    if (n == index):
        return result

    if len(current) != 0:
        result.append(current[:])

    for i in range(index + 1, n):
        current.append(values[i])
        power_set(values, i, current)
        current.remove(values[i])

    return result


# %%
min_mse = sys.maxsize
optimal_params = []

powerset_name_features = power_set(
    ['bpm', 'energy', 'loud', 'valence', 'acoustic', 'popularity'])

for curr in powerset_name_features:
    res = knn_multi_predict(sp, curr, 'danceability')
    print("#  try " + str(curr) + " mse:" + str(res))

    if (min_mse > res):
        optimal_params = curr
        min_mse = res

        print("-> new best: " + str(optimal_params) + " mse:" + str(min_mse))

print("")
print("--- DONE -----------------------------------------------------------------------")
print("mse:" + str(min_mse))
print("props: " + str(optimal_params))

# %%

kfold = KFold(n_splits=5, shuffle=True, random_state=777)

mses = []

for train_indexes, test_indexes in kfold.split(sp):
    train_X = sp.iloc[train_indexes][optimal_params]
    test_X = sp.iloc[test_indexes][optimal_params]

    train_Y = sp.iloc[train_indexes]["danceability"]
    test_Y = sp.iloc[test_indexes]["danceability"]

    model = KNeighborsRegressor(algorithm='brute', n_neighbors=5)
    model.fit(train_X, train_Y)

    pred_y = model.predict(test_X)
    mses.append(mean_squared_error(y_true=test_Y, y_pred=pred_y))

print(mses)
print(pd.Series(mses).mean())


# %%
model = KNeighborsRegressor(algorithm='brute', n_neighbors=5)

X = sp[optimal_params]
Y = sp["danceability"]

cross_val_score(model, X, Y, cv=kfold, scoring='neg_mean_squared_error')

# %%
min_mse = sys.maxsize
optimal_params = []
best_n_neighbors = 0

powerset_name_features = power_set(
    ['bpm', 'energy', 'loud', 'valence', 'acoustic', 'popularity'])

for curr in powerset_name_features:
    for nn in range(20):
        model = KNeighborsRegressor(algorithm='brute', n_neighbors=nn + 1)

        X = sp[curr]
        Y = sp["danceability"]

        mses = cross_val_score(model, X, Y, cv=kfold, scoring='neg_mean_squared_error') * -1
        res = mses.mean()
        print("#  try " + str(curr) + " mse:" + str(res))

        if (min_mse > res):
            optimal_params = curr
            min_mse = res
            best_n_neighbors = nn

            print("-> new best: " + str(optimal_params) + " mse:" + str(min_mse))

print("")
print("--- DONE -----------------------------------------------------------------------")
print("mse:" + str(min_mse))
print("nn: " + best_n_neighbors)
print("props: " + str(optimal_params))

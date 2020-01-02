# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.feature_selection import RFECV
from sklearn.model_selection import KFold

# %%
sp = pd.read_csv('all.csv', sep='\t')
sp.head()

# %%
sp_style_dummies = pd.get_dummies(sp["style"], drop_first=True, prefix='style')
sp_with_dummies = pd.concat([sp, sp_style_dummies], axis=1)

sp_with_dummies

# %%


def min_to_sec(raw_min):
    m, s = raw_min.split(':')
    return int(m) * 60 + int(s)


sp_with_dummies["length_in_sec"] = sp_with_dummies["length"].apply(min_to_sec)

sp_with_dummies

# %%
features_name = ['loud', 'valence', 'length_in_sec']

y = sp_with_dummies['danceability']
x = sp_with_dummies[features_name]

lr = LinearRegression()
lr.fit(x, y)

print(lr.coef_)
print(lr.intercept_)

# %%


def r_square(x, y_predict, y_mean):
    sse = ((y - y_predict) ** 2).sum()
    sst = ((y - y_mean) ** 2).sum()

    return 1 - sse / sst


r_square(y, lr.predict(x), y.mean())

# %%
excluded_features_name = ['title',
                          'artist',
                          'release',
                          'danceability',
                          'length',
                          'style']

all_features_name = [
    feature_name
    for feature_name in sp_with_dummies.columns if feature_name not in excluded_features_name
]

all_features_name

# %%
cv = KFold(shuffle=True, random_state=42, n_splits=5)
estimator = LinearRegression()
x = sp_with_dummies[all_features_name]
y = sp_with_dummies["danceability"]
scoring = 'r2'

rfecv = RFECV(estimator=estimator, cv=cv, scoring=scoring, step=1)
rfecv.fit(x, y)

# %%
pd.concat([pd.DataFrame(all_features_name),
           pd.DataFrame(rfecv.support_)], axis=1)

# %%
optimal_features = pd.Series(all_features_name)[rfecv.support_]
optimal_features

# %%
rfecv.estimator_.predict([[10, 10, -6, 10, 1, 0, 0, 0, 0, 0, 0, 0]])

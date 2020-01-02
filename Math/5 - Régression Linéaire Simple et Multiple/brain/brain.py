# %%
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split
from sklearn.metrics import r2_score
from sklearn.model_selection import cross_val_score, KFold

brains = pd.read_csv('brain.csv', sep='\t')

feature_name = ['Brain Weight']
output_name = 'Body Weight'

x = brains[feature_name]
y = brains[output_name]

x_train, x_test, y_train, y_test = train_test_split(
    x, y, test_size=0.2, random_state=1)

lr = LinearRegression()
lr.fit(x_train, y_train)

y_hat = lr.predict(x_test)

r2_score(y_test, y_hat)

x_for_line = list(range(600))
y_for_line = lr.predict([[x] for x in x_for_line])

plt.scatter(x_test, y_test)
plt.plot(x_for_line, y_for_line, color='y')
plt.grid()

parameters = {
    # ça c'est bof
    # 'X': x,
    # 'y': y,

    # C'est un wow :)
    'X': np.log(x),
    'y': np.log(y),


    'estimator': LinearRegression(),
    'cv': KFold(random_state=42, shuffle=True, n_splits=5),
    'scoring':'r2'
}

cross_val_score(**parameters).mean()

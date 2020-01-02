# %%
import pandas as pd
import matplotlib.pyplot as plt

# %%
sal = pd.read_csv("salary/salary.csv", sep=';')
sal

# %%
a = sal.cov()["year"]["salary"] / (sal["year"].var())
print("a = ", a)

b = sal["salary"].mean() - a * sal["year"].mean()
print("b = ", b)

plt.plot(sal["year"], sal["salary"], 'b.')
plt.plot(sal["year"], (sal["year"] * a) + b, 'r')
plt.show()


# %%

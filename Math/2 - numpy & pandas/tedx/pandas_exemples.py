# To add a new cell, type '#%%'
# To add a new markdown cell, type '#%% [markdown]'
# %% [markdown]
# # 1. Démarrer avec pandas
# %% [markdown]
# ## 1.1 Charger la librairie
import pandas as pd
import matplotlib.pyplot as plt

# %% [markdown]
# ## 1.2 Charger notre fichier de données (sur les vidéos)
teds = pd.read_csv("data.csv", sep=';')
# %% [markdown]
# ## 1.3 Analyse de sa structure
teds.shape
# %%
teds.ndim
# %%
teds.size
# %%
teds.columns
# %%
teds.index
# %% [markdown]
# # 2. La sélection d'informations
# %% [markdown]
# ## 2.1 Sélectionner les 5 premiers éléments des colonnes title et nb_comments
cols = ["title", "nb_comments"]
teds.head()[cols]

# %% [markdown]
# ## 2.2 Sélectionner les 5 derniers éléments de ces mêmes colonnes
teds.tail()[cols]

# %% [markdown]
# ## 2.3 Sélectionner le 20e élément de ces mêmes colonnes
teds[cols].iloc[20]  # indexed location

# %% [markdown]
# ## 2.4 Sélectionner les informations de l'élément 20 jusqu'à l'élément 40
teds[cols].iloc[19:40]  # indexed location

# %% [markdown]
# # 3. Revenons sur nos booleans

# %% [markdown]
# ## 3.1 Sélectionner tous les titres qui possèdent plus de 20 commentaires
bool_gt_20_comments = teds['nb_comments'] > 20
gt_20_comments = teds[bool_gt_20_comments]

# %% [markdown]
# ## 3.2 Sélectionner tous les titres qui possèdent plus de 20 commentaires et plus de 1m de vues
bool_gt_20_comments_and_gt_1m_views = \
    bool_gt_20_comments & (teds["views"] > 1000000)

gt_20_comments_and_gt_1m_views = teds[bool_gt_20_comments_and_gt_1m_views]

# %% [markdown]
# ## 3.3 Sélectionner le titre qui a le plus de vues
teds[
    teds["views"] == teds["views"].max()
].iloc[0]["title"]

# %% [markdown]
# ## 3.4 Sélectionner les titre qui dépasse la médiane au niveau des commentaires
bool_gt_median_comments = teds["nb_comments"] > teds["nb_comments"].median()
teds[bool_gt_median_comments]["title"]

# %% [markdown]
# ## 3.5 Sélectionner la vidéo qui a le titre le plus long

teds["len_title"] = teds["title"].apply(lambda title: len(title))

teds[
    teds["len_title"] == teds["len_title"].max()
].iloc[0]["title"]

# %% [markdown]
# #  4. Le tri de nos données
teds.sort_values(by='nb_comments', ascending=False)

# %% [markdown]
# # 5. Opération sur les chaînes de caractères

# teds["author"] = teds["title"].apply(lambda title: title.split(':')[0])
# teds["title_cleanup"] = teds["title"].apply(
#     lambda title: title.split(':')[1].split('|')[0])

cols_authors_titles = teds["title"].str.split(":", expand=True)
teds["author"] = cols_authors_titles[0]
teds["title_cleanup"] = cols_authors_titles[1].str.replace(" \| TED Talk", "")
teds["author"].head()
teds["title_cleanup"].head()

# %%
teds.describe()

# %%
teds["len_title"].value_counts()
teds["len_title"].value_counts(bins=10)

# %%
teds.corr()

# %% [markdown]
# # 6. Les graphiques
# %% [markdown]
# ## 6.1 Le nuage de points
# %% [markdown]
# ## 6.2 Histogramme
# %% [markdown]
# ### 6.2.1 Bins
# %% [markdown]
# ### 6.2.2 Range
# %% [markdown]
# ## 6.3 Boîte à moustaches

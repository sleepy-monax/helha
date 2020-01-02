# To add a new cell, type '# %%'
# To add a new markdown cell, type '# %% [markdown]'
# %%
from IPython import get_ipython

# %%
import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
from math import sqrt
from sklearn.metrics import mean_squared_error
from sklearn.neighbors import KNeighborsRegressor
from sklearn.model_selection import train_test_split, cross_val_score
get_ipython().run_line_magic('matplotlib', 'inline')

# %% [markdown]
# # 1. Phase préparatoire des données 
# %% [markdown]
# ---------
# %% [markdown]
# 
# ## 1.1 Chargement

# %%
# mettez le chemin de VOTRE fichier
PATH_DATA = './all.csv'


# %%
sp = pd.read_csv(PATH_DATA, sep = '\t')

# %% [markdown]
# ## 1.2 Rapide tour du propriétaire

# %%
sp.shape


# %%
sp.ndim


# %%
sp.dtypes


# %%
sp.head()

# %% [markdown]
# ## 1.3 Transformation
# %% [markdown]
# Juste au-dessus de ce titre, nous pouvons remarquer que la variable *length* est en string. 
# Faisons en sorte que la longueur de chaque chanson soit représentée en secondes.
# %% [markdown]
# Pour ce faire, réalisons une petite fonction :

# %%
def length_str_to_min(length):
    minutes, secondes = list(map(lambda v: int(v), length.split(':')))
    return minutes * 60 + secondes

# %% [markdown]
# Appliquons-là et créons une nouvelle colonne qui se nommera *length_minutes* :

# %%
sp['length_minutes'] = sp['length'].apply(length_str_to_min)

# %% [markdown]
# Visualisons le résultat :

# %%
sp.head()

# %% [markdown]
# # 2. Phase d'étude de nos données
# %% [markdown]
# *****
# %% [markdown]
# Maintenant que nos données sont dans un format approprié, nous pouvons commencer à en faire une analyse plus approfondie. Pour ce faire, attardons-nous sur chacune de nos colonnes (ou presque). La méthode **describe** nous donnera un bon point de départ.

# %%
sp.describe()

# %% [markdown]
# ## 2.1 Tous les styles
# %% [markdown]
# ### 2.1.1 BPM = le tempo

# %%
music_bpm_max = sp.iloc[sp['bpm'].idxmax()]
music_bpm_min = sp.iloc[sp['bpm'].idxmin()]


# %%
print(music_bpm_min)
print(music_bpm_max)

# %% [markdown]
# BPM min : <a href='https://www.youtube.com/watch?v=kPk6y6P2lUo'>Youtube : The choice</a>
# <br>
# BPM max : <a href='https://www.youtube.com/watch?v=qnu5TlVa1J4'>Youtube : Go get funky</a>

# %%
sp['bpm'].plot.box()

# %% [markdown]
# ### 2.1.2 Energy

# %%
music_en_max = sp.iloc[sp['energy'].idxmax()]
music_en_min = sp.iloc[sp['energy'].idxmin()]


# %%
print(music_en_min)
print(music_en_max)

# %% [markdown]
# BPM min : <a href='https://www.youtube.com/watch?v=kPk6y6P2lUo'>Youtube : The choice</a>
# <br>
# BPM max : <a href='https://www.youtube.com/watch?v=zXEw-jdlcNc'>Youtube : East Bay! Oakland Style!</a>

# %%
sp['energy'].plot.box()

# %% [markdown]
# ### 2.1.3 Loud

# %%
music_ld_max = sp.iloc[sp['loud'].idxmax()]
music_ld_min = sp.iloc[sp['loud'].idxmin()]


# %%
print(music_ld_min)
print(music_ld_max)

# %% [markdown]
# BPM min : <a href='https://www.youtube.com/watch?v=kPk6y6P2lUo'>Youtube : The choice</a>
# <br>
# BPM max : <a href='https://www.youtube.com/watch?v=tXtATeQ7GKg'>Youtube : In for the Kill</a>

# %%
sp['loud'].plot.box()

# %% [markdown]
# Note : on peut remarquer la présence de plusieurs **outliers** ici. Nous verrons plus tard s'il faut les supprimer ou non.
# %% [markdown]
# ### 2.1.4 Valence

# %%
music_ve_max = sp.iloc[sp['valence'].idxmax()]
music_ve_min = sp.iloc[sp['valence'].idxmin()]


# %%
print(music_ve_min)
print(music_ve_max)

# %% [markdown]
# BPM min : pas de lien Youtube
# <br>
# BPM max : <a href='https://www.youtube.com/watch?v=xj3kTdx1QBw'>Youtube : Wannbe in LA</a>

# %%
sp['valence'].plot.box()

# %% [markdown]
# ### 2.1.5 Acoustic

# %%
music_ac_max = sp.iloc[sp['acoustic'].idxmax()]
music_ac_min = sp.iloc[sp['acoustic'].idxmin()]


# %%
print(music_ac_min)
print(music_ac_max)

# %% [markdown]
# BPM min : <a href='https://www.youtube.com/watch?v=GTyN-DB_v5M'>Youtube : Never Forget You</a>
# <br>
# BPM max : <a href='https://www.youtube.com/watch?v=KYZjvMmKqmw'>Youtube : Fusion</a>

# %%
sp['acoustic'].plot.box()

# %% [markdown]
# ### 2.1.6 Danceability

# %%
music_dy_max = sp.iloc[sp['danceability'].idxmax()]
music_dy_min = sp.iloc[sp['danceability'].idxmin()]


# %%
print(music_dy_min)
print(music_dy_max)

# %% [markdown]
# BPM min : <a href='https://www.youtube.com/watch?v=TX3Zr5RX1ug'>Youtube : Glaciers</a>
# <br>
# BPM max : <a href='https://www.youtube.com/watch?v=PtPAu17Vw_I'>Youtube : Get Dripped</a>

# %%
sp['danceability'].plot.box()

# %% [markdown]
# ## 2.2 Les corrélations
# %% [markdown]
# Nous pouvons observer les différentes corrélations entre *danceability* et les autres :

# %%
sp.corr()['danceability']

# %% [markdown]
# Tout ceci n'est pas très visuel. Arrangeons cela grâce à seaborn :

# %%
sns.heatmap(sp.corr())

# %% [markdown]
# Les points les plus clairs indiquent les endroits les plus corrélés. En nous concentrant exclusivement vers *danceability*, quelques éléments ressortent du lot : **energy, loud et valence**. D'ailleurs, sauvegardons-les dans une variable appelée **features**.

# %%
features = ['energy', 'loud', 'valence']

# %% [markdown]
# ## 2.3 Les outliers de loud
# %% [markdown]
# Comme nous l'avons précédemment vu, *loud* est constitué de plusieurs outliers. Maintenant, que faut-il en faire ?
# %% [markdown]
# Par principe, il ne faut ni les altérer ni les supprimer. S'il s'agissait d'outliers où nous sommes persuadés qu'ils sont dus à une erreur (humaine par exemple), alors, nous aurions pu les supprimer. Les outliers de loud ne doivent pas être retirés car ce ne sont pas des erreurs. Ainsi, nous allons les laisser comme tels.
# %% [markdown]
# ## 2.4 Scaling
# %% [markdown]
# N'oublions pas de normaliser nos features :

# %%
for feature in features:
    # normalisation
    sp['f_' + feature] = (sp[feature] - sp[feature].min()) / (sp[feature].max() - sp[feature].min())
    # standardisation
    #sp['f_' + feature] = (sp[feature] - sp[feature].mean()) / sp[feature].std()
    # no scaling
    #sp['f_' + feature] = sp[feature]


# %%
sp.head()

# %% [markdown]
# Modifions les noms de nos features :

# %%
features = list(map(lambda f: 'f_' + f, features))


# %%
features

# %% [markdown]
# # 3. Phase de construction de notre modèle
# %% [markdown]
# ***
# %% [markdown]
# ## 3.1 Avant la construction
# %% [markdown]
# ### 3.1.1 Que cherchons-nous ?
# %% [markdown]
# Nous cherchons à trouver le score de *danceability* d'une chanson à travers ses attributs : **energy, loud et valence**. Toutefois, nous commencerons à prédire ce score en utilisant uniquement **l'energy**.
# %% [markdown]
# Pour faire nos tests, nous utiliserons ces données ([40, -10, 50] = **l'energy, loud puis valence**) :

# %%
music_for_test = pd.DataFrame([[0.7, 0.5, 1]], columns = ['f_energy', 'f_loud', 'f_valence']).iloc[0]


# %%
music_for_test

# %% [markdown]
# ### 3.1.2 Procédure de la mise en place de l'agorithme du K-Nearest Neighbor
# %% [markdown]
# 1. Nous devons choisir nos données sur lesquelles nous allons effectuer notre prédiction.
# 2. Il faut calculer la distance entre tous nos éléments. 
# 2. Il faut trier nos données par ordre croissant de nos distances.
# 3. On sélectionne les K plus proches voisins (le K est spécifié au début de l'algorithme).
# 4. Soit on fait la moyenne (si notre y est une variable continue/entière) soit on prend le mode (si notre y est une variable nominale).
# %% [markdown]
# ## 3.2 Construction du modèle
# %% [markdown]
# Nous cherchons donc un score de *danceability*. Stockons cela dans une variable **target**.

# %%
target = 'danceability'

# %% [markdown]
# ### 3.2.1 Prédiction via un paramètre (soit energy)
# %% [markdown]
# Nous utiliserons **l'energy** pour essayer de prédire le score. Sauvegardons cela dans une variable **mono_feature**

# %%
mono_feature = 'f_energy'

# %% [markdown]
# #### 3.2.1.1 Calcul des distances
# %% [markdown]
# Calculons nos distances en créant une fonction :

# %%
def distance_bt_energy_musics(energy_1, energy_2):
    return sqrt(((energy_1 - energy_2) ** 2))

# %% [markdown]
# Exemple d'utilisation :

# %%
# la méthode sample sur une DataFrame nous donne un échantillon de nos données
# ici, nous lui demandons de nous renvoyer un échantillon composé d'une unité
random_music = sp.sample(1, random_state = 1).iloc[0]


# %%
random_music


# %%
distance_bt_energy_musics(random_music[mono_feature], music_for_test[mono_feature])

# %% [markdown]
# Le distance entre la musique aléatoire et la nôtre est de 0.11.
# %% [markdown]
# Maintenant, créons une nouvelle colonne **distance_energy** tout en faisant une copie de notre DataFrame :

# %%
e_music_test = music_for_test[mono_feature]
sp_dt_energy = sp.copy()
sp_dt_energy['distance_energy'] = sp_dt_energy['f_energy'].apply(lambda e: distance_bt_energy_musics(e, e_music_test))


# %%
sp_dt_energy.head()

# %% [markdown]
# #### 3.2.1.2 Trier par ordre croissant de distance

# %%
sorted_sp_dt_energy = sp_dt_energy.sort_values(by = 'distance_energy')


# %%
sorted_sp_dt_energy.head(10)

# %% [markdown]
# #### 3.2.1.3 On sélectionne les K plus proches voisins

# %%
k_neighbors_mono_feature = 5


# %%
neighbors_mono_feature = sorted_sp_dt_energy[:k_neighbors_mono_feature]

# %% [markdown]
# #### 3.2.1.4 On fait la moyenne de leur danceability

# %%
neighbors_mono_feature[target].mean()

# %% [markdown]
# #### 3.2.1.5 Sklearn est là pour nous épauler
# %% [markdown]
# Évidemment, cet algorithme n'est pas tout récent et celui-ci a déjà été implémenté dans la libraire scikit-learn.
# %% [markdown]
# Créons le modèle :

# %%
# on lui demande de se baser sur ses 5 proches voisons
# et nous avons spécifié l'algorithme en brute => c'est celui avec lequel nous avons précédemment travaillé
knn_mono = KNeighborsRegressor(5, algorithm = 'brute')

# %% [markdown]
# Donnons lui ensuite des données afin qu'il les "étudie" :

# %%
knn_mono.fit(sp_dt_energy[[mono_feature]], sp[target])

# %% [markdown]
# Enfin, nous pouvons lui demander de faire des prédictions :

# %%
knn_mono.predict(music_for_test[mono_feature])

# %% [markdown]
# ### 3.2.2 Multivariate K-Nearest Neighbors
# %% [markdown]
# Sous ce nom quelque peu imposant se cache un concept simple. Pour l'instant, nous n'avons utilisé qu'un seul paramètre pour prédire notre score. Ce n'est évidemment pas suffisant pour prédire avec précision la réalité. Une potentielle solution serait d'utiliser plusieurs paramètres : **energy, loud et valence**.
# %% [markdown]
# Lorsque vous utilisez plusieurs paramètres avec le K-Nearest Neighbors, on dit de lui qu'il est **multivariate**. 
# %% [markdown]
# Basons-nous sur le modèle que nous propose sklearn :

# %%
knn_multivariate = KNeighborsRegressor(5, algorithm='brute')

# %% [markdown]
# Entraînons notre modèle :

# %%
knn_multivariate.fit(sp[features], sp[target])

# %% [markdown]
# Réessayons de trouver le score de *danceability* de notre musique :

# %%
knn_multivariate.predict([music_for_test[features]])

# %% [markdown]
# Nous voyons que notre score a augmenté. Cependant, il est pour l'instant impossible de dire si notre premier modèle est meilleur que le second (ou l'inverse) !
# %% [markdown]
# Pour vérifier cela, nous allons devoir **l'évaluer**.
# %% [markdown]
# ### 3.2.3 Evaluation d'un modèle
# %% [markdown]
# Nous avons enfin obtenu un algorithme qui marche et qui est capable de réaliser des prédictions uniquement sur **l'energy**. Toutefois, cet algorithme n'est pas parfait et ne prédit pas à 100% un résultat réel. Nous nous devons donc de le contrôler à travers le procédé du **mean squared error**.
# %% [markdown]
# <img src='assets/mse_formula.png'/>
# %% [markdown]
# Ne soyez pas effrayé à cause de cette formule. Décomposons-là ensemble :
# 1. Dans la parenthèse, vous devez soustraire votre variable réelle 'target' et votre variable prédite (le résidu).
# 2. Réalisez ensuite le carré.
# 3. Répétez cette procédure autant de fois que vous avez d'éléments et additionnez-les.
# 4. Divisez ensuite par n (oui, il s'agit d'une moyenne).
# %% [markdown]
# Plus le résultat de cette formule sera proche de 0, meilleur sera votre modèle.
# %% [markdown]
# On peut déjà préparer nos Y (réels) :

# %%
Y = sp[target]

# %% [markdown]
# #### 3.2.3.1 Evalutation de notre premier modèle

# %%
Y_predicted_mono = knn_mono.predict(sp[[mono_feature]])


# %%
mse_mono = ((Y - Y_predicted_mono) ** 2).mean()
mse_mono

# %% [markdown]
# #### 3.2.3.2 Evaluation de notre second modèle

# %%
Y_predicted_multi = knn_multivariate.predict(sp[features])


# %%
mse_multi = ((Y - Y_predicted_multi) ** 2).mean()
mse_multi

# %% [markdown]
# Pour aller plus vite dans le calcul du **mse**, nous pouvons utiliser la fonction **mean_squared_error** de sklearn :

# %%
mean_squared_error(Y, Y_predicted_multi)

# %% [markdown]
# #### 3.2.3.3 Verdict
# %% [markdown]
# Grâce à ce mécanisme, nous pouvons dire que le second modèle est meilleur que le premier.

# %%
mse_multi < mse_mono

# %% [markdown]
# # 4. Utilisons l'outil sklearn
# %% [markdown]
# ## 4.1 Préparons nos données pour entraîner et tester notre modèle

# %%
train, test = train_test_split(sp, test_size=0.2, random_state = 1)


# %%
train.head()

# %% [markdown]
# ## 4.2 Créer et entraîner notre modèle

# %%
# Nous le créons
knn = KNeighborsRegressor(n_neighbors = 5, algorithm = 'brute')


# %%
# Nous l'entraînons
knn.fit(train[features], train[target])


# %%
# Nous réalisons une prédiction
knn.predict([random_music[features]])

# %% [markdown]
# ## 4.3 Tester notre modèle
# %% [markdown]
# ### 4.3.1 La validation croisée : théorie
# %% [markdown]
# sklearn nous propose quelques outils pour tester rapidement et facilement nos modèles. L'un d'entre eux se nomme ***KFold***. Afin de comprendre à quoi il correspond réellement, nous devons comprendre un nouveau concept : **l'entrainement** et le **test**.
# %% [markdown]
# Quand on **entraîne** un modèle, on extraira une partie de notre base de données afin de lui faire apprendre de nouvelles informations. Cette partie-là possède un nom : **training set**. Généralement, on utilise **80%** de nos ressources en tant que **training set**.
# %% [markdown]
# Dès lors, il nous reste logiquement 20% qui est non affecté. Justement, ces **20%** vont être utilisés pour **tester** notre modèle fraîchement construit.
# %% [markdown]
# L'outil ***KFold***, lui, fait tout ça à notre place et bien plus. Une image valant plus de mille mots :
# %% [markdown]
# <img src='http://i.imgur.com/gu3Fa6w.png'/>
# %% [markdown]
# <div style='text-align: center'>Source : Dataquest - <a href='http://i.imgur.com/gu3Fa6w.png'>lien de l'image</a></div>
# %% [markdown]
# En nous basant sur l'image, nous pouvons remarquer que le ***KFold*** réalise plusieurs itérations. Lors de chaque itération, il vous procure un **training** et un **test** set différent à chaque fois. Grâce à cela, il sera plus facile de tester la viabilité de votre modèle en fonction de la même source de données.
# %% [markdown]
# En nous basant sur une instance de KFold, nous pourrons réaliser n-boucles où nous créerons des modèles afin de vérifier leur mse (mean squared error). Leur mse, nous les stockerons dans un tableau. À la fin de notre boucle, nous pouvons effectuer la moyenne des mse afin de détecter de potentielles anomalies ou non (par exemple : l'overfitting).
# %% [markdown]
# Toute cette procédure porte un nom : **la validation croisée**.
# %% [markdown]
# ### 4.3.2 La validation croisée : pratique
# %% [markdown]
# On importe le module en question 

# %%
from sklearn.model_selection import KFold

# %% [markdown]
# On crée une instance de ***KFold***

# %%
kfold = KFold(n_splits= 5, shuffle= True, random_state= 1)

# %% [markdown]
# Analysons ensemble les arguments entrés :
# 1. Lorsque l'on va appeler la méthode pour "découper" nos données, on lui demande d'en faire 5 découpes/itérations. Par conséquent, il nous fournira 5 training sets et 5 test sets. Ces training/test sets **contiennent uniquement des indices et non les données en elles-mêmes**.
# 2. On lui demande de mélanger nos données aléatoirement.
# 3. On peut également parler de *seed*. Grâce à ce concept, l'algorithme va mélanger les données sur base de cette information.
# %% [markdown]
# Afin de récupérer nos "découpes", on envoie un message à la méthode *split* en lui passant en argument notre dataset.
# %% [markdown]
# Nous réaliserons :

# %%
# on crée notre tableau où nous stockerons les mse
mses = []
# on exécute nos découpes
for train_i, test_i in kfold.split(sp):
    # grâce aux indices que nous donne notre découpe, on sélectionne notre training et test set
    train = sp.iloc[train_i]
    test = sp.iloc[test_i]
    # on crée notre modèle
    knn_fold = KNeighborsRegressor(5, algorithm = 'brute')
    # on les lui fait apprendre 
    knn_fold.fit(train[features], train[target])
    # on réalise nos prédictions
    predictions = knn_fold.predict(test[features])
    # on calcule son mse
    mse = mean_squared_error(test[target], predictions)
    # on ajoute son mse à notre tableau
    mses.append(mse)


# %%
print('MSES :', mses)
print('Var MSE', np.var(mses))
print('MSE avg :', np.mean(mses))


# %%
plt.scatter(list(range(len(mses))), mses, label = 'mses')
plt.scatter(5, [len(mses) + 1], label = 'mse of our model')
plt.axhline(np.mean(mses), color = 'black', label = 'mean of mses')
plt.legend()

# %% [markdown]
# Pourquoi notre modèle a-t-il un mse bien plus faible que les autres ? La réponse est simple : nous lui avons donné beaucoup plus de données qu'aux autres modèles. Par conséquent, il sait prédire avec plus d'efficacité le futur => d'où son mse plus faible.
# %% [markdown]
# ### 4.3.3 Cross val score
# %% [markdown]
# Tout ce que l'on vient de produire au-dessus peut être réalisé avec l'aide de la fonction **cross_val_score**.
# %% [markdown]
# Celle-ci prend en considération plusieurs arguments :
# 1. une instance vierge de votre modèle
# 2. tous vos X (sous une forme de tableau à **deux dimensions**)
# 3. tous vos y (sous une forme de tableau à **une dimension**)
# 4. scoring = le type de valeur qu'il doit calculer. Nous utiliserons "neg_mean_squared_error"
# 5. cv (cross validation) = une instance de KFold (entre autres)
# %% [markdown]
# En suivant toutes ces règles :

# %%
blank_model = KNeighborsRegressor(n_neighbors=5, algorithm='brute')
kfold = KFold(n_splits=5, shuffle=True, random_state=1)
cross_val_score(blank_model, sp[features], sp[target], scoring="neg_mean_squared_error", cv=kfold)

# %% [markdown]
# ### 4.3.4 À la recherche du MSE minimal
# %% [markdown]
# En faisant appel à **cross_val_score**, nous allons tenter de trouver les features les plus pertinentes ainsi que le bon nombre de voisins.
# %% [markdown]
# Commençons par créer une variable "features_optimal" (pour plus de facilitée, nous ne prenons que les variables d'origines [nous ignorons les variables normalisées/standardisées]) et une liste de voisins :

# %%
# 1er essai
# features_optimal = ['bpm', 'energy', 'valence', 'loud', 'acoustic', 'popularity', 'length_minutes']
# MSE = 156
# 2e essai
# features_optimal = ['bpm', 'energy', 'valence', 'loud', 'acoustic', 'popularity']
# MSE = 137
# ---> le MSE a baissé en retirant length_minutes. Alors, nous le supprimons définitivement
# 3e essai
# features_optimal = ['bpm', 'energy', 'valence', 'loud', 'acoustic']
# MSE = 157
# ---> en supprimant popularity, mon MSE a augmenté. Donc, nous ne le supprimons pas
# 4e essai
# features_optimal = ['bpm', 'energy', 'valence', 'loud', 'popularity']
# MSE = 139
# ---> le MSE a augmenté, nous ne supprimons pas acoustic
# 5e essai
features_optimal = ['bpm', 'energy', 'valence', 'acoustic', 'popularity']
# ---> en supprimant loud, mon MSE reste toujours à 137. Supprimons le pour baisser la complexité de notre modèle
# ---> et ainsi de suite...
K = list(range(1, 31))

# %% [markdown]
# Pour trouver le MSE minimal, retirez au fur et à mesure les features qui font diminuer votre MSE.

# %%
matrix_mse = []
for k in K:
    blank_model = KNeighborsRegressor(n_neighbors=k, algorithm='brute')
    kfold = KFold(n_splits=5, shuffle=True, random_state=k)
    mses = abs(cross_val_score(blank_model, sp[features_optimal], sp[target], scoring="neg_mean_squared_error", cv=kfold))
    matrix_mse.append(mses)


# %%
# nous réalisons la moyenne de chaque ligne
# ainsi, chaque valeur sera la moyenne de chaque valeur de k
mses_by_k = np.mean(matrix_mse, axis = 1)


# %%
min(mses_by_k)


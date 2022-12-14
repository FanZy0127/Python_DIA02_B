import numpy as np

m = np.random.randint(1, 20, (10, 10))

# Affichez les multiples de 3 de la première ligne du tableau m.
print(f'MULTIPLES DE 3 DE LA PREMIÈRE LIGNE : \n {m[0][m[0] % 3 == 0]}')

# Affichez la deuxième colonne et faite la somme des nombres pairs de cette colonne.
# On compte le nombre de nombre pair de la deuxième colonne
print(f'DEUXIÈME COLONNE : {m[:, 1]}')
mask = m[:, 1] % 2 == 0
print(f'SOMME DES NOMBRES PAIRS DE LA DEUXIÈME COLONNE : {mask.sum()}')

# Total des nombres pairs de la deuxième colonne
print(f'NOMBRES PAIRS DE LA DEUXIÈME COLONNE : {m[:, 1][mask]}')
print(f'TOTAL DES NOMBRES PAIRS DE LA DEUXIÈME COLONNE : {(m[:, 1][mask]).sum()}')

# Faites la somme des lignes puis des colonnes qui contiennent au moins un 1.

print(np.isin(m, 1))
mask_one = np.isin(m, 1)
# ligne
print(m)
print('----')
print(m[np.any(mask_one, axis=1)])
print('---')
print(m[np.any(mask_one, axis=1)].sum())
# si on voulait faire la somme que des lignes extraites
# print(m[ np.any(mask_one, axis=1) ].sum(1))
print('----')
# On peut également raisonner sur les lignes uniquement et pas les colonnes  
print(m.T[np.any(np.isin(m.T, 1), axis=1)].sum())

# Comme axis transpose le mask par rapport aux colonnes on doit alors l'appliquer aux colonnes de la matrice 
print(m.T[np.any(np.isin(m, 1), axis=0)].sum())


print('----')

# Reprenez le tableaux m et faite la somme de chaque colonne que vous placerez dans un tuple.
print(f'SOMME DE CHAQUE COLONNE DANS UN TUPLE : {tuple(m.sum(0))}')

# Même consigne mais maintenant pour les lignes.
print(tuple(m.sum(1)))

# Faites la somme des valeurs paires des colonnes.

"""
Baptiste
columns = m.shape[1]
total = 0
for i in range(columns):
    column = m[:, i]
    total += column[column % 2 == 0].sum()
print(total)
"""

print(f'SOMME DES COLONNES : {m.T[(m.T % 2) == 0].sum(0)}')

# Calculez la moyenne des valeurs et l'écart type.
print(f'MOYENNE DES VALEURS : {np.mean(m)}')
print(f'ÉCART TYPE : {(np.std(m))}')

# Créez un nouveau tableau à partir des valeurs paires de la matrice m
mask = m % 2 == 0 
neo_m = np.array(m[mask], copy=True)
print(neo_m)

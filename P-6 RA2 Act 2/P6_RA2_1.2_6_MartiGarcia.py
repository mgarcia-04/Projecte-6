def multiplica_tot(*nombres):
    resultat = 1
    for nombre in nombres:
        resultat *= nombre
    return resultat

print("Multiplica 2, 3, 4:", multiplica_tot(2, 3, 4))
print("Multiplica 5, 10:", multiplica_tot(5, 10))
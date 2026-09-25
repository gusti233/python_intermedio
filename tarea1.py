#Suarez Zeniquel Tomas Alfonso 

A = {1, 2, 3, 4}
B = {3, 4, 5, 6}

# 1. union 
print("Unión:", A.union(B))

# 2. interseccion
print("Intersección:", A.intersection(B))

# 3. diff simetrica
print("Diferencia simétrica:", A.symmetric_difference(B))

# 4. A subconjunto de B? 
print("¿A es subconjunto de B?:", A.issubset(B))

# 5. nro de elementos de A
print("Cantidad de elementos en A:", len(A))
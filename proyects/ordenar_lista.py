lista = [4,5,8,12,14,1,8,9]

n= len(lista)

for x in range(n):
    for j in range(n-1):
        elemento_actual = lista[j]
        siguiente = lista[j+1]
        
        if elemento_actual > siguiente:
            lista[j] = siguiente 
            lista[j + 1] = elemento_actual
            
print(lista)
from itertools import combinations

caracteres = ['J', 'X', 'Y']
permsList = ['-'.join(x) for x in combinations(caracteres, 2)]
print(permsList) # ['00', '01', '02', '10', '11', '12', '20', '21', '22']
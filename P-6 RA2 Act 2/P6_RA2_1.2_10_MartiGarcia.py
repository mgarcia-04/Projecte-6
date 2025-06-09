def filtra_parells(llista):
    return [num for num in llista if num % 2 == 0]

print("Parells de [1, 2, 3, 4, 5, 6]:", filtra_parells([1, 2, 3, 4, 5, 6]))
print("Parells de [10, 15, 20, 25, 30]:", filtra_parells([10, 15, 20, 25, 30]))
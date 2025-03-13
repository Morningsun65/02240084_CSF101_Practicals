first_list = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
inverse_list = []

index = len(first_list)  -1


while index >= 0:
    inverse_list.append(first_list.pop())  
    index -= 1  

print(inverse_list)  
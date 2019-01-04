my_list = [1,2,3,4,5,6,7,8,9,1,1,2,2,3,3,3,5,6,6,6,6,7,9,9]

for i in range (0, len(my_list)):
    temp = my_list[i]
    for j in range (0, len(my_list)):
        if i == j:
            continue
        if temp == my_list[j]:
            print(str(temp) + " has been repeated")
            break
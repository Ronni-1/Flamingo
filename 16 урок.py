# i = 1
# j = 0
# i,j = j,i
# print(i,j)

mass = [[1, 2, 3], [7, 8, 9]]
#print(mass[::-1])
for i in range(len(mass)):
    print(i)
    print()
    for j in range(len(mass)-1, 1, 1):
        print(mass[i][j],  j)
print()


           #0          1          2
mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
    #    0, 1, 2    0, 1, 2    0, 1, 2

# for t in mass:
#     print(t)
#
# print()
for i in range(len(mass)-1): #2 массив
    for j in range(len(mass)-1): #0  ---4
        if i > j:  # i == 1 j == 4
            mass[i][j],mass[j][i] = mass[j][i],mass[i][j] #mass 0,4 = mass 4,0  ---> mass 4,0

    for t in mass:
        print(t)
    print()
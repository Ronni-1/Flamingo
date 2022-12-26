# n = 3
# m = 3
# mass = [[0]*n]*m
#
# for i in range(len(mass)):
#     for j in range(len(mass[i])):
#         if i == 0:
#             mass[0][j] = 1
#             # mass[i][j] = 1
#         # elif i == 0:
#             # mass[i][j] = mass[i-1][j] + mass[i][j-1]
#     print(mass)



mass = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]
n = len(mass)
r = 0
for i in range(len(mass)):
    for j in range(len(mass[-1])):
        if j == n-1-i:
            print(mass[i][j])



matr = []
while True:
    rows = input()
    if rows != "end":
        matr += [[int(i) for i in rows.split()]]
    else: break

new_m = []
for i in range(len(matr)):
    # print(i, '=', end=' ')
    for j in range(len(matr[i])):
        print(matr[(i+1) % len(matr)][j], matr[i][(j+1) % len(matr[i])], matr[i-1][j], matr[i][j-1])
        break
        # print(matr[i][j], end=' ')




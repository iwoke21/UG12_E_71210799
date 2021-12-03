f = int(input("Masukan awal deret: "))
e = int(input("Masukan akhir deret: "))

for j in range(f,e):
    if j % 2 == 0:
        if j % 5 != 0 and j % 9 != 0:
            print(j, end=" ")
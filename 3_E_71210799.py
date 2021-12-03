WOo = int(input("masukan angka :"));
limit= WOo;
for bintang in range (0,WOo):
    for  pola in range (-2, limit+1):
         print(" ",end="")

    for shape in range (0, bintang+1):
        print("* ", end="")
    limit-=1
    print("")

limit=WOo;
for bintang in range (1,WOo):
    for pola in range (-4, bintang):
        print(" ",end="")

    for shape in range (1, limit):
        print("* ",end="")
    limit-=1
    print("")


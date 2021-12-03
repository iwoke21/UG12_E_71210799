def variabel_a(deret_bilangan):
    variabel_b = deret_bilangan[0]
    for variabel in deret_bilangan:
        if variabel > variabel_b:
            variabel_b = variabel
    return variabel_b
def variabel_y(deret_bilangan):
    variabel_c = deret_bilangan[0]
    for variabel in deret_bilangan:
        if variabel < variabel_c:
            variabel_c = variabel
    return variabel_c

a=[3, 20, 100, -35 ,50]
print (a)
print('nilai terbesar: ', variabel_a(a))
print('nilai terkecil: ', variabel_y(a))
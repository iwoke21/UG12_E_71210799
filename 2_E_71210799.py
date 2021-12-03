senin  =['ke- algoritma graf','ke-3 sistem operasi','ke-4 pak','ke-5 praktikum inlan']
selasa =['ke-2 matematika teknik','ke-4 bahasa indonesia','ke-6 pkm']
kamis  =['ke-1 ','ke-3 logmat ','ke-4 prakkom'] 
jumat  =['ke-2 sistem basis data','ke-4 prakom sistem basis data ','ke-6 inlan']

n = input("hi tutu, silakan masukin hasil yang ingin anda telusuri : ")
if n == "senin" :
    for i in range (len(senin)):
        print ("kelas", senin[i])
elif n == "selasa" :
    for i in range (len(selasa)):
        print ("kelas", selasa[i])
elif n == "rabu" :
        print ("hari rabu anda tidak ada kelas")
elif n == "kamis":
    for i in range (len(kamis)):

        print ("kelas", kamis[i])
elif n == "jumat" :
    for i in range (len(jumat)):
        print ("kelas", jumat[i])
 


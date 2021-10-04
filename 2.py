n = int (input("masukkkan angka : ")) #harus ganjil
print ()
k1 = int(n/2+1)

for i in range (n):
    for j in range (n):
        if (i + j) % 2 == 0 :
            print ("&", end="")
        else: 
            print ("-", end="")
    print ("\n")

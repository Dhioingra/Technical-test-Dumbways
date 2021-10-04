#Variabel
total_jarak = 64500
Percepatan = (5-3)/1380
titik_percepatan_c = 3 + Percepatan * 2100
total_jarak_ke_c = 3 * 2100 + 1/2 * (Percepatan * 2100**2)
kecepatan_konstan = (3 + Percepatan * 720) - 3
total_waktu = (total_jarak - total_jarak_ke_c) / kecepatan_konstan

#jawaban
detik = total_waktu
menit = detik / 60
jam = menit / 60

print ("Waktu yang ditempuh Ismail adalah ", jam, "jam")
print ("Waktu yang ditempuh Ismail adalah ", menit, "menit")
print ("Waktu yang ditempuh Ismail adalah ", detik, "detik")

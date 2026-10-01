nilai= int (input("masukkan nilai="))

if nilai >= 100:
   print ("nilai anda diatas rata-rata")

elif nilai >= 90 and nilai < 100:
    print ("nilai anda di bawah rata-rata")

elif nilai <= 80:
    print ("nilai anda sangat jelek")
#materi baru 
#
#
nilai= 20
nilai= 100

if nilai >= 30 and nilai <= 60:
    print ("nilai benar")

else:
    print ("nilai salah")
#materi baru
#
#
#temperature
ac= 0.0
penghangat= "mati"
temperature= 0.0
temperature= float(input("masukkan suhu:"))

if temperature <20.0:
    penghangat= "nyala"
    print ("kondisi penghangat =", penghangat)
elif temperature >=20.0 and temperature <=30.0:
    print ("kondisi stabil")
    print("penghangat =", penghangat, "ac =", ac)
elif temperature >30.0:
    ac= "nyala"
    print ("kondisi ac =", ac)
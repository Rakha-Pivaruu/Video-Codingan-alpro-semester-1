makanan = ["ayam goyeng", "mie goyeng", "sate ayam" ]
minuman = ["es teh", "es jeruk", "jus alpukat"]

harga_makanan =  [15.0, 12.0, 10.0]
harga_minuman = [5.0, 6.0, 8.0]

ayam_goyeng_dan_es_teh = harga_makanan[0] + harga_minuman[0]
mie_goyeng_dan_es_jeruk = harga_makanan[1] + harga_minuman[1]
sate_ayam_dan_jus_alpukat = harga_makanan[2] + harga_minuman[2]

paket1 = "ayam goyeng_dan_es_teh"
paket2 = "mie goyeng_dan_es_jeruk"
paket3 = "sate_ayam_dan_jus_alpukat"

print ("paket 1 adalah" , paket1, "dengan harga" , ayam_goyeng_dan_es_teh)
print ("paket 2 adalah" , paket2, "dengan harga" , mie_goyeng_dan_es_jeruk)
print ("paket 3 adalah" , paket3, "dengan harga" , sate_ayam_dan_jus_alpukat)

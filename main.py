sozluk = {
    "Oyun": "GTA V",
    "Eşya": "Doblo Sağ Ön Farı",
    "Takım": "Fenerbahçe",
    "Ülke": "Türkiye"
}

aranan_key = input("Aradığınız kategoriyi/key'i girin: ")

try:
    print(aranan_key,":",sozluk[aranan_key])
except KeyError:
    print("Hata:", aranan_key, "anahtarı sözlükte bulunamadı.")

urunAfiyat = 4000
urunBfiyat = 3000
kdvOrani = 0.18

# Ürün fiyatlarına KDV eklenmiş fiyatları hesaplama
print(urunAfiyat + (urunAfiyat * kdvOrani))
print(urunBfiyat + (urunBfiyat * kdvOrani))

urunToplam = urunAfiyat + urunBfiyat
print(urunToplam + (urunToplam * kdvOrani))

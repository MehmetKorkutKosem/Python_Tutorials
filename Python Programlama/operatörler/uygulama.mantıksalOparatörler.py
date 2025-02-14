#1. Girilen bir sayının 0-100 arasında olup olmadığını kontrol edin.
sayi = int(input("Bir sayi girin: "))
if (sayi >= 0 and sayi <= 100):
    print("Sayi 0 ile 100 arasinda.")
else:
    print("Sayi 0 ile 100 arasinda değil.")
#2. Girilen bir sayının pozitif çift sayı olup olmadığını kontrol edin.
sayi = int(input("Bir sayi girin: "))
if (sayi > 0 and sayi % 2) == 0:
    print("Sayi pozitif ve çift.")
else:
    print("Sayi pozitif çift değil.")

#3. Email ve parola bilgileri ile giriş kontrolü yapın.
email = "ornek@ornek.com"
parola = "12345"

girilenemail = input("Email: ")
girilenparola = input("Parola: ")

if girilenemail == email and girilenparola == parola:
    print("Giriş başarili.")
else:
    print("Email veya parola hatali.")
# 4. Girilen 3 sayıyı büyüklük olarak karşılaştırın.
sayi1 = int(input("1. sayiyi girin: "))
sayi2 = int(input("2. sayiyi girin: "))
sayi3 = int(input("3. sayiyi girin: "))

if sayi1 >= sayi2 and sayi1 >= sayi3:
    print("En büyük sayi:", sayi1)
elif sayi2 >= sayi1 and sayi2 >= sayi3:
    print("En büyük sayi:", sayi2)
else:
    print("En büyük sayi:", sayi3)
# 5. Kullanıcıdan 2 vize (%60) ve final (%40) notunu alıp ortalama hesaplayın. Ortalama 50 ve üstündeyse geçti, değilse kaldı yazdırın.
vize1 = float(input("1. vize notu: "))
vize2 = float(input("2. vize notu: "))
final = float(input("Final notu: "))

ortalama = (vize1 * 0.3) + (vize2 * 0.3) + (final * 0.4)
if(final==70):
    print("geçti")
else:
   if ortalama >= 50 and final >= 50:
    print("Geçti.")
   else:
    print("Kaldi.")

# 6. Kişinin ad, kilo ve boy bilgilerini alıp kilo indekslerini hesaplayın ve hangi gruba girdiğini yazdırın.

ad = input("Adiniz: ")
kilo = float(input("Kilonuz (kg): "))
boy = float(input("Boyunuz (m): "))

vki = kilo / (boy ** 2)

print(f"{ad}'in Vücut Kitle İndeksi: {vki}")

if vki < 18.5:
    print("Zayif")
elif vki >= 18.5 and vki <= 24.9:
    print("Normal")
elif vki >= 25 and vki <= 29.9:
    print("Fazla Kilolu")
elif vki >= 30 and vki <= 34.9:
    print("Şişman (Obez)")
else:
    print("Obez")


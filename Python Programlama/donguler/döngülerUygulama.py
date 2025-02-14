import random
# artır ve azalt komutları ile sayi bulma
# Random bir sayı oluştur
sayi = random.randint(0, 10)
print(sayi)
mod = 10 / 2
kontrol = ""

# Sonsuz döngü
while True:
    if mod > sayi:
        print("mod sayidan büyüktür")
    elif mod < sayi:
        print("mod sayidan küçüktür")
    else:
        print(f"sayı {sayi}")
        break
    
    # Kullanıcıdan giriş alma
    kontrol = input("Artır veya azalt (artır/azalt) girin: ").strip().lower()
    
    if kontrol == "artır":
        mod += 1
    elif kontrol == "azalt":
        mod -= 1
    else:
        print("Geçersiz giriş, lütfen 'artır' veya 'azalt' girin.")
   # kullanıcı girişli tahmin
sayi2 = random.randint(0, 100)
hak=5
    
while True :
         tahmin=int(input("sayi giriniz"))
         if tahmin >sayi :
             print("sayi kucuk")
             hak-=1
         elif tahmin <sayi:
             print("sayi buyuk")
             hak-=1
         else :
             print(f"sayi{sayi} bildiniz ")
             print(hak*20) 
             break
# girilen sayinin asal sayi olup olmadığını kontrol etme
sayi=int(input("sayi giriniz"))
if sayi == 1:
    print("sayi asal degil")
else :
    for x in range(2,sayi,1):
       if sayi%x==0 :
           print("sayi asal degil")
           break
if x==sayi-1:
    print("sayi asal")
              
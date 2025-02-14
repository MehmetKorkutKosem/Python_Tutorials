# oluşturulan listedeki sayılar arsından ucun katı olanı yazdır,sayıların toplamını yazdır,
sayilar=[]
toplam=0
a=int(input("girilecek sayi miktarini giriniz"))
for x in range(a):# randge belirlediğimiz aaralıkta for döngüsünün dönmesin için
 sayi=int(input("sayi giriniz"))
 sayilar.append(sayi)# sayıları for döngüsü yardımıyla eklemek için
 
for x in sayilar:
    toplam+=x
    if x%3==0:
        print(f"{x} ucun kati")
    if x%2!=0 :
        print(x**2)
print(toplam)
# sehirlerden oluşan bir dizi oluştur oluşturduğun şehirler arasında uzunluğu en fazla beş karakterden oluşan şehirleri ekrana yazdır
sehirler=[]
a=int(input("girilecek sehir sayisini belirleyiniz"))
for x in range(a):
   sehir=str(input("sehir giriniz"))
   sehirler.append(sehir)
 
for x in sehirler:
   if len(x)<=5 :
      print(f"{x} kelimesinin uzunlugu")

# Kullanıcıdan döngü sayısını alıyoruz

a = int(input("Döngü sayısını giriniz (şehir sayısı): "))

# Şehirler ve fiyatları tutacak liste
telefon_fiyat_listesi = []


for i in range(a):
   
    name = input(f"{i+1}. telefon ismini giriniz: ")
    price = input(f"{i+1}. telefon fiyatını giriniz: ")
    
    
    telefon_fiyat_listesi.append({"name": name, "price": price})


print(telefon_fiyat_listesi)
toplam=0
for urun in telefon_fiyat_listesi :
    fiyat=int(urun["price"])
    toplam+=fiyat
    if fiyat<=5000 :
        print(urun)

print(toplam)
 




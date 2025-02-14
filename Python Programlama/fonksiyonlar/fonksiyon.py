def yaz():        
    print("hello")

def yaz1(name="invalid"):
    print(f"hello {name}")

def yazi(name="invalid"):
    return "hello"+" "+name

def topla(sayi1,sayi2):# iki parametre alır
    return sayi1+sayi2 # sayi1 ve sayi2 parametresinin toplamını çevirir

def age(dogumYili,yil):
    return yil-dogumYili

def emeklilik(dogumYili,yil,isim):
    ''' DOCSTRING= emeklilik yasina kalan miktari hesaplama
        INPUT= dogum yili , bulundugumuz yil , isim
        OUTPUT= emeklilige kalan yil'''
    yas=age(dogumYili,yil)
    kalan=65-yas
    print(isim+" "+ str(kalan))


yaz() # temel fonksiyon tanımı
yaz1("ali") # parametre olarak aliyi alır ve yazdırır
yaz1()# parametre almaz default olarak tanımlanan değeri alır " invalid"
result=yazi()
print(yazi())# print içinde doğrudan yazdırılabilir veya yeni bir değişkene atanıp ardından değiştirilebilir
print(result)
print(topla(1,2))
a=int(input("dogum yilinizi giriniz"))
b=int(input("bulundugunuz yili giriniz"))
print(age(a,b))
emeklilik(a,b,"ali")
print(help(emeklilik))
